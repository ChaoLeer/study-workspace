from random import sample
import openpyxl
from openpyxl.styles import Font, colors

def generateXlsx(num):
    for i in range(num):
        wb = openpyxl.Workbook()
        ws = wb.worksheets[0]
        # 添加表头
        ws.append(['字段'+str(_) for _ in range(1,6)])
        # 添加随机数据
        for _ in range(10):
            ws.append(sample(range(10000), 5))
        wb.save(str(i)+'.xlsx')
generateXlsx(5)