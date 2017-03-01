@set DIR=F:\SyncProjects\ShuiHu\hqsh180_20170228



@echo 开始处理....


@python ./PythonScripts/CheckHideDir.py %DIR%


@rem xcopy %SourceDesignPath%\*.* %DestDesignPath%\ /s /e 

Pause