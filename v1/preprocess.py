import xml.etree.ElementTree as ET
import xlwt
import os

#建一個試算表
table = xlwt.Workbook()
sheet = table.add_sheet('sheet1')

#parse static
tree_1 = ET.parse('./static.xml')
root_1 = tree_1.getroot()
sheet.write(0,0,'routeid')
row = 1
list = []
for info in root_1.iter('Info'):
	sheet.write(row,0,info.attrib['routeid'])
	list.append(info.attrib['routeid'])
	row += 1

#parse multi dynamic
number = 1
pre  = './812/' #path
tail = '.xml'
for count in range(144): #xml
	mid = str(number)
	path = pre+mid+tail
	print(path)
	tree_2 = ET.parse(path)
	root_2 = tree_2.getroot()
	sheet.write(0,number,root_2[0][0].attrib['datacollecttime'])
	for i in range(len(list)):
		for j in root_2.iter('Info'):
			if list[i] == j.attrib['routeid']:
				sheet.write(i+1,number,j.attrib['value'])
	number = number + 1

	
table.save('value812.xls')
	
