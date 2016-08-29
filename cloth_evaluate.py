import random

if __name__ == '__main__':
    clothes = []
    with open('clothes.csv','r') as f:
        clothes = f.readlines()

    result = []
    for i in range(50):
        max = random.randint(1,3)
        line = []
        for j in range(3):
            if j < max:
                choice = random.choice(clothes)
                choice_split = choice.split(',')
                line.append(choice_split[6].replace('\n',''))
            else:
                line.append('\"null\"')
        eval = random.randint(0,100)
        line.append('\"'+str(eval)+'\"')
        result.append(','.join(line))

    with open('cloth_evaluate.csv','w') as f:
        f.write('\"clothes1\",\"clothes2\",\"clothes3\",\"osyaredo\"\n')
        for i,d in enumerate(result):
            f.write(d+'\n')


