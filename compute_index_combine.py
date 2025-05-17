from scipy.special import perm, comb
from itertools import combinations
"""
    compure the combinatorial index
"""
if __name__=='__main__':
    with open('corpus1.txt','r') as f:
        data = f.readlines()
    min_length=99999
    max_length=0
    for i in range(len(data)):
        if min_length>len(data[i].strip().split(' ')):
            min_length = len(data[i].strip().split(' '))
        if max_length<len(data[i].strip().split(' ')):
            max_length = len(data[i].strip().split(' '))
    # print(min_length)
    # print(max_length)
    # print(comb(31,2))
    for i in range(min_length,max_length):
        combins = [c for c in  combinations(range(31), 2)]
        print(i,":",combins)
    # for i in range(min_length,max_length):
    #     if i%2==0:
    #         k=int(i/2)
    #         print(comb(i, k))
    #         combins = [c for c in  combinations(range(i), k)]
    #         print(combins)
    #     else:
    #         k=int((i+1)/2)
    #         print(comb(i,k))
    #         combins = [c for c in combinations(range(i),k)]
    #         print(combins)
    #     print(i)
        # break
    