import psycopg2
import sys
import os
con = None

directory = 'C:\\test\\check'
files = os.listdir(directory)
print("Number of files: " + str(len(files)))
print(files)

error_count = 1
succ_count = 1
for f in files:

    with open(directory + '/' + f, 'r') as file_in:
        text = file_in.read();
        print("Query:")
        print(text)
        print("_____________")
        try:
            con = psycopg2.connect("host='localhost' dbname='testdb' user='postgres' password='1'")   
            cur = con.cursor()
            cur.execute(text)
            while True:
                row = cur.fetchone()
 
                if row == None:
                    break
 
                print("Product: " + row[1] + "\t\tPrice: " + str(row[2]))
       # con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()

            print('Error %s' % e)    
            #sys.exit(1)
            #sys.exit(0)
            file_in.close();
            os.rename("C:\\test\\check\\" + f, "C:\\test\\error\\" + str(error_count) + '_' + f)
            error_count +=1
            
        else:
            file_in.close();
            os.rename("C:\\test\\check\\" + f, "C:\\test\\ready\\" + str(succ_count) + '_' + f)
            succ_count +=1
            

        finally:   
            if con:
                con.close()
        
        print("\n")