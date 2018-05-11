#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# 使用def语句声明函数
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。

# 写一个abs函数
def my_abs(num):
	if not isinstance(num, (int, float)):
		raise TypeError('bad operand type')
	if num < 0:
		return -num
	else:
		return num
print(my_abs(-99)) # 99
print(my_abs(9)) # 9
# print(my_abs('a')) # 错误参数自检

# 占位, pass, 占位，开发的时候可以让代码先跑起来
def nop_fun():
	pass
	
	
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
	
x,y = move(100, 100, 60, math.pi / 6)
print(x, y)

def quadratic(a, b, c):
	if not isinstance(a, (int, float)):
		raise TypeError('a 必须是数值')
	if not isinstance(b, (int, float)):
		raise TypeError('b 必须是数值')
	if not isinstance(c, (int, float)):
		raise TypeError('c 必须是数值')
	if a == 0:
		raise TypeError('a不能等于0')
	
	x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
	x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
	
	return x1, x2

print(quadratic(2, 3, 1))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
	
	
# 定义一个x n次方
def power(x, n = 2):
	res = x
	idx = 1
	if n == 0:
		return 1
	while idx < n:
		res = res * x
		idx = idx + 1
	return res

print(power(3, 0)) # 1
print(power(3)) # 9

def power2(x = 2, n = 2):
	res = 1
	while n > 0:
		n = n - 1
		res = res * x
	return res

print(power2(3, 0)) # 1
print(power2()) # 4

# 默认参数值
def enroll(name, sex, age = 8, city = 'xian'):
	print('name%s'%name)
	print('sex%s'%sex)
	print('age%s'%age)
	print('city%s'%city)

enroll('lc', 'man')
# 可以不按顺序
enroll('lc', 'man', city = 'zhouzhi')

def end_add(L = []):
	L.append('END')
	return L
print(end_add([1]))
print(end_add([1]))

print(end_add()) # ['END']
print(end_add()) # ['END', '#END']
# 修复后
def end_add1(L = None):
	if L == None:
		L = []
	L.append('END')
	return L
print(end_add1()) # ['END']
print(end_add1()) # ['END']

# 可变参数
def calc(numbers=[]):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc([1, 2, 3]))
print(calc())

#### *使得参数接受的是一个tuple
def calc1(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc1(1, 2, 3))

#### 如果需要传入一个list
params = [1, 2, 3]
print(calc1(*params))


#关键字参数
def person(name, age, **ke):
	ke['sex'] = 'woman'
	print('name:', name, 'age:', age, 'other:', ke)
person('lc', 18)
person('kebi', 18, city='xian')
person('kebi', 18, city='xian', weight=200)
extra = {'city': 'xian', 'weight': 200, 'sex': 'man'}
# print(**extra) #只能在function中使用
person('kebi', 18, **extra)
print(extra) # **在函数中操作，是不会影响外部的extra的

#
def person1(name, age, *, city = 1, sex = 2):
	print('name:', name, 'age:', age, 'city:', city, 'sex', sex)

person1('kebi', 18)

# 递归函数
# n! = 1 * 2 * 3 * 4...
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

print(fact(1))
print(fact(3))
print(fact(5))
# 尾递归做优化，可惜python解释器并没有对尾递归做优化，所以过多的递归还是会导致栈溢出
def fact1(n):
	return fact_iter(n, 1)
def fact_iter(num, pro):
	if num == 1:
		return pro
	return fact_iter(num - 1, pro * num)
print(fact1(5))

# 汉诺塔 64个
def tower(num):
	return math.pow(2, num) - 1
print(tower(64))
# 思路 不管在什么情况下都是把n-1个从a挪到b   然后a再挪到c,  最后再把n-1个从b挪到c
def move(n, a, b, c):
	if n == 1:
		print(a, '---->', c)
	else:
		move(n-1, a, c, b)
		move(1, a, b, c)
		move(n-1, b, a, c)
move(10, 'A', 'B', 'C')

###############################################
# 返回函数
###############################################
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
	def num():
		# def g():
		# 	return t
		# return g
		n = 0
		while True:
			n = n + 1
			yield n
	f = num()
	def create():
		return 	next(f)		
	return create
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

###############################################
# 匿名函数
###############################################
# lambda 返回表达式的结果
# f(x) = x * x
f = lambda x: x * x
print(f(2))

# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
is_odd = lambda n: n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)

###############################################
# 装饰器
###############################################
# 函数也是一个对象，可以赋值给变量，通过变量调用
def now():
	print('2018年')
f = now
f()

# 函数有一个__name__属性,可以拿到函数的名字
print(now.__name__)
print(f.__name__)
# 打印日志的装饰器
def log(func):
	def wrapper(*arg, **kw):
		print('call %s():'%func.__name__)
		return func(*arg, **kw)
	return wrapper

@log
def now():
	print('2015-3-25')
now()

# 带参数的装饰器
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
# 调用
@log('测试execute')
def now():
	print('2099-1-1')
now()
print(now.__name__)
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*arg, **kw):
		print('call %s():'%func.__name__)
		return func(*arg, **kw)
	return wrapper
# 带参数的decorator
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*arg, **kw):
			print('call %s():'%func.__name__)
			return func(*arg, **kw)
		return wrapper
	return decorator

@log('测试execute')
def now():
	print('2099-1-1')
now()
print(now.__name__)

# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools

def metric(fn):
	@functools.wraps(fn)
	def wrapper(*arg, **kw):
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print('%s executed start in %s ms'%(fn.__name__, t))
		start_time = time.time()
		result = fn(*arg, **kw)
		end_time = time.time()
		runtime = end_time - start_time
		print('运行总共耗费时间: %sms'%(runtime))
		t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print('%s executed end in %s ms'%(fn.__name__, t))
		return result
	return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
	print('测试成功！')


import functools
def logtest(func):
	# 判断是否是方法
	if callable(func):
		@functools.wraps(func)
		def wrapper(*arg, **kw):
			print('%s方法执行' % func.__name__)
			return func(*arg, **kw)
		return wrapper
	else:
		def decorator(fn):
			@functools.wraps(fn)
			def wrapper(*arg, **kw):
				print('参数是%s的%s方法执行'%(func, fn.__name__))	
				return fn(*arg, **kw)
			return wrapper
		return decorator


@logtest
def f1():
	print('无参数')
f1()

@logtest('你好，hello')
def f2():
	print('有参数')
f2()