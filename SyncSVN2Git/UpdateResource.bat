@set SourcePath=F:\SyncProjects\ShuiHu\hqsh180_20170228
@set DestPath=F:\SyncProjects\ShuiHu\gitWorks\ShuiHu

@rem rmdir /s/q %DestArtPath% 

@echo ͬ��Ŀ¼

@python ./PythonScripts/SyncFolder.py %SourcePath% %DestPath%


Pause