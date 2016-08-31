import hashlib

if __name__ == '__main__':
    data = []
    with open('personal_infomation.csv','r') as f:
        data = f.readlines()

    with open('personal.csv','w') as f:
        f.write('\"point_id\",\"user_name\",\"user_pronoun\",\"sex\",\"phone\",\"email\",\"address\",\"age\"\n')
        for i,d in enumerate(data):
            if i == 0:
                continue
            d = d.split(',')
            name = d[1]
            pronoun = d[2]
            sex = d[3]
            phone = d[4]
            email = d[5]
            address = d[7] +' '+d[8]+' '+d[9]+' '+d[10]+' '+d[11]
            age = d[12].replace('\n','')
            code = '{0:04d}'.format(i)
            f.write('\"'+code+'\",\"'+name+'\",\"'+pronoun+'\",\"'+sex+'\",\"'+phone+'\",\"'+email+'\",\"'+address+'\",\"'+age+'\"\n')