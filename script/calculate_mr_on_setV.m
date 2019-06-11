%test MR on set00/V000 in KAIST dataset
%change file result of Yolo detect in `script/test_bbGT_copy.txt` as name/bbsNm
%change imgDir to direct test files
%change gtDir to direct annotation files
%return miss rate

pTest = {'name','script/', 'imgDir','/storageStudents/K2015/duyld/dungnm/dataset/KAIST/images/set00/V000','gtDir','/storageStudents/K2015/duyld/dungnm/dataset/KAIST/annotations/set00/V000','pLoad',[{'format',0,'ellipse',1,'squarify',[],'lbls',[],'ilbls',[],'hRng',[],'wRng',[],'aRng',[],'arRng',[],'oRng',[],'xRng',[],'yRng',[],'vRng',[]}]};
dfs={ 'name','REQ', 'imgDir','REQ', 'gtDir','REQ', 'pLoad',[], 'pModify',[], 'thr',.5,'mul',0, 'reapply',0, 'ref',10.^(-2:.25:0), 'lims',[3.1e-3 1e1 .05 1], 'show',0 };
[name,imgDir,gtDir,pLoad,pModify,thr,mul,reapply,ref,lims,show] = getPrmDflt(pTest,dfs,1);
bbsNm=[name 'test_bbGT_copy.txt'];
[gt,dt] = bbGt('loadAll',gtDir,bbsNm,pLoad);
[gt,dt] = bbGt('evalRes',gt,dt,thr,mul);
[fp,tp,score,miss] = bbGt('compRoc',gt,dt,1,ref);
miss=exp(mean(log(max(1e-10,1-miss)))); roc=[score fp tp];
miss

