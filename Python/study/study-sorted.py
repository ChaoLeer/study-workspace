#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
###############################################
# 排序算法
###############################################
# sorted
print(sorted([36, 5, -12, 9, -21]))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# 例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 字符串排序的例子
print(sorted(['bob', 'about', 'Zoo', 'Credit'])) # ['Credit', 'Zoo', 'about', 'bob']
# 默认情况下，对字符串排序，是按照ASCII的大小比较的
# 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法
# 不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。
# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
# def k(s):
# 	return s.lower()
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
def fn(itm):
	return itm[0].lower()
print(sorted(L, key=fn))
# 按成绩从高到低排序
def fnh(itm):
	return itm[1]
print(sorted(L, key=fnh, reverse=True))