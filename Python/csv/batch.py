#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'处理文件'

__author__ = '作者'

from random import sample
import openpyxl
from openpyxl.styles import Font, colors

def batchFormat(num):
    for i in range(num):
        fn = str(i)+'.xlsx'
        wb = openpyxl.load_workbook(fn)
        ws = wb.worksheets[0]
        for irow, row in enumerate(ws.rows, start=1):
            if irow == 1:
                # 表头加粗、黑体
                font = Font('黑体', bold=True)
            elif irow%2 == 0:
                # 偶数行红色，宋体
                font = Font('宋体', color=colors.RED)
            else:
                print('奇数行')
                # 奇数行浅蓝色，宋体
                # font = Font('宋体', color='00CCFF')
            for cell in row:
                cell.font = font
                # 偶数行添加背景填充色，从红到蓝渐变
                if irow%2 == 0:
                    # cell.fill = openpyxl.styles.fills.GradientFill(stop=['FF0000', '0000FF'])
                    cell.font = Font('黑体', color=colors.BLUE)
                    cell.fill = openpyxl.styles.fills.GradientFill(stop=['FF0000', 'FF0000'])
        # 另存为新文件
        wb.save('new'+fn)
batchFormat(5)