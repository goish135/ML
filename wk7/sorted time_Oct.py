import json

#with open('train_value.json','r',encoding='utf-8') as f:
#	data = json.load(f)
#	total = len(data)
	
#matchroadid = ['66000m3JE02']

#time  = [list(data[i].keys()) for i in matchroadid]
#value = [list(data[i].values()) for i in matchroadid]

#print('len1:',len(time[0]))   # 51
#print('len2:',len(value[0]))  # 51
# 51 / 6573

#pair = []                                # merge to time - value
#for i in range(len(time[0])):
#	pair.append([time[0][i],value[0][i]])


	
with open("./time.json",'r') as f:
		content = json.load(f)	
		print(len(content)) # 6573

space =content[0].split()
#print(space[0])  #year/month/day
#print(space[1])  #hour:minute:second
listA = space[0].split('/')
listB = space[1].split(':')
#print(listA)
#print(listB)
year  = int(listA[0])
month = int(listA[1])
date  = int(listA[2])
hour  = int(listB[0])
minute= int(listB[1])
second= int(listB[2])

#print('>>>',year,month,date)
#print('>>>',hour,minute,second)
	
import time 

tple = (year,month,date,hour,minute,second,0,0,0)
secs = time.mktime(tple) 
tA=time.localtime(secs)
StyleTime =time.strftime("%Y/%m/%d %H:%M:%S",tA)
#print(StyleTime)
#print(secs)	# --OK

# sort
newlist = []
for i in range(len(content)):
	space=content[i].split()
	listA = space[0].split('/')
	listB = space[1].split(':')
	year  = int(listA[0])
	month = int(listA[1])
	date  = int(listA[2])
	hour  = int(listB[0])
	minute= int(listB[1])
	second= int(listB[2])
	tple = (year,month,date,hour,minute,second,0,0,0)
	secs = time.mktime(tple)
	#tA=time.localtime(secs)
	#StyleTime = time.strftime("%Y/%m/%d %H:%M:%S",tA)
	newlist.append(secs)

result = sorted(newlist)
print(result)

# sec to format of y/m/d h:m:s
format_newlist = []
for i in range(len(result)):
	tA=time.localtime(result[i])
	StyleTime = time.strftime("%Y/%m/%d %H:%M:%S",tA)
	format_newlist.append(StyleTime)

#for j in range(len(result)):
#	print(format_newlist[j])

fn3 = 'sorted_time.json'	
with open(fn3,'w',encoding='utf8') as f:
	f.write(json.dumps(format_newlist,indent=4,ensure_ascii=False))