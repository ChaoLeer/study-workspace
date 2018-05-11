#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# 高级特性

# 构造一个1,3,5,7,...,99的列表
L = []
n = 99
while n > 0:
	L.append(n)
	n = n - 2

print(L)

# 取一个list 或者tuple的部分元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L)
# 取前三个
n = 0
resL = []
while n < 3:
	resL.append(L[n])
	n = n + 1
print(resL)

n1 = 0
resL1 = []
for i in range(3):
	resL1.append(L[i])
print(resL1)

###############################################
# 切片
###############################################

# 索引 0 - 索引3，但是不包含3
print(L[0:3])
# 如果索引开始是0，可省略
print(L[:3])

# 倒数第一个是-1
print(L[-1:])
print(L[-2:-1])

L1 = list(range(10))
print(L1)
# 复制出一个list
L2 = L1[:]
print(L2)
str1 = 'ABCDEFG'
# :3 0-3 从0开始取，到3，但是不包含3
print(str1[:3]) # ABC
# ::2每隔2个取
print(str1[::2]) # ACEG
# 前6个，每隔2个取
print(str1[:6:2]) # ACE
print(str1[:6:3]) #AD

# tuple 与 list一样, 注意返回的仍是一个tuple
L3 = (1, 2, 3, 4)
print(L3[::2]) # (1, 3)

# 写一个trim()方法
def my_trim(str1):
	l = 0
	if str1 == '':
		return str1
	while l < len(str1):
		if str1[:1] == ' ':
			str1 = str1[1:len(str1)]
		if str1[-1:] == ' ':
			str1 = str1[0:-1]
		if (str1[:1] != ' ') & (str1[-1:] != ' '):
			return str1

# print(' hello, nihoa ', '首尾有空格')
# print(my_trim(' hello, nihoa '), '首尾有空格')
# print(' hello', '首有空格')
# print(my_trim(' hello'), '首有空格')
# 测试:
if my_trim('hello  ') != 'hello':
    print('测试hello  失败!')
elif my_trim('  hello') != 'hello':
    print('测试  hello失败!')
elif my_trim('  hello  ') != 'hello':
    print('测试  hello  失败!')
elif my_trim('  hello  world  ') != 'hello  world':
    print('测试  hello  world  失败!')
elif my_trim('') != '':
    print('测试失败!')
elif my_trim('    ') != '':
    print('测试    失败!')
else:
    print('测试成功!')
###############################################
# 迭代
###############################################
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
# 默认情况下dict迭代的Key
# dict 迭代vlaue用d.values()
for v in d.values():
	print(v)
# dict 迭代key,value 用d.items()
for k,v in d.items():
	print(k, v)
	
# str 字符串迭代
for s in 'ABCC':
	print(s)
	
# 判断是否是可迭代，需要引入from collections import Iterable
# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance(123, Iterable))
# print(isinstance([1,2,3], Iterable))

#使用迭代查找一个list中最小和最大值，并返回一个tuple
def my_maxmin(L):
	if len(L) == 0:
		return None, None
	min = L[0]
	max = L[0]
	for idx in range(len(L)):
		if min > L[idx]:
			min = L[idx]
		if max < L[idx]:
			max = L[idx]
	print(min, max)
	return min, max
my_maxmin([1, 3, 6, 4, 5, 2])
# 测试
if my_maxmin([]) != (None, None):
    print('测试失败!')
elif my_maxmin([7]) != (7, 7):
    print('测试失败!')
elif my_maxmin([7, 1]) != (1, 7):
    print('测试失败!')
elif my_maxmin([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

		
###############################################
# 列表生成式
###############################################
# 生成[1x1, 2x2, 3x3, ..., 10x10]
L4 = []
n = 1
while n <= 10:
	L4.append(n * n)
	n = n + 1
print(L4)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])
# 生成全排列
print([x + y for x in 'ABCD' for y in 'XYZW'])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([(k + '=' + v) for k, v in d.items()])

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 如果list 中存在非str类型，就会报错
def my_lower(L):
	tmp = []
	for s in L:
		m = isinstance(s, str)
		print(s)
		if isinstance(s, str):
			tmp.append(s.lower())
		else:
			tmp.append(s)
	return tmp
print(my_lower(L))
print([s.lower() for s in L if isinstance(s, str)])
# 测试:
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
### int，float，bool，complex，str(字符串)，list，dict(字典)，set，tuple




###############################################
# 生成器
###############################################

# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		# tmp = b
		# b = b + a
		# a = tmp
		a,b = b, a+b
		n = n + 1
	print('done')

fib(6)

# generator yield
def fib_yield(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		# tmp = b
		# b = b + a
		# a = tmp
		a,b = b, a+b
		n = n + 1
	print('done')
	return 'well done'

f = fib_yield(6)
print(f)

print([x for x in f])

#generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 2
	print('step 3')
	yield 3
p = odd()
next(p)
next(p)
# next(p)
# next(p)

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib_yield(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

# 杨辉三角定义如下：

#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
	L = [1]
	while True:
		yield L
		tmp = L[:]
		L = []
		for i in range(len(tmp)):
			if i == 0:
				L.append(1)
			else:
				L.append(tmp[i] + tmp[i-1])
		L.append(1)	
nm = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    nm = nm + 1
    if nm == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')