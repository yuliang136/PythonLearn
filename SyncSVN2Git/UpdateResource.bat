@set SourcePath=F:\SyncProjects\ShuiHu\hqsh180_20170228
@set DestPath=F:\SyncProjects\ShuiHu\gitWorks\ShuiHu

@rem rmdir /s/q %DestArtPath% 

@echo Í¬²½Ä¿Â¼

@python ./PythonScripts/SyncFolder.py %SourcePath% %DestPath%


Pause