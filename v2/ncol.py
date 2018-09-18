import xlrd
excel = xlrd.open_workbook('./value812.xls')

table = excel.sheet_by_name('sheet1')
cols  = table.ncols

print('cols:',cols)