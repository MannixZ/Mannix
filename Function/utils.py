#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
import xlrd

# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()  # 初始化字体函数
    style.alignment.horz = 2  # 设置水平居中, 1为设置垂直居中
    font.name = name  # 字体风格
    font.bold = False   # bold 字体为粗体
    font.colour_index = 0x08  # 字体的颜色
    font.height = height   # 字体在单元格的高度
    style.font = font  # 将字体应用样式
    return style

def write_excel(row, col, filename):
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet('new',cell_overwrite_ok=True)
    for i in range(0, len(row)):
        sheet1.write(i, 0, row[i], set_style('Times New Roman', 220, True))
    for i in range(0, len(col)):
        sheet1.write(i, 1, col[i], set_style('Times New Roman', 220, True))
    f.save(filename)

def read_excel(rfilename):
    wb = xlrd.open_workbook(filename)
    shee1 = wb.sheet_by_index(0)
    cols_row = shee1.nrows # 列总数
    cols_col = shee1.ncols # 行总数
    for i in range(cols_row):
        one_col = shee1.cell(i, 0).value #第i行第一格内容
        two_col = shee1.cell(i, 1).value #第i行第二格内容

