# -*- coding: utf-8 -*-
# coding: utf-8

from __future__ import division

import csv
import codecs
import GlobalVariable
import sys
import os;
import shutil;
import string;
import filecmp
import time

ISOTIMEFORMAT='%Y-%m-%d %X'


def IterateSourceDir(sourceDir, destDir):
	# 遍历Source目录下所有文件.
	# 替换Dest外层目录进行查找.
	# 没有文件时进行复制.
	# 文件不同时 进行复制覆盖.
	files = os.listdir(sourceDir)
	for singleFileName in files:
		# print singleFileName
		# dest_d = os.path.join(destDir,singleFileName)
		# print dest_d

		# 添加过滤文件夹. .git .svn
		if singleFileName == '.git':
			# print "Get .git directory"
			continue

		if singleFileName == '.svn':
			# print "Get .svn directory"
			continue

		sourceFileName = os.path.join(sourceDir,singleFileName);
		if os.path.isdir(sourceFileName):
			# 组合出目录再进行操作
			# print sourceFileName
			# pass
			sourceSubDir = sourceFileName
			destSubDir = os.path.join(destDir,singleFileName);

			# 判断destSubDir如果为空时,创建目录.
			if not os.path.exists(destSubDir):
				os.makedirs(destSubDir)
				Logout(destSubDir, "Add")

			IterateSourceDir(sourceSubDir,destSubDir)

		else:
			# 取得后缀名字 进行判断是否是csv.
			# 获得源文件.
			# print sourceFileName
			# 获得目标文件.
			destFileName = os.path.join(destDir,singleFileName)
			# print destFileName

			HandleSourceFile(sourceFileName,destFileName)

# 遍历Dest目录进行处理.
def IterateDestDir(sourceDir, destDir):
	files = os.listdir(destDir)
	for singleFileName in files:
		# print singleFileName
		# dest_d = os.path.join(destDir,singleFileName)
		# print dest_d

		# 添加过滤文件夹. .git .svn
		if singleFileName == '.git':
			# print "Get .git directory"
			continue

		if singleFileName == '.svn':
			# print "Get .svn directory"
			continue


		destFileName = os.path.join(destDir,singleFileName)
		if os.path.isdir(destFileName):
			# 组合出目录再进行操作
			# print sourceFileName			
			destSubDir = destFileName
			sourceSubDir = os.path.join(sourceDir,singleFileName)

			# 这里destSubDir有可能为空.
			# 判断destSubDir如果为空时,创建目录.
			# 这里可能是有目录整体都没有 那么这个目录下所有文件也没有.
			# 这里在同一级下目录和文件在一个层次.
			# 没有影响 因为是广度遍历 当目录被删除时 下面的文件不用再处理.

			if not os.path.exists(sourceSubDir):
				# 递归删除目录.
				# shutil.rmtree()
				shutil.rmtree(destSubDir)
				Logout(destSubDir, "Del")
			else:
				IterateDestDir(sourceSubDir,destSubDir)

		else:
			# 取得后缀名字 进行判断是否是csv.
			# 获得源文件.
			# print sourceFileName
			# 获得目标文件.

			# 这里过滤git里的两个文件.
			if(singleFileName == '.gitignore'):
				continue
			if(singleFileName == 'README.md'):
				continue

			sourceFileName = os.path.join(sourceDir,singleFileName)
			# print destFileName
			HandleDestFile(sourceFileName,destFileName)


def Logout(strMessage,strType):
	print strType + "  " + strMessage

def Progress(curNum, TotalNum):
	# GlobalVariable.FuHao = GlobalVariable.FuHao + '#'
	sys.stdout.write(str(int((curNum / TotalNum)*100))+'%' + "\r")
	sys.stdout.flush()

# 更新进度条.
def UpdateHandleTime():
	# 先使用 后计算
	Progress(GlobalVariable.CurNum, GlobalVariable.TotalFileNum)
	GlobalVariable.CurNum = GlobalVariable.CurNum + 1


# 处理目标文件夹里所有文件.
def HandleDestFile(sourceFile,destFile):

	# 处理进度调用
	UpdateHandleTime()

	# 判断同步目标里面的文件 在源文件里是否还存在
	# 如果在源文件里不存在 则删除目标文件.
	if not os.path.exists(sourceFile):
		os.remove(destFile)
		Logout(destFile, "Del")

