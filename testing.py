import numpy as np
#import csv
w = np.load('value.npy')

import xlrd,os
import numpy as np
import math

data = xlrd.open_workbook('./value812.xls')
table = data.sheet_by_name('sheet1')

col_value = table.row_values(5) # 66000m10153
#print(col_value[1:table.ncols])


x = []
y = []
start = 63

total = 73
for i in range(total):
	x.append([])
	for j in range(start,start+4):
		if col_value[j] == '':
			flag = 0 
			for k in range(j-1,1,-1):
				if col_value[k] != '':
					col_value[j] = col_value[k]
					flag = 1
					break
			if flag == 0 :
				for m in range(j+1,total):
					if col_value[m]!='':
						col_value[j]=col_value[m]
						flag = 1
						break
			if flag == 0:
				col_value[j] = 200
		x[i].append(int(col_value[j]))
	if col_value[start+4] == '':
		mark = 0
		for a in range(start+4-1,1,-1):
			if col_value[a]!='':
				col_value[start+4] = col_value[a]
				mark = 1
				break
		if mark == 0:
			for b in range(start+4+1,total):
				if col_value[b]!='':
					col_value[start+4] = col_value[b]
					mark = 1
					break
		if mark == 0:
			col_value[start+4]=200	
	y.append(int(col_value[start+4]))
	start+=1
	#print(i,'pairs')
	#print(x[i][0:4])
	#print(y[i])
	
	
x = np.array(x)

print(len(y))
x = np.concatenate((np.ones((x.shape[0],1)),x), axis=1)

ans = []
for i in range(len(x)):
	a = np.dot(w,x[i])
	ans.append(round(a,0))

#print(ans)
print(len(ans))
import xlwt
table = xlwt.Workbook()
sheet = table.add_sheet('sheet1')
for i in range(len(ans)):
	sheet.write(i,0,y[i])
	sheet.write(i,1,ans[i])
table.save('ans.xls')	