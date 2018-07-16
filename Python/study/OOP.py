#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象编程'

__author__ = 'ChaoLee'
###############################################
# 数据封装、继承和多态是面向对象的三大特点
###############################################
class Student(object):
	"""docstring for Student"""
	# __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
	def __init__(self, name, score):
		super(Student, self).__init__()
		self.name = name
		self.score = score
		self.__private = name
	def print_score(self):
		print('%s:%s分'%(self.name, self.score))
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >=60:
			return 'B'
		else:
			return 'C'
bob = Student('bob', 88)
lei = Student('lei', 98)
bob.print_score()
lei.print_score()
print(bob.get_grade())
print(lei.get_grade())

###############################################
# 访问限制 
###############################################
# 把属性的名称前加上两个下划线__
print(bob.name)
# print(bob.__private)
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print('访问私有变量', bob._Student__private)