
if __name__ == '__main__':
    path = 'cloth_evaluate.csv'
    db = 'ApparelStrategy.osyaredo'
    result = []
    data = []
    with open(path,'r') as f:
        data = f.readlines()

    header = ''

    for i,d in enumerate(data):
        if i == 0:
            split = d.split(',')
            header = ','.join(split).replace('\"','`')
        else:
            split = d.split(',')
            values = ','.join(split)
            da = 'insert into '+db+' ('+header + ') values ('+values+');'
            #da = da.replace('\"','`')
            result.append(da)
    with open(path+'.sql','w') as f:
        for i,d in enumerate(result):
            f.write(d+'\n')
