import os

PATH = '/storageStudents/K2015/duyld/dungnm/dataset/KAIST/annotations/set00/V000'
# max = 0
# a = [0,0,0,0,0,0,0,0,0,0,0]
# for file in os.listdir(PATH):
#     max_idle = 0
#     with open(os.path.join(PATH,file),'r') as f:
#         for line in f:
#             max_idle += 1
#         a[max_idle] += 1
# print(a)
#         if max_idle == 1:
#             max += 1
# print(max)

        # if max_idle ==10:
        #     with open('Log_10p.txt','a') as l:
        #         l.write(file+'\n')

aaa = os.listdir(PATH)
aaa.sort()
# print(aaa[0:5])
for idx,file_ in enumerate(aaa):

    with open(os.path.join(PATH,file_),'r') as f:
        n_ln = 0
        for line in f:
            n_ln += 1
            if n_ln>1:
                a = line.split(' ')
        #        line[0] = idx
                a[0] = idx+1
                with open('test_bbGT.txt','a') as fi:
                # print(a[0:6])   
                    fi.write('{id},{l},{t},{w},{h},{s}\n'.format(id=a[0],l=a[1],t=a[2],w=a[3],h=a[4],s=a[5]))
