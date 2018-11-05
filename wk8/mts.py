#import os
#import xlrd

#from openpyxl import load_workbook#xlsx
import glob 
import xlrd #xls#

dict = {}
#  time :  8 9 10 11 12 13 14 15 16 17 #
row     = [0,8,21,33,44,57,69,81,92,105] 
for f in glob.iglob("./predict/*.xls"):
	#print(f)
	fn = f[11:21]
	#print(fn)
	#wb=load_workbook(f)
	#a_sheet = wb.sheet_by_index(0)
	#sheet = wb.active
	book  = xlrd.open_workbook(f)
	sheet = book.sheet_by_index(0)
	#print(sheet.row_values(1)[2]) # (1,2)
	
	#sheet = book.active
	#print(sheet.nrows)
	#print(sheet.ncols)
	for t in range(9): # 8->17 # total hours:9
		if fn not in dict:
			dict[fn] =[sheet.row_values(row[t])[2]]
		else:
			dict[fn].append(sheet.row_values(row[t])[2])
		#print(type(sheet['C1']))
		#print(sheet['C'+str(row[t]+1)])

import json
filename = 'ValueData.json'
with open(filename,'w',encoding='utf8') as f:
	f.write(json.dumps(dict,indent=4,ensure_ascii=False))
		