%train ACF in (KAIST) dataset
%change file result 
%change opts.posGtDir to direct test files
%change opts.posImgDir to direct annotation files
%return models to use later

%explaine: to train new ACF models, we must feed data to opts. To save time, reuse parameter from the previous models like "Detector.mat" (it will be available when you clone this git) and change some para 

dtt = load('detector/models/Detector.mat’);
dtt = dtt.detector;
opts = dtt.opts;
opts.name = 'detector/models/';
opts.posGtDir = 'path to Gt direction';
opts.posImgDir = 'path to Img direction'

detector = acfTrain( opts )
opts = acfTrain()


