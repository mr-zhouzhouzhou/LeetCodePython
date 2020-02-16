# import sys
# from xlrd import open_workbook # xlrd用于读取xld
# import xlwt  # 用于写入xls
# workbook = open_workbook(r'1.xls')  # 打开xls文件
# sheet_name= workbook.sheet_names()  # 打印所有sheet名称，是个列表
# #sheet = workbook.sheet_by_index(0)  # 根据sheet索引读取sheet中的所有内容
# sheet1= workbook.sheet_by_name('6113')  # 根据sheet名称读取sheet中的所有内容
# #print(sheet.name, sheet.nrows, sheet.ncols)  # sheet的名称、行数、列数
# # 第六列内容
#
# cell = sheet1.cell(79,0).value
# print(cell, type(cell))
# for item in sheet_name:
#     pass

import sys
import xlrd
from xlwt import *
from xlutils.copy import copy

xlsfile = '1.xls'
book = xlrd.open_workbook(xlsfile)
sh = book.sheet_by_name("6113")
sheet_name = book.sheet_names()
#print(sheet_name)
#data = ["######", "######", "######", "######", "######", "######", "######", "######"]
data = ["0", "43817", "月度综合检查", "检查设备外观、清理设备卫生、有无内漏、检测仪检查有无外漏、各连接部位是否存在锈蚀","卫生清洁、无内漏、无外漏、无锈蚀","徐帅"]


for name in sheet_name:

    sheet = book.sheet_by_name(name)
    nrows = sheet.nrows
    ncols = sheet.ncols
    # print(nrows)
    # print(ncols)

    row_data = sheet.row_values(-1)
    col_data = sheet.col_values(-1)
    # print(row_data)
    # print(col_data)
    for index, value in enumerate(data):
        if index == 0:
            value = int(sheet.cell(-1, 0).value) + 1
            print("value:  " ,value)
            #index_0 = float(sheet.cell(59,0)).split(":")[1])//1
            sheet.put_cell(len(col_data), index, xlrd.XL_CELL_TEXT, str(value), 0)
        else:
            sheet.put_cell(len(col_data), index, xlrd.XL_CELL_TEXT, value, 0)
    # sheet.put_cell(len(col_data),0,xlrd.XL_CELL_TEXT,u"13",None)
    # sheet.put_cell(len(col_data),1,xlrd.XL_CELL_TEXT,u"月度综合检查",None)
    # sheet.put_cell(79,2,xlrd.XL_CELL_TEXT,u"月度综合检查",None)
    # sheet.put_cell(79,3,xlrd.XL_CELL_TEXT,u"RDYJSKUWCVSUWVUSW",None)
    # sheet.put_cell(79,4,xlrd.XL_CELL_TEXT,u"检查设备外观、清理设备卫生、有无内漏、检测仪检查有无外漏、各连接部位是否存在锈蚀",None)
    # sheet.put_cell(7,5,xlrd.XL_CELL_TEXT,u"徐帅",None)
    # #sheet.put_cell(79,1,5,"徐帅",0)

    # data = ["43817","月度综合检查", "检查设备外观、清理设备卫生、有无内漏、检测仪检查有无外漏、各连接部位是否存在锈蚀","卫生清洁、无内漏、无外漏、无锈蚀","徐帅"]
    #
    # print(sheet.cell(-1,1))
wb = copy(book)
wb.save(xlsfile)
    #
    # cell_value = sheet.cell_value(3,0)
    # print(cell_value)
    # cell_value2 = sheet.cell(3,0)
    # print(cell_value2)
    #
    # sheet.put_cell(1,2,1,"test",0)
    # cell_value2 = sheet.cell(1,1)
    # print(cell_value2)
    #
    # #保存xlsfile
    # wb = copy(book)
    # wb.save(xlsfile)


