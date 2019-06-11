%using this file to calculation MR with result of ACF
%change name of result predict by replace "Dets_TestK_day.txt", it will store at "name"
%change imgDir to direct test files 
%change gtDir to direct annotation files
%change other model of KAIST by replace "DetectorKaist.mat" which store at "name"
%return miss rate

pTest = {'name','detector/models/', 'imgDir','/storageStudents/K2015/duyld/dungnm/dataset/KAIST/train/images_train','gtDir','/storageStudents/K2015/duyld/dungnm/dataset/KAIST/train/annotations_train','pLoad',[{'format',0,'ellipse',1,'squarify',[],'lbls',[],'ilbls',[],'hRng',[],'wRng',[],'aRng',[],'arRng',[],'oRng',[],'xRng',[],'yRng',[],'vRng',[]}],'pModify',[{'cascThr',-70,'cascCal',0.075}]};

dfs={ 'name','REQ', 'imgDir','REQ', 'gtDir','REQ', 'pLoad',[], 'pModify',[], 'thr',.5,'mul',0, 'reapply',0, 'ref',10.^(-2:.25:0), 'lims',[3.1e-3 1e1 .05 1], 'show',0 };
[name,imgDir,gtDir,pLoad,pModify,thr,mul,reapply,ref,lims,show] = getPrmDflt(pTest,dfs,1);
bbsNm=[name 'Dets_Train_Thr70_Cal075.txt'];
if(reapply && exist(bbsNm,'file')), delete(bbsNm); end
if(reapply || ~exist(bbsNm,'file'))
  detector = load([name 'DetectorKaist.mat']);
  detector = detector.detector;
  if(~isempty(pModify)), detector=acfModify(detector,pModify); end
  imgNms = bbGt('getFiles',{imgDir});
  acfDetect( imgNms, detector, bbsNm );
end
[gt,dt] = bbGt('loadAll',gtDir,bbsNm,pLoad);
[gt,dt] = bbGt('evalRes',gt,dt,thr,mul);
[fp,tp,score,miss] = bbGt('compRoc',gt,dt,1,ref);
miss=exp(mean(log(max(1e-10,1-miss)))); roc=[score fp tp];
miss

