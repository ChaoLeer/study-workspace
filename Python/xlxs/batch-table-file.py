#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'处理表格数据对比'

__author__ = 'ChaoLee'

# 并未进行验证for循环嵌套的性能问题，先这么来吧，后面有需要再研究性能这块

import csv
from random import sample
import openpyxl
from openpyxl.styles import Font, colors

csv_col_title = '昵称'
xlsx_col_title = '昵称'
xlsx_file = 'data'
# 读取表格数据
with open('match.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		# 通过row[title]可以获取当前列的值
		# print(row[csv_col_title], row['编号'])
		csv_name = row[csv_col_title]
		print(csv_name, '这个是指定列下的数据')
		# 读取处理数据表格，先定为xlsx格式

		fn = xlsx_file+'.xlsx'
		wb = openpyxl.load_workbook(fn)
		ws = wb.worksheets[0]
		sheet = wb.active
		ant_row = 0
		for row in sheet.rows:
			for cell in row:
				print(cell, cell.value, cell.row)
				if cell.value == csv_name:
					ant_row = cell.row
				else:
					pass
		for irow, row in enumerate(ws.rows, start=1):
			print(irow)
			if irow == 1:
				pass
			elif ant_row + 1 == irow:
				for cell in row:
					cell.fill = openpyxl.styles.fills.GradientFill(stop=['FF0000', 'FF0000'])
			else:
				pass
		# 另存为新文件
		wb.save('new'+fn)