

if __name__=='__main__':
    with open('./train.txt','r') as f:
        train_data = f.readlines()
    with open('./test.txt','r') as f:
        test_data = f.readlines()
    corpus=[]
    for i in range(1,len(train_data)):
        # print(train_data[i].strip().split('\t'))
        corpus.append(train_data[i].strip().split('\t')[3])
        corpus.append(train_data[i].strip().split('\t')[4])
        # break
    for i in range(1,len(test_data)):
        # print(test_data[i].strip().split('\t'))
        corpus.append(test_data[i].strip().split('\t')[3])
        corpus.append(test_data[i].strip().split('\t')[4])
        # break
    # print(len(corpus))
    with open('corputs1.txt','a') as f:
        for item in corpus:
            f.write(item)
            f.write('\n')

    