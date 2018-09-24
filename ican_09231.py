import xml.etree.ElementTree as ET
import xlwt
import os
import json
import glob

routeid     = []
roadsection = []


#tree_static = ET.parse("static.XML")
#root_static = tree_static.getroot()
#for info in root_static.iter('Info'):
#	rr          = []
#	rr.append(info.attrib['routeid'])
#	rr.append(info.attrib['roadsection'])
#	routeid.append(rr)
#filename = 'train.json'
#with open(filename,'w+',encoding='utf8') as f:
#		f.write(json.dumps(routeid,indent=4,ensure_ascii=False))
#		#f.write(json.dumps(roadsection,indent=4,ensure_ascii=False))
data = []
with open('./train.json','r',encoding='utf8') as f:
		data = json.load(f)
		total = len(data)
		#for i in range(total):
		#	print(data[i][0])

matchdata = {i[0]:{} for i in data}

datacollecttime = []
value           = []
for k in range(len(data)):
	value.append([])
			
count_XML = 0
xxml = 0
miss = 0
for i_1 in glob.iglob("./parse/*/*/*/*.XML"):

	print(i_1)
	count_XML+=1
	try:
		tree_dynamic = ET.parse(i_1)
		root_dynamic = tree_dynamic.getroot()
		
		datatime = root_dynamic[0][0].attrib['datacollecttime']
		datacollecttime.append(datatime)
		
		for j in root_dynamic.iter('Info'):
			if j.attrib['routeid'] in matchdata:
				matchdata[j.attrib['routeid']][datatime] = j.attrib['value']
			else:
				matchdata[j.attrib['routeid']] = {datatime:j.attrib['value']}
				print('fuck')
				miss = miss + 1

	except:
		print('file error')
		xxml = xxml + 1
		pass
		
					
print("Total:",count_XML)
print("total:",xxml)
print("Final:",count_XML-xxml)
print("fuck:", miss)

fn = 'train_value.json'
with open(fn,'w',encoding='utf8') as f:
	f.write(json.dumps(matchdata,indent=4,ensure_ascii=False))
