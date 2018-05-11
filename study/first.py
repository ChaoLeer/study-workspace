#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
name = input('嘿，输入你的名字')
print(100 + 200, name, 'love u')
code = 9
if code >= 5:
	print(code)
else:
	print(code)
	
	
print('''nihao,
woshi,
nibaba''')
		
print('''nihao,
... woshi,
... nibaba''')
	
print(True)
print(False)
print(3>2)
print(3<2)

print(True and False)
print(True and 3 < 2)
print(False or True)

print(not True)
print(not 3>2)

print(None)
print(None == '')
print(None == 0)

test = 'nihao'
test = 2
print(test)

testA = 'ceshi'
testB = testA
testB = 'ceshi1'
print(testA)

testAA = 'ceshi'
testBB = testAA
testAA = 'ceshiAA'
print(testBB)


print(100 / 3)
print(100 // 3)
print(100 % 3)

f=45.789
print(f)

s1 = 'hello, "button"'
print(s1)


print(ord('中'))
print(chr(20013))

print('中文显示')

testFormatString = '测试, 字符串%s, 整数%d, 浮点数%f.....' % ('nihao', 200, 200.2222)
print(testFormatString)
testFS = '测试格式化中有%%, %s %%' % 200
print(testFS)
testFS1 = '可以在任何时候用%%s, 字符串%s, 数字%s, boolean-%s' % ('nihao', 200, True)
print(testFS1)
testFormatFun = '测试format方法{0}, {1}, {2}'.format('第一个', 20, 200.2222)
print(testFormatFun)
sum = 0
for x in range(101):
	sum = sum + x
print(sum)
m = list(range(5))
print(m)

#计算100以内的奇数和
n = 99
jishu = 0
while n > 0:
	jishu = jishu + n
	n = n - 2
print(jishu)

#跳出循环break
x = 1
while x > 0:
	if x == 10:
		break
	else:
		x = x + 1
print(x)
#直接进行下次循环
y = 1
while y > 0:
	y = y + 1
	if y < 10:
		print('跳过%s'%y)
		continue
	print('正常打印%s'%y)
	if y > 20:
		break

t = 1
while t > 0:
	if t > 100:
		break
	if t%2 == 0:
		t = t + 1
		continue
	else:
		t = t + 1
		print(t)





















