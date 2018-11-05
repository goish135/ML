import json

with open('test_value.json','r',encoding='utf-8') as f:
	data = json.load(f)
	total = len(data)


matchroadid  = list(data.keys())

#timelist  = [list(data[i].keys()) for i in matchroadid]#
#value = [list(data[i].values()) for i in matchroadid]#

#print('len1:',len(time[0]))   # 51
#print('len2:',len(value[0]))  # 51
# 51 / 6573

for rid in matchroadid:
	timelist = [list(data[rid].keys())]
	value    = [list(data[rid].values())]

	pair = []                                # merge to time - value
	for i in range(len(timelist[0])):
		pair.append([timelist[0][i],value[0][i]])


	fn3 = 'sorted_time.json'	
	with open(fn3,'r') as f:
		format_newlist = json.load(f)
		
	# supplement data # i:第幾個時間(段) 
	all = []
	for i in range(len(format_newlist)):
		all.append([])
		for j in range(len(timelist[0])): 
			if format_newlist[i] == pair[j][0]:
				all[i] = pair[j][1]
				#print(i,all[i])


	for i in range(len(format_newlist)):
		#print(all[i])
		if len(all[i]) == 0:
			#print(all[i]) # value
			flag = 0       # 找不到 
			for j in range(i+1,len(format_newlist)): #往後找
				if len(all[j])!=0:
					all[i] = all[j]
					flag = 1                  #有補上
					break
			if flag == 0:		
				for k in range(i-1,-1,-1):
					if len(all[k])!=0:
						all[i] = all[k]
						flag = 1
						break
			if flag == 0:
				print('amazing')
				#all[i].append(100)
				break
	if flag == 0 : # 該路段在期間內，未回傳任何速率值
		continue
	# supplement end
	filename = rid +".json"
	with open('./rid/'+filename,'w') as f:
		json.dump(all,f)
	
			
