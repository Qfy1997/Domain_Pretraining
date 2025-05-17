

if __name__=='__main__':
    with open('train.txt','r') as f:
        train_data = f.readlines()
    with open('test.txt','r') as f:
        test_data = f.readlines()
    corpus=[]
    print(train_data[1].strip().split('\t'))
    for i in range(1,len(train_data)):
        corpus.append(train_data[i].strip().split('\t')[3].split(' '))
        corpus.append(train_data[i].strip().split('\t')[4].split(' '))
    for i in range(1,len(test_data)):
        corpus.append(test_data[i].strip().split('\t')[3].split(' '))
        corpus.append(test_data[i].strip().split('\t')[4].split(' '))
    print(corpus[0])
    with open('corpus.txt','a') as f:
        for i in range(len(corpus)):
            for item in corpus[i]:
                f.write(item)
                f.write(' ')
    

