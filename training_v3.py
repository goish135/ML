
import numpy as np
import math

# 取出 train Data
# data = xlrd.open_workbook('./train.xls')
# table = data.sheet_by_name('sheet1')

# 取 第六列的Data 的 col values # 
# col_value = table.row_values(5) # 66000m10153
# 從0開始編號 

# 補缺失值及建立矩陣#
#start = 1

#total = (table.ncols-1)-5+1
#for i in range(total):
#	x.append([])
#	for j in range(start,start+4): # 1 2 3 4
#		if col_value[j] == '':
#			flag = 0 
#			for k in range(j-1,1,-1):
#				if col_value[k] != '':
#					col_value[j] = col_value[k]
#					flag = 1
#					break
#			if flag == 0 :
#				for m in range(j+1,total):
#					if col_value[m]!='':
#						col_value[j]=col_value[m]
#						flag = 1
#						break
#			if flag == 0:
#				col_value[j] = 200
#		x[i].append(int(col_value[j]))
#	if col_value[start+4] == '':   # 5
#		mark = 0
#		for a in range(start+4-1,1,-1):
#			if col_value[a]!='':
#				col_value[start+4] = col_value[a]
#				mark = 1
#				break
#		if mark == 0:
#			for b in range(start+4+1,total):
#				if col_value[b]!='':
#					col_value[start+4] = col_value[b]
#					mark = 1
#					break
#		if mark == 0:
#			col_value[start+4]=200	
#	y.append(int(col_value[start+4]))
#	start+=1
# end # 	


# 讀入 json (4個)
# id : 
# 1. 66000m4BR14
# 2. 66000m3JE02
# 3. 66000m4MK17
# 4. 66000m1CV16 
rid = input('input routeid:')
print('my input',rid)

import json
with open(rid+'.json','r') as f:
	value_list = json.load(f)
	lenlen        = len(value_list)

#print('list 長度:',lenlen) -- read OK

set_number = lenlen - 4 # 6571 6570 6569 6568 # 6572 - 6568 = 4
print('set_number:',set_number) # imp. 

x = []
y = []

start  = 0 
for i in range(set_number):
	x.append([])                   # two - dimention
	for j in range(start,start+4): # 0 1 2 3  # total is 'four' 
		#print('shift:',j)
		#a =input()
		x[i].append(int(value_list[j]))
	y.append(int(value_list[start+4]))	
	start = start + 1	


# print matrix #	
#for i in range(set_number):
#	for j in range(len(x[i])):
#		print(x[i][j],end=" ")  # -- Ok	
#	print()
#	print(y[i])                 # -- Ok
#	print("/")



######################################################## optimized ########################################################

	
x = np.array(x)
y = np.array(y)	

x = np.concatenate((np.ones((x.shape[0],1)),x),axis=1)
w = np.zeros(len(x[0]))                               # weight initialize


l_rate= input('lr:')
log_decent = {}  # declare dict
log_decent['learning rate'] = l_rate
repeat= input('re:')
log_decent['repeat'] = repeat
l_rate = int(l_rate)
repeat = int(repeat) 
# Before : 36024

x_t = x.transpose()
s_gra = np.zeros(len(x[0]))







pre = -1
repeat_ending = -1   
for i in range(repeat):
#while True:
	hypo = np.dot(x,w)
	loss = hypo - y
	cost = np.sum(loss**2)/len(x)
	cost_a = math.sqrt(cost)
	gra = np.dot(x_t,loss)
	s_gra += gra**2
	ada = np.sqrt(s_gra)
	w = w - l_rate*gra/ada
	print('iteration:%d | Cost: %f '%(i,cost_a))
	log_decent[i] = cost_a
	if pre == cost_a:
		repeat_ending = i
		stop = input()
		break
	pre = cost_a 

log_decent['update_repeat'] = repeat_ending	


with open(rid+'_log.json','w') as f:
	json.dump(log_decent,f,indent=4)

# save model
np.save(rid+'.npy',w)
