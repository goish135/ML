#import xml.etree.ElemetTree as ET
import xml.etree.ElementTree as ET
tree = ET.parse('static.xml')
root = tree.getroot()

dict = {}
import xlrd 
data     = xlrd.open_workbook('deactive.xlsx')
sheet    = data.sheet_by_name('sheet1')
col_data = sheet.col_values(5)
col_data = col_data[1:]

for rid in col_data:
	for info in root.iter('Info'):
		if info.attrib['routeid'] == rid:
			fromkm = info.attrib['fromkm']
			x1,y1= fromkm.split(',')
			tokm   = info.attrib['tokm']
			x2,y2  = tokm.split(',')
			dict[rid] = [float(x1),float(y1),float(x2),float(y2)]

import json
filename = "static.json"
with open(filename,"w") as f:
	json.dump(dict,indent=4,ensure_ascii=False, fp=f)