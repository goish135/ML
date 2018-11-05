# read deactive.xls and store as list # step 1 #
import xlrd
data     = xlrd.open_workbook('deactive.xlsx')
sheet1   = data.sheet_by_name(u'sheet1')
col_data = sheet1.col_values(5) # 欄位名: routeid 
col_data = col_data[1:]
#print(col_data)
len_col_data = len(col_data)
print(len_col_data) 

import numpy as np
import json 

# load 模型 # step 2
loss_road = 0

for i_1 in range(len_col_data):
	fn = './npy/'+col_data[i_1]+'.json.npy'
	try:
		w = np.load(fn)
		print('night')
		print(w)
		# read from rid folder and calcuate how many testing pair # step 3
	
		with open('./rid/'+col_data[i_1]+'.json','r') as f:
			value_list = json.load(f)
		print(value_list[:])	
		with open('sorted_time.json','r') as f:
			time_list  = json.load(f)
		print('sorted time')	
		# 前4個(前20分鐘的Data),預測第5個速率值	
		x = [] # test value
		y = [] # real value
		update_time_list = []
		
		start = 0
		set_number = len(value_list)-4
		for i in range(set_number):
			x.append([])
			for j in range(start,start+4):
				x[i].append(int(value_list[j]))
			y.append(int(value_list[start+4]))
			update_time_list.append(time_list[start+4])
			start = start + 1
		
		# matrix initial # step 4 
		#input()
		x = np.array(x)
		#input()
		# print(len(y)) # <= how many pair 
		x = np.concatenate((np.ones((x.shape[0],1)),x), axis=1)

		# predict value of road # step 5 # imp. 
		ans = []
		for i in range(len(x)):
			a = np.dot(w,x[i])
			ans.append(round(a,0))
		#print(ans)
		#print(len(ans))
		print(ans[:])
		#input()
		# 寫入 excel # step 6-1 write to excel 
		import xlwt
		table = xlwt.Workbook()
		sheet = table.add_sheet('sheet1')
		for i in range(len(ans)):   # add time ... V
			sheet.write(i,0,update_time_list[i])
			sheet.write(i,1,y[i])   # real 
			sheet.write(i,2,ans[i]) # predict
	
		time_predict_data = './predict/'+col_data[i_1]+'.xls'
		table.save(time_predict_data)   
		print('Save it?')
		#input()
		# 畫圖	# step 6-2 draw figure 
	except:
		print(col_data[i_1]+'not found')
		loss_road = loss_road + 1
		pass
print('loss_road',loss_road)		