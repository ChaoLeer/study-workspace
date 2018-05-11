#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
###############################################
# filter
# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素
###############################################
# list中删掉偶数，只保留奇数[1, 2, 4, 5, 6, 9, 10, 15]
d = [1, 2, 4, 5, 6, 9, 10, 15]
def is_odd(n):
	return n%2 != 0
print(list(filter(is_odd, d)))

# 把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 用filter求素数
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

# 首先，列出从2开始的所有自然数，构造一个序列：

# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

# 不断筛下去，就可以得到所有的素数。
def _iter(l):
	res = l[:]
	def f(s):
		return s % res[0] != 0 
	while True:
		try:
			print(res[0])
			res = list(filter(f, res))
		except Exception as e:
			return '错误'

d = list(range(100))
dl = d[2:]
# print(dl)
_iter(dl)

# 生成自然数
def _odd_iter():
	n = 1
	while True:
		n = n + 1
		yield n
# 过滤方法
def _not_divisible(n):
	return lambda x: x % n > 0
def primes():
	yield 2
	iter = _odd_iter()
	while True:
		n = next(iter)
		yield n
		iter = filter(_not_divisible, iter)
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


d = '123456'
print(d[::-1])


# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数
from functools import reduce
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
def is_palindrome(n):
	n1 = str(n)[::-1]
	def tran(k):
		return d[k]
	l = reduce(lambda x, y: x * 10 + y, map(tran, n1))
	return n == l
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
