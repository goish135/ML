from os import listdir
from os.path import isfile,isdir,join
import xlwt
import xml.etree.ElementTree as ET

#CREATE ONE TABLE
table = xlwt.Workbook()
sheet = table.add_sheet('sheet1')
path = "./parse/"
lay_2 = listdir(path)
#parse static
tree_1 = ET.parse('./static.xml')
root_1 = tree_1.getroot()
sheet.write(0,0,'routeid') #第0列第0欄
row = 1
list = []
for info in root_1.iter('Info'):
	sheet.write(row,0,info.attrib['routeid']) #路段id
	list.append(info.attrib['routeid'])
	row += 1

col = 1	
#parse more multi dynamic	
for f in lay_2:
	lay_3 = listdir(path+f)
	for ff in lay_3:
		lay_4 = listdir(path+f+'/'+ff)
		for fff in lay_4:
			lay_5 = listdir(path+f+'/'+ff+'/'+fff)
			#start parse into excel
			for file in lay_5:
				try:
					tree_2 = ET.parse(path+f+'/'+ff+'/'+fff+'/'+file)	
					root_2 = tree_2.getroot()					
					sheet.write(0,col,root_2[0][0].attrib['datacollecttime']) #資料收集時間
					for i in range(len(list)): #路段數量
						for j in root_2.iter('Info'):
							if list[i] == j.attrib['routeid']:
								sheet.write(i+1,col,j.attrib['value']) #路段速率
					print('Success write!')			
					col+=1		
				except:
					print('ignore error then continue')
					pass
			#col+=1
					
table.save('train.xls')					
				
	

