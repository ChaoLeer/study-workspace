#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'处理表格数据对比'

__author__ = 'ChaoLee'

# 并未进行验证for循环嵌套的性能问题，先这么来吧，后面有需要再研究性能这块
# 目标数据----------即为源数据
# 比对数据----------即为源数据是否打上标识的依据
# 最后产出的是new开头的数据

import csv
from random import sample
import openpyxl
from openpyxl.styles import Font, colors

# 标记背景色
affix_color = '42b983'

# 比对数据文件名
ref_file_name = 'match.csv'
# 比对数据列名
ref_col_title = '昵称'

# 目标数据列名
target_col_title = '昵称'
# 目标数据文件名
target_file_name = 'data.xlsx'

# 结果数据文件(比对完成后生成的文件)，默认为new为前缀加上设置的目标数据文件名称
result_file_name = 'new_' + target_file_name

# 读取表格数据
wb = openpyxl.load_workbook(target_file_name)
ws = wb.worksheets[0]
sheet = wb.active
ant_row = []

# 如果是字符串则进行剪裁首位空格
def match_str(s):
	tmp_s = s
	if type(tmp_s) == str:
		tmp_s = tmp_s.strip()
	return tmp_s

# 读取比对文件，csv格式
with open(ref_file_name) as csvfile:
	reader = csv.DictReader(csvfile)
	# 读取比对文件每一行
	for row in reader:
		# 通过row[title]可以获取当前列的值
		ref_name = match_str(row[ref_col_title])
		# 标记循环之前的长度
		pre_length = len(ant_row)
		# 读取处理数据表格，先定为xlsx格式
		for row in sheet.rows:
			for cell in row:
				cell_value = match_str(cell.value)
				if cell.row == 1:
					pass
				elif cell_value == ref_name:
					ant_row.append(cell.row)
				else:
					pass
		# 判断是否命中
		after_length = len(ant_row)
		if after_length == pre_length:
			print('请注意【%s】未在数据表格中命中'%ref_name)

for irow, row in enumerate(ws.rows, start=1):
	if irow in (ant_row):
		for cell in row:
			cell.fill = openpyxl.styles.fills.GradientFill(stop=[affix_color, affix_color])
	else:
		pass

# 另存为新文件
wb.save(result_file_name)