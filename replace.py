for f in files:

    with open(directory + '/' + f, 'r') as file_in:
        text = ''
        for line in file_in.readlines():
            #print(line)
            if line.startswith('-- Generated by Ora2Pg, the Oracle database Schema converter, version 18.2'):
                continue
            if line.startswith('-- Copyright'):
                continue
            if line.startswith('-- DATAS'):
                continue
            if line.startswith('SET client'):
                continue
            if line.startswith('\set ON'):
                continue
            if line.startswith('SET check_'):
                continue
            if line.isspace():
                continue
            else:
               # file_in.write(line);
                #print(line)
                text = text + line
    print(text)
    with open(directory + '/' + f, "w") as file_out:
        file_out.write(text)
            

