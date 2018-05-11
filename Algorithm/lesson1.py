# 输入一个正整数为n，能顺序打印从1到n的全部正整数
def print_n(n):
	i = 1
	while i <= n:
		print(i)
		i = i+ 1

print_n(100)
# 递归方式实现
def print_n1(n):
	if n:
		print_n1(n - 1)
		print(n)

print_n1(100)