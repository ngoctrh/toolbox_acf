import os
import sys

#copy set0_ from src_img to des_dir

SRC_IMG = './annotations_test'
#PATH_TRAIN = '../darknet/build/darknet/x64/data/test.txt'
DES_DIR = './annotations_test_day'
total = 0
for filename in os.listdir(SRC_IMG):
    if filename[:5] == 'set06' or filename[:5] == 'set07' or filename[:5] == 'set08':
        
        #total+=1
        os.system('cp {} {}'.format(SRC_IMG+'/'+filename,DES_DIR))
        #break
#print(total)
        # exit()

#29178 file test_day
#15962 file test_night
#45140 total 

#print('Test:',len(data))
#with open(PATH_TRAIN,'w') as f:
 #   f.writelines(data)
    # f.write('aaaaa')
