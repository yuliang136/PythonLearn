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
# from progressbar import *

# total = 1000


# fuhao = '#'


# 把sourceDir同步到destDir里.
def Run():
	# print sourceDir
	# print destDir

	print "ProgressBarDemo"

	# print GlobalVariable.FuHao

	#一共有100个文件 需要处理100次
	handleTime = 60

	# 1~60
	# 处理60次的显示方法
	for x in xrange(1,handleTime + 1):
		# GlobalVariable.FuHao = GlobalVariable.FuHao + '#'
		sys.stdout.write(str(int((x/handleTime)*100))+'%' + "\r")
		sys.stdout.flush()
		time.sleep(0.1)
		

def main ():
	Run()

if __name__ == '__main__':
    main()




