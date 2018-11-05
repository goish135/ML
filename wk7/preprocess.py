import xml.etree.ElementTree as ET
import xlwt
import os
import json
import glob

routeid     = []
roadsection = []



data = []
with open('./train.json','r',encoding='utf8') as f:  # 路段id ，路段名 
		data = json.load(f)
		total = len(data)

# deactive.xlsx #
import xlrd  # 用 xlrd 讀取 Excel 
data_2 = xlrd.open_workbook('deactive.xlsx')
sheet1 = data_2.sheet_by_name(u'sheet1')
col_data = sheet1.col_values(5)  # 第5個為routeid 
print(col_data[1:])

matchroadid = col_data[1:]
matchdata = {i[0]:{} for i in matchroadid}　# 第幾個routeid

datacollecttime = []
value           = []
for k in range(len(data)):
	value.append([])
			
count_XML = 0
xxml = 0
fine = 0
for i_1 in glob.iglob("./dynamic data/*.XML"):
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
				print('fine')
				fine = fine + 1

	except:
		print('file error')
		xxml = xxml + 1
		pass
		
					
print("Total:",count_XML)
print("total:",xxml)
print("Final:",count_XML-xxml)
print("fine:", fine)

fn = 'test_value.json'
with open(fn,'w',encoding='utf8') as f:
	f.write(json.dumps(matchdata,indent=4,ensure_ascii=False))