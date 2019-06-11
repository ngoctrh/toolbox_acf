import os

PATH ='/storageStudents/K2015/duyld/dungnm/source/Yolo/darknet_Kaist/mAP/predicted'
#var = os.listdir(PATH)
#var.sort()
#for idx,file_ in enumerate(var):
#    with open(os.path.join(PATH,file_),'r') as f:
#        for line in f:
#            lb,mAP,l,t,r,b = line.split(' ')
#            w = int(r) - int(l)
#            h = int(b) - int(t)
#            # print(idx,l,t,w,h,mAP)
#            with open('Yolo_predict.txt','a') as fi:
#                fi.write('{id},{l},{t},{w},{h},{s}\n'.format(id=idx,l=l,t=t,w=w,h=h,s=mAP))
    # print(file_)

var = os.listdir(PATH)
var.sort()
day = 0
for idx,file_ in enumerate(var[29178:]):
    with open(os.path.join(PATH,file_),'r') as f:
        for line in f:
            lb,mAP,l,t,r,b = line.split(' ')
            w = int(r) - int(l)
            h = int(b) - int(t)
            # print(idx,l,t,w,h,mAP)
            with open('Yolo_predict_night.txt','a') as fi:
                fi.write('{id},{l},{t},{w},{h},{s}\n'.format(id=idx,l=l,t=t,w=w,h=h,s=mAP))
    # print(file_)

