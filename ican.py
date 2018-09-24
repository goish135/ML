import xml.etree.ElementTree as ET
import xlwt
import os
import json

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

with open('./train.json','r',encoding='utf8') as f:
		data = json.load(f)
		total = len(data)
		#for i in range(total):
		#	print(data[i][0])

datacollecttime = []
value           = []
for k in range(len(data)):
	value.append([])
			
count_XML = 0
xxml = 0
for i_1 in os.listdir("./parse"):
	#print(i_1)
	for i_2 in os.listdir("./parse/"+i_1):
		#print(i_2)
		for i_3 in os.listdir("./parse/"+i_1+"/"+i_2):
			#print(i_3)
			for i_4 in os.listdir("./parse/"+i_1+"/"+i_2+"/"+i_3):
				#print(i_4)
				count_XML+=1
				try:
					tree_dynamic = ET.parse("./parse/"+i_1+"/"+i_2+"/"+i_3+"/"+i_4)
					root_dynamic = tree_dynamic.getroot()
					datacollecttime.append(root_dynamic[0][0].attrib['datacollecttime'])
					for i in range(len(data)):
						#print(len(data))
						flag = 0
						for j in root_dynamic.iter('Info'):
							#print('Ok')
							if data[i][0] == j.attrib['routeid']:
								value[i].append(j.attrib['value'])
								flag = 1
								#print('add')
						if flag == 0 :
							value[i].append('-1')
							#print('no value')
						#print("while")	
				except:
					print('file size is too small')
					xxml = xxml + 1
					pass
			print('Hi')		
					
print("Total:",count_XML)
print("total:",xxml)
print("Final:",count_XML-xxml)

fn = 'train_value.json'
with open(fn,'w+',encoding='utf8') as f:
	f.write(json.dumps(datacollecttime,indent=4,ensure_ascii=False))
	f.write(json.dumps(value,indent=4,ensure_ascii=False))