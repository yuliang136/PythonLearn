@rem @set SourcePath=F:\SyncProjects\ShuiHu\hqsh180_20170228

@rem @set SourcePath=F:\SyncProjects\ShuiHu\tanyu180_20170224
@rem @set DestPath=F:\SyncProjects\ShuiHu\gitWorks\ShuiHu

@rem rmdir /s/q %DestArtPath% 

@rem @echo ͬ��Ŀ¼

@rem @python ./PythonScripts/SyncFolder.py %SourcePath% %DestPath%

@rem HandleTrunk
@set svnShuiHu=F:\SyncProjects\ShuiHu\trunk
@set gitShuiHu=F:\SyncProjects\ShuiHu\gitWorks\ShuiHu\ShuiHu_trunk
@set branchName=trunk
@set compName=CheckSVN2Git_ShuiHu_trunk
@python ./PythonScripts/SyncSVN2Git.py %svnShuiHu% %gitShuiHu% %branchName% %compName%


@set svnShuiHu=F:\SyncProjects\ShuiHu\tanyu180_20170224
@set gitShuiHu=F:\SyncProjects\ShuiHu\gitWorks\ShuiHu\ShuiHu_tanyu180
@set branchName=tanyu180
@set compName=CheckSVN2Git_ShuiHu_tanyu180
@python ./PythonScripts/SyncSVN2Git.py %svnShuiHu% %gitShuiHu% %branchName% %compName%


@set svnShuiHu=F:\SyncProjects\ShuiHu\hqsh180_20170228
@set gitShuiHu=F:\SyncProjects\ShuiHu\gitWorks\ShuiHu\ShuiHu_hqsh180
@set branchName=HQSU180
@set compName=CheckSVN2Git_ShuiHu_hqsh180
@python ./PythonScripts/SyncSVN2Git.py %svnShuiHu% %gitShuiHu% %branchName% %compName%


Pause