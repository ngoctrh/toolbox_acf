%using this file to calculation MR with result 
%change file result of detect in `script/Yolo_predict.txt` as name/bbsNm
%change imgDir to direct test files
%change gtDir to direct annotation files
%return miss rate

pTest = {'name','script/', 'imgDir','/storageStudents/K2015/duyld/dungnm/dataset/KAIST/test/images_test','gtDir','/storageStudents/K2015/duyld/dungnm/dataset/KAIST/test/annotations_test','pLoad',[{'format',0,'ellipse',1,'squarify',[],'lbls',[],'ilbls',[],'hRng',[],'wRng',[],'aRng',[],'arRng',[],'oRng',[],'xRng',[],'yRng',[],'vRng',[]}]};
dfs={ 'name','REQ', 'imgDir','REQ', 'gtDir','REQ', 'pLoad',[], 'pModify',[], 'thr',.5,'mul',0, 'reapply',0, 'ref',10.^(-2:.25:0), 'lims',[3.1e-3 1e1 .05 1], 'show',0 };
[name,imgDir,gtDir,pLoad,pModify,thr,mul,reapply,ref,lims,show] = getPrmDflt(pTest,dfs,1);
bbsNm=[name 'Yolo_predict.txt'];
[gt,dt] = bbGt('loadAll',gtDir,bbsNm,pLoad);
[gt,dt] = bbGt('evalRes',gt,dt,thr,mul);
[fp,tp,score,miss] = bbGt('compRoc',gt,dt,1,ref);
miss=exp(mean(log(max(1e-10,1-miss)))); roc=[score fp tp];
miss

