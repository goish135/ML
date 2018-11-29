# 讀 儲 寫
import xlrd
import glob #多檔(同類型)處理
import matplotlib.pyplot as plt
import numpy as np

for file in glob.iglob("./v3_predict/*.xls"):
	filename = file[13:len(file)-4]
	real    = []
	predict = []
	book  = xlrd.open_workbook(file)
	sheet = book.sheet_by_index(0)
	
	
	for i in range(109):
		cell_1 = sheet.cell(i,1) # real
		cell_2 = sheet.cell(i,2) # predict
		real.append(cell_1.value)
		predict.append(cell_2.value)
		
	
	# 畫圖	# 10/20 testing 
	xx = np.linspace(1,109,109) 
	yy1 = real
	yy2 = predict

	plt.figure()
	plt.title(filename)
	plt.plot(xx,yy1,label='real') #blue line
	plt.plot(xx,yy2,color='red',label='predict')
	plt.legend(loc='upper left')
	plt.xlim((1,109))    
	plt.ylim((10,80))   
	plt.xlabel('time')
	plt.ylabel('value')
	plt.xticks([10,20,30,40,50,60,70,80,90,100],['9:01','9:50','10:44','11:35','12:21','13:11','14:05','14:53','15:44','16:36']) 
	#plt.show()
	plt.savefig('./img/'+filename+'.png')