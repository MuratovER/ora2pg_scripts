import psycopg2
import sys
import os
from datetime import datetime

con = None
#directory with files, that will be checked
directory = 'C:\\test\\check'
files = os.listdir(directory)
print("Number of files: " + str(len(files)))
#print all files in the directory \\check
#print(files)

#count for naming the files
succ_count = 1
time = datetime.now().strftime('%Y-%m-%d_%H-%M')

for file_name in files:
    #open every file
    with open(directory + '/' + f, 'r') as file_in:
        text = file_in.read()
        #print("Query:")
        #print(text)
        #print("_____________")
        try:
            #establishing connetction to db
            con = psycopg2.connect("host='localhost' dbname='dbname' user='postgres' password='1'")   
            cur = con.cursor()
            #query execution
            cur.execute(text)
            con.commit()
        except (psycopg2.DatabaseError as e):
            #if error happens, sql file moves to folder \\error
            if con:
                con.rollback()

            print('Error %s' % e)    
            file_in.close()
            #moving to file to folder \error
            os.rename("C:\\test\\check\\" + file_name, "C:\\test\\error\\" + file_name)
            with open(directory + '/' + time + '.log', "a") as file_out:
                file_out.write(file_name + "\n")
                file_out.write(e + "\n")
                file_out.write("\n" + "\n" + "\n")
            
            
        else:
            #if there is no erros, file moved to folder \\ready
            file_in.close()
            #moving the file
            os.rename("C:\\test\\check\\" + file_name, "C:\\test\\ready\\" + str(succ_count) + '_' + file_name)
            succ_count +=1
            

        finally:   
            if con:
                con.close()
        
        #print("\n")