# 处理单个文件的操作
# 不存在或者不相同是进行操作.
def HandleSourceFile(sourceFile, destFile):

	# 处理进度调用
	UpdateHandleTime()

	# 判断destFile是否存在 如果不存在则建立文件.
	if not os.path.exists(destFile):
		shutil.copy(sourceFile, destFile)
		# 输出更新结果.
		Logout(destFile,"Add")

	else:
		# 判断两个文件是否一致，如果不一致 则用sourceFile覆盖destFile.
		if not filecmp.cmp(sourceFile, destFile):
			shutil.copy(sourceFile, destFile)
			Logout(destFile,"Update")


def CalFileTotaolNum(handleDir):	
	# 统计sourceDir目录.
	files = os.listdir(handleDir)
	for singleFileName in files:

		# 添加过滤文件夹. .git .svn
		if singleFileName == '.git':
			# print "Get .git directory"
			continue

		if singleFileName == '.svn':
			# print "Get .svn directory"
			continue


		fullFileName = os.path.join(handleDir,singleFileName)
		if os.path.isdir(fullFileName):
			# 组合出目录再进行操作
			# print sourceFileName			
			CalFileTotaolNum(fullFileName)

		else:

			# 这里过滤git里的两个文件.
			if(singleFileName == '.gitignore'):
				continue
			if(singleFileName == 'README.md'):
				continue

			# 总数进行计数.
			GlobalVariable.TotalFileNum = GlobalVariable.TotalFileNum + 1;
			# print GlobalVariable.TotalFileNum

# 把sourceDir同步到destDir里.
def syncFolder(sourceDir, destDir):
	# print sourceDir
	# print destDir

	print "Calculate Total File Number...."
	
	CalFileTotaolNum(sourceDir)
	CalFileTotaolNum(destDir)

	print "Total File Number = " + str(GlobalVariable.TotalFileNum)



	IterateSourceDir(sourceDir, destDir)
	IterateDestDir(sourceDir, destDir)

def HandleSvnPath(svnPath):
	print "HandleSvnPath " + svnPath

	# 生成Python解释类.
	strPythonEXE = 'svn revert -R ' + svnPath
	print strPythonEXE
	os.system(strPythonEXE)

	strPythonEXE = 'svn cleanup --remove-unversioned --remove-ignored ' + svnPath
	print strPythonEXE
	os.system(strPythonEXE)

	strPythonEXE = 'svn update ' + svnPath
	print strPythonEXE
	os.system(strPythonEXE)

def HandleGitPath(gitPath, branchName):
	print "HandleGitPath " + gitPath

	# print os.getcwd()
	os.chdir(gitPath)
	# print os.getcwd()

	strPythonEXE = 'git reset --hard HEAD'
	os.system(strPythonEXE)

	strPythonEXE = 'git clean -df'
	os.system(strPythonEXE)

	strPythonEXE = 'git checkout ' + branchName
	os.system(strPythonEXE)


	#切换到git目录.

def GitCommit():
	print "GitCommit"

	strPythonEXE = 'git add .'
	os.system(strPythonEXE)

	commitComment = 'update from svn at ' + time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
	strPythonEXE = 'git commit -m ' + '\"' + commitComment + '\"'
	os.system(strPythonEXE)

	strPythonEXE = 'git push'
	os.system(strPythonEXE)

def OpenCompareTool(compareName):
	print "OpenCompareTool"

	strPythonEXE = 'BComp ' + compareName
	os.system(strPythonEXE)

def main ():

	# 显示svn目录
	# 显示git目录
	# 显示git分支
	GlobalVariable.SvnPath = sys.argv[1]
	GlobalVariable.GitPath = sys.argv[2]
	GlobalVariable.GitBranchName = sys.argv[3]
	GlobalVariable.CompareName = sys.argv[4]

	print "SyncSVN2GitTool"
	print GlobalVariable.SvnPath
	print GlobalVariable.GitPath
	print GlobalVariable.GitBranchName
	print GlobalVariable.CompareName

	# 处理svn目录 reset后update	
	HandleSvnPath(GlobalVariable.SvnPath)

	# 处理git目录 reset后切换分支
	HandleGitPath(GlobalVariable.GitPath, GlobalVariable.GitBranchName)
	
	# 进行 svn 2 git 同步
	syncFolder(GlobalVariable.SvnPath, GlobalVariable.GitPath)

	# git进行自动提交和push
	GitCommit()

	# 打开比较工具
	OpenCompareTool(GlobalVariable.CompareName)

if __name__ == '__main__':
    main()




