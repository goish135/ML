import xlrd,os
import numpy as np
import math

data = xlrd.open_workbook('./train.xls')
table = data.sheet_by_name('sheet1')

col_value = table.row_values(5) # 66000m10153
# 從0開始編號 

x = []
y = []
start = 1

total = (table.ncols-1)-5+1
for i in range(total):
	x.append([])
	for j in range(start,start+4): # 1 2 3 4
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
	if col_value[start+4] == '':   # 5
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

	
x = np.array(x)
y = np.array(y)	

x = np.concatenate((np.ones((x.shape[0],1)),x),axis=1)
w = np.zeros(len(x[0]))
l_rate = 10
repeat = 36025

x_t = x.transpose()
s_gra = np.zeros(len(x[0]))

for i in range(repeat):
	hypo = np.dot(x,w)
	loss = hypo - y
	cost = np.sum(loss**2)/len(x)
	cost_a = math.sqrt(cost)
	gra = np.dot(x_t,loss)
	s_gra += gra**2
	ada = np.sqrt(s_gra)
	w = w - l_rate*gra/ada
	print('iteration:%d | Cost: %f '%(i,cost_a))

# save model
np.save('value.npy',w)





