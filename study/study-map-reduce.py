#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

###############################################
# map
# map(fn, [])
###############################################
#  第一个函数，第二个参数Iterable 返回一个Itarator
# 函数f(x) = x^2
def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6])
print(r)
# 通过list()可以转成list
print(list(r)) # [1, 4, 9, 16, 25, 36]
 
# 将所有元素转为str
print(list(map(str, [1, 2, 3, 4, 5, 6]))) # ['1', '2', '3', '4', '5', '6']


###############################################
# reduce 
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
###############################################
# reduce()接收两个参数，reduce把结果继续和序列的下一个元素做累积计算


def add(x, y):
	return x + y

l = reduce(add, [1, 3, 5, 7, 9])
print(l)

# 使用sum()求和
print(sum([1, 3, 5, 7, 9]))

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def tran(x, y):
	return x * 10 + y
print(reduce(tran, [1, 3, 5, 7, 9]))

# 配合map()写出把str转换为int的函数
def char2num(k):
	d = {
		'0': 0,
		'1': 1,
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
	}
	return d[k]
print(reduce(tran, map(char2num, '13579'))) # 13579

# 整理上面的代码，组织成一个str2int(s)的方法
def str2int(s):
	_dict = {
		'0': 0,
		'1': 1,
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
	}
	def _tran(x, y):
		return x * 10 + y
	def _char2num(k):
		return _dict[k]
	return reduce(_tran, map(_char2num, s))
print(str2int('13579'))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def format_username(nameList):
	def _tran(s):
		s = s.lower()
		return s[:1].upper() + s[1:]
	return list(map(_tran, nameList))
print(format_username(['Adam', 'Lisa', 'Bart']))

def normalize(s):
	s = s.lower()
	return s[:1].upper() + s[1:]
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# import math
def str2float(s):
	# return float(s)
	_dict = {
		'0': 0,
		'1': 1,
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
	}
	def cut(s):
		idx = s.find('.')
		if idx == -1:
			i = int(s)
			c = 0
		else:
			i = int(s[:idx])
			c = s[(idx + 1):]
		return [i, c]
	# def _trans(x, y):
	# 	return x / 10 + y
	def f(k):
		return _dict[k]
	i, c = cut(s)
	mapc = list(map(f, c))
	mapc.reverse()
	# tmpc = reduce(_trans, mapc)
	tmpc = reduce(lambda x, y: x / 10 + y, mapc)
	return i + (tmpc / 10)
print(str2float('123.456'))
# lambda x,y: x/10 + y
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')