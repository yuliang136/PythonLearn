# -*- coding: utf-8 -*-
# coding: utf-8

import csv
import codecs
import GlobalVariable

import os;
import shutil;
import string;
import filecmp

import sys

splitRow = 10000

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
			sourceFileName = os.path.join(sourceDir,singleFileName)
			# print destFileName
			HandleDestFile(sourceFileName,destFileName)


def Logout(strMessage,strType):
	print strType + "  " + strMessage



# 处理目标文件夹里所有文件.
def HandleDestFile(sourceFile,destFile):
	# 判断同步目标里面的文件 在源文件里是否还存在
	# 如果在源文件里不存在 则删除目标文件.
	if not os.path.exists(sourceFile):
		os.remove(destFile)
		Logout(destFile, "Del")

# 处理单个文件的操作
# 不存在或者不相同是进行操作.
def HandleSourceFile(sourceFile, destFile):
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

# 把sourceDir同步到destDir里.
def syncFolder(sourceDir, destDir):
	# print sourceDir
	# print destDir


	IterateSourceDir(sourceDir, destDir)
	IterateDestDir(sourceDir, destDir)

def WriteSingleFile(textSplitFile, countnewFile, newFileData):
	# 拼接出新的文件名字.
	# 写入文件并保存.

	# 去掉后缀名字.
	strSingleName = textSplitFile.split('.')[0]
	strExt = textSplitFile.split('.')[1]

	newFileName = strSingleName + "_" + str(countnewFile)

	# 组合文件.
	newFileFullName = newFileName + "." + strExt

	newFileHandle = open(newFileFullName, 'w')

	# newFileHandle.writelines(newFileData)

	# print len(newFileData)

	for line in newFileData:
		# print line
		newFileHandle.write(line)

	# for lineNum in xrange(0,len(newFileData)):
	# 	newFileHandle.write(str(newFileData[lineNum]))

	# newFileHandle.write(newFileFullName)

	newFileHandle.close()


def splitFile(textSplitFile):
	print textSplitFile

	with codecs.open(textSplitFile, 'r', 'utf8') as f:
		GlobalVariable.TXTData = f.readlines()

	textRowNum = len(GlobalVariable.TXTData)

	
	newFileData = []
	countRow = 0
	countNewFile = 0


	for rowLine in xrange(0, textRowNum):
		# print GlobalVariable.TXTData[rowLine]

		if(rowLine == textRowNum - 1):
			# 已到达最后一个文件 进行收尾操作.
			WriteSingleFile(textSplitFile,countNewFile,newFileData)
			#reset Data.
			newFileData = []
			countRow = 0
			countNewFile = countNewFile + 1
		else:
			# 未收尾工作
			if(countRow < splitRow):
				newFileData.append(GlobalVariable.TXTData[rowLine])
				countRow = countRow + 1
			else:
				# =>splitRow. 进行写文件操作
				WriteSingleFile(textSplitFile,countNewFile,newFileData)
				#reset Data.
				newFileData = []
				countRow = 0
				countNewFile = countNewFile + 1



	# 基于list的list.



	print textRowNum

def TestForNum():
	for rowLine in xrange(0,3):
		# 0 1 2
		print rowLine


def CheckDir(checkFile):
	print checkFile

	files = os.listdir(checkFile)
	for singleFileName in files:

		FileName = os.path.join(checkFile,singleFileName)
		if os.path.isdir(FileName):
			if singleFileName == '.svn':
				print "Get .svn directory"
				continue
			print FileName

def main ():
	# syncFolder(sys.argv[1],sys.argv[2])

	reload(sys)
	sys.setdefaultencoding('utf8')

	# print sys.argv[1]

	CheckDir(sys.argv[1])




if __name__ == '__main__':
    main()




