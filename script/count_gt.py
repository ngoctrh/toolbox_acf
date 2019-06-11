import os
# PATH = '/storageStudents/K2015/duyld/dungnm/dataset/KAIST/annotations/set00/V000'
# for file in os.listdir(PATH):
#     i = 0
#     with open(os.path.join(PATH,file),'r') as f:
#         for line in f:
#             i += 1
#             if i > 1:
#                 wrt = line.split()
#                 a = str(file[2:6])+' '+wrt[1]+' '+wrt[2]+' '+wrt[3]+' '+wrt[4] 
#                 print(a)
#                 with open('GT_set00_V000','a') as l:
#                     l.write(a+'\n')

# import pandas as pd
# ROIS_KAIST_CSV = '~/Perdestrian-/mydata/rois_trainKaist_thr70_1.csv'
# bbs = pd.read_csv(ROIS_KAIST_CSV)
# df = pd.DataFrame(bbs)
# num = df.groupby(['id']).size()
# print(len(num))
# s = -1
# for i in num:
#     s += 1
#     print(i)

#     with open('num_rois.txt','a') as l:
#         l.write(str(s) + ','+str(i)+'\n')




# PATH = '/storageStudents/K2015/duyld/dungnm/dataset/KAIST/test/annotations_test'

# # def count_person(path):
# max = 0 #max n person
# a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #know as max = 10
#count anno
# for file in os.listdir(PATH):
#     max_idle = -1
#     with open(os.path.join(PATH,file),'r') as f:
        
#         for line in f:
#             max_idle += 1
#         a[max_idle] += 1
        # print(a)
        # if max_idle == 1:
        #     max += 1
        # print(max_idle)
        #save max num of people
        # if max_idle == 14:
        # #     print(file)
        #     with open('Log_14per_test.txt','a') as l:
        #         l.write(file+'\n')
#test [22130, 10008, 5878, 3076, 1472, 844, 636, 295, 187, 226, 145, 136, 34, 48, 25, 0, 0, 0] 
#train [28026, 8565, 5759, 3151, 2059, 1229, 634, 559, 159, 43, 0, 0, 0, 0, 0, 0, 0, 0]





# aaa = os.listdir(PATH)
# aaa.sort()
# # print(aaa[0:5])
# for idx,file_ in enumerate(aaa):

#     with open(os.path.join(PATH,file_),'r') as f:
#         n_ln = 0
#         for line in f:
#             n_ln += 1
#             if n_ln>1:
#                 a = line.split(' ')
#         #        line[0] = idx
#                 a[0] = idx+1
#                 with open('test_bbGT.txt','a') as fi:
#                 # print(a[0:6])   
#                     fi.write('{id},{l},{t},{w},{h},{s}\n'.format(id=a[0],l=a[1],t=a[2],w=a[3],h=a[4],s=a[5]))
