import xml.etree.ElementTree as ET
import xlwt
import os
import json
import glob

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


matchdata ={}

count_XML = 0
xxml = 0
miss = 0

fn = 'train_value.json'
with open(fn,'w',encoding='utf8') as f:
	f.write("[\n")
	for i_1 in glob.iglob("./parse/*/*/*/*.XML"):
	
		print(i_1)
		count_XML+=1
		try:
			tree_dynamic = ET.parse(i_1)
			root_dynamic = tree_dynamic.getroot()
			
			datatime = root_dynamic[0][0].attrib['datacollecttime']
	
			matchdata[datatime] = {}
			
			for j in root_dynamic.iter('Info'):
				
				routeid = j.attrib['routeid']
				value = j.attrib['value']
				matchdata[datatime][routeid] = value

		except:
			print('file error')
			xxml = xxml + 1
			pass
		if count_XML != 1:
			f.write(",\n")
		f.write(json.dumps(matchdata,indent=4,ensure_ascii=False))
		matchdata.clear();
	f.write("]\n")
					
print("Total:",count_XML)
print("total:",xxml)
print("Final:",count_XML-xxml)
print("miss:", miss)


	
