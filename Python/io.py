#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'io'

__author__ = '作者'

f = open('./iofile.txt', 'r')
print(f.read())
# 必须关闭
f.close()

# 由于文件读写可能出现IOError,可以使用try...finally
try:
	f = open('./iofile.txt', 'r')
	print(f.read())
finally:
	if f:
		f.close()
# 这么写很麻烦，python引入了with语句自动调用close()
with open('./iofile.txt', 'a') as f:
	# print(f.read())
	f.write('nihao')

# 由于read()会一次性读取文件的全部内容，可能造成爆内存，文件小的时候可以使用
# read(size) 每次最多读取size个字节的内容
# readline()可以每次读取一行内容，推荐读取不确定大小的文件
# readlines() 一次读取所有内容病按行返回list， 推荐读取配置文件
print('**************************readlines() start***************')
with open('./iofile.txt', 'r') as f:
	for line in f.readlines():
		print(line.strip())
print('**************************readlines() end***************')


print('**************************读取gbk编码文件 start***************')
# with open('../../ioword.docx', 'r', encoding='gbk', errors='ignore') as f:
# 	print(f.read())
print('**************************读取gbk编码文件 end***************')

###############################################
# 操作文件和目录
###############################################
import os
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)
# 获取详细系统信息
# print(os.uname()) # 在windows不提供
# 环境变量
print(os.environ)
# 获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('JAVA_HOME'))

# 查看当前目录的绝对路径 .   ../   ../../ 可以省略最后一个/
p = os.path.abspath('.')
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的路径表示出来:
print(os.path.join(p, 'testdir'))
np = os.path.join(p, 'testdir')
# 创建目录
# os.mkdir(np)
# os.rmdir(np)
# os.rmdir('testdir')
# 把两个路径合成一个时，不要直接拼字符串，而要
# 通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：

# part-1/part-2
# 而Windows下会返回这样的字符串：

# part-1\part-2

# 同样os.path.split()去拆分
print(os.path.split(np)) # 拆分为两部分，第二个参数是后一部分，最后目录或文件名
# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext(np))

# 重命名
# os.rename('test.txt', 'test.py')
# 删除
# os.remove('test.py')

# shutil模块提供了copyfile()的函数


# 当前目录下的所有目录 isdir(x) isfile(x)
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']) 