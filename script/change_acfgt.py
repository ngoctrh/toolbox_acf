import os
import sys

path_acf = 'bbs'
des = 'result_gt_acf'
for files in os.listdir(path_acf):
    #print(files)
    index = 0
    #print(os.path.join(path_acf,files))
    with open(os.path.join(path_acf,files),'r') as f:
        for line in f:
            p = line.split(',')[:4]
    a= []
    for i in p:
        i = float(i)
        a.append(i)
    a.insert(0,index)
    a[3] = round(a[1]+a[3],3)
    a[4] = round(a[2]+a[4],3)
    name = files.split('.')[0]

    with open('{}/{}_new.txt'.format(des,name),'w+') as fi:
        fi.write('{id},{l},{t},{r},{b}'.format(id=a[0],l=a[1],t=a[2],r=a[3],b=a[4]))

