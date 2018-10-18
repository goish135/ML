import numpy as np
import math

#手動輸入指定json檔案
#rid = input('input routeid:')
#print('my input',rid)

# 迴圈處理多檔 #
from os import listdir
from os.path import isfile,isdir,join
# 指定要列出所有檔案的目錄
OkData = "./OkData"
# 取得所有檔案與子目錄名稱
files = listdir(OkData)

total_fs = 0
for fs in files:
	print(fs) # 檔名
	
	total_fs+=1
#print('total_fs',total_fs)
	# 產生檔案的絕對路徑
	fullpath = join(OkData,fs) 		
	import json
	with open(fullpath,'r') as f:
		value_list = json.load(f)
		lenlen        = len(value_list)

#print('list 長度:',lenlen) -- read OK

	set_number = lenlen - 4 # 6571 6570 6569 6568 # 6572 - 6568 = 4
#print('set_number:',set_number) # imp. 

	x = []
	y = []

	start  = 0 
	x_ok   = 0
	y_ok   = 0
	flag   = 0
	for i in range(set_number):
		x.append([])                   # two - dimention
		for j in range(start,start+4): # 0 1 2 3  # total is 'four' 
#		#print('shift:',j)
		#a =input()
			try:
				x[i].append(int(value_list[j]))
				x_ok = 1
			except:
				print("No return value:x")
				pass
		try:		
			y.append(int(value_list[start+4]))
			y_ok = 1
		except:
			print("No return value:y")
			pass
		if x_ok == 1 and y_ok ==1:	
			start = start + 1
		else: 
			flag = 1
			break
	if flag==1:
		print('Novalid',fs)
		continue
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


	#l_rate= input('lr:')
	l_rate = 10 
	log_decent = {}  # declare dict
	log_decent['learning rate'] = l_rate
	#repeat= input('re:')
	repeat = 30000
	log_decent['repeat'] = repeat
	l_rate = int(l_rate)
	repeat = int(repeat) 
	#Before : 36024

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
			#stop = input()
			break
		pre = cost_a 

	log_decent['update_repeat'] = repeat_ending	


	with open('./output/log/'+fs+'_log.json','w') as f:
		json.dump(log_decent,f,indent=4)

	# save model
	np.save('./output/npy/'+fs+'.npy',w)
	print('model#',total_fs)	
