#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import xlrd
import xlwt
from datetime import date,datetime

# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()  # 初始化字体函数
    font.name = name  # 字体风格
    font.bold = bold   # 字体为粗体
    font.colour_index = 4  # 字体的颜色
    font.height = height   # 字体在单元格的高度
    style.font = font  # 将字体应用样式
    return style

# 写Excel
def write_excel_test():
    f = xlwt.Workbook(encoding='utf-8') # 创建Workbook,设置编码
    sheet1 = f.add_sheet('学生', cell_overwrite_ok=True)
    row0 = ['姓名', '年龄', '出生日期', '爱好']
    colum0 = ['张三', '李四', '恋习python', '小明', '小红', '无名', '小a']
    # 写第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))  # 第一个参数是行、第二个参数是列、第三个参数是输入内容，第四个参数是字体风格设置
    # 写第一列
    for i in range(0, len(colum0)):
        sheet1.write(i+1, 0, colum0[i], set_style('Times New Roman', 220, True))
    sheet1.write(1, 3, '我是2行4列')
    sheet1.write_merge(6, 7, 1, 3, '未知') #合并单元格
    # sheet1.write_merge(1, 2, 3, 3, '打游戏') #合并列单元格
    sheet1.write_merge(4, 5, 3, 4, '打篮球')

    f.save('test.xls')

# 读Excel
def read_excel_test():
    wb = xlrd.open_workbook(filename='test2.xls')  # 打开 'test2.xls' 文件
    print(wb.sheet_names())
    sheet1 = wb.sheet_by_index(0) # 通过索引获取表属性
    sheet2 = wb.sheet_by_name('年级')  # 通过表名称获取表属性
    print(sheet1,sheet2)
    print(sheet1.row_values(1), sheet1.col_values(0))
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    rows = sheet1.row_values(2)  # 获取第三行内容
    cols = sheet1.col_values(3)  # 获取第四列内容
    print(rows)
    print(cols)
    print(sheet1.cell(1,0).value) #获取第二行，第一列内容，下面方法同样
    print(sheet1.cell_value(1,0))
    print(sheet1.row(1)[0].value)
    print('=============================')
    print(sheet1.cell(1,2).ctype)  # 获取第二行，第三列的 ctype属性
    data_value = xlrd.xldate_as_tuple(sheet1.cell_value(1, 2), wb.datemode)  # 把内容处理为date格式
    print(data_value)
    print(date(*data_value[:3]))  # 转化为时间格式，下面同样
    print(date(*data_value[:3]).strftime('%Y/%m/%d'))
    print('============================')
    print(sheet1.merged_cells) # 获取合并格内容
    print(sheet1.cell_value(1,3)) # 输出合并格内容，下面同样
    print(sheet1.cell_value(4,3))
    print(sheet1.cell_value(6,1))

# 公共方法
def read_excel(filename, num=''):
    '''

    :param filename: 文件名称
    :param row_num: 想要查询的excel行数
    :return:
    '''
    row_content_list = []
    wb = xlrd.open_workbook(filename=filename)
    print ('start read %s excel' %filename)
    sheet1 = wb.sheet_by_index(0)
    cols_row = sheet1.nrows  # 行总数
    cols_col = sheet1.ncols  # 列总数
    if num != '':
        for row in range(cols_row):
            row_content = sheet1.cell_value(row, num)
            row_content_list.append(row_content)
    else:
        row_content_list = [sheet1.row_values(row) for row in range(cols_row)]
    return row_content_list

if __name__ == '__main__':
    read_excel()
    # write_excel()