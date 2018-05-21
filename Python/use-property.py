#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用property装饰器'

__author__ = 'ChaoLee'

class Studernt(object):
	"""docstring for Studernt"""
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value > 900:
			raise ValueError('score must between 0 - 900')
		self._score = value

s = Studernt()
s.score = 800
s.score = 900
# s.score = 901

###############################################
# 只读属性---定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
###############################################
class Animal(object):
	@property
	def birth(self):
		self._birth = 2018 - self._age
		return self._birth
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self, value):
		if not isinstance(value, int):
			raise ValueError('age must be an integer')
		if value > 200:
			raise ValueError('age must between 0 - 200')
		self._age = value

a = Animal()
a.age = 18	
print(a.birth, '年出生')

# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
	@property
	def width(self):
		return self._width
	@property
	def height(self):
		return self._height

	@width.setter
	def width(self, width):
		self._width = width
	@height.setter
	def height(self, height):
		self._height = height

	@property
	def resolution(self):
		self._resolution = self._width * self._height
		return self._resolution

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')	
	
	
###############################################
# __getattr__
###############################################
# 在没有找到属性的情况下，才调用__getattr__
# 已有的属性，比如name，不会在__getattr__中查找。
class Studernt(object):
	"""docstring for Studernt"""
	# def __init__(self, arg):
	# 	super(Studernt, self).__init__()
	# 	self.arg = arg
	def __getattr__(self, attr):
		if attr == 'age':
			return lambda: 25
		raise AttributeError('Student object has no attribute %s'%attr)
student = Studernt()
a = student.age()
print(a)
# student.mmm()
###############################################
# 处理REST API
###############################################
class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s'%(self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__

c = Chain()
print(c.status.user.timeline.list)
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名
print(callable(c))
print(c.users('michael').repos)