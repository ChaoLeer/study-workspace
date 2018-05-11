#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#dict
d = {}
d['one'] = '帅'
print(d['one'])
print(d)

# 判断key是否存在, 存在True,不存在False
print('one' in d) # True
print('two' in d) # False

# 获取key
# 不存在则直接返回None
print(d.get('two')) # None

# key不存在时候，第二个参数可以设置默认值
print(d.get('two', '初始')) # 初始

print(d)
# 删除
print(d.pop('one'))
print(d)

#set
s1 = set([1, 2, 3, 4, 1, 2, 4])
print(s1) # {1,2,3,4}
s1.add(8) # {1, 2, 3, 4, 8}
print(s1.add(8)) # None
s1.remove(2)
print(s1) # {1, 3, 4, 8}

# 交集
ss1 = set([1, 2, 3])
ss2 = set([2, 3, 4, 5])
print(ss1 & ss2) # {2, 3}

# 并集
print(ss1 | ss2) # {1, 2, 3, 4, 5}
