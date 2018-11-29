import glob
import xlrd

dict  = {} # key(路段ID) => filename , value(速率) => percent
for file in glob.iglob("./v3_predict/*.xls"):
    filename = file[13:len(file)-4]
    #print(filename)
    book = xlrd.open_workbook(file)
    sheet = book.sheet_by_index(0)
	
    nrows = sheet.nrows # 有幾列
    #print('nrows:',nrows)
    SSres = 0
    avg   = 0
	
    
    for i in range(nrows):
        #print(sheet.cell(i,1),sheet.cell(i,2))
        #print(type(sheet.cell(i,1)))
        cell_1 = sheet.cell(i,1) # real
        cell_2 = sheet.cell(i,2) # predict
        avg   = avg + cell_1.value 
        #print(type(cell.value))
        SSres = SSres + (cell_1.value-cell_2.value)*(cell_1.value-cell_2.value)
    #print('殘差平方和:',SSres)
	
    avg = avg / nrows
    SStot = 0
    for i in range(nrows):
        SStot = SStot + (sheet.cell(i,2).value - avg)*(sheet.cell(i,2).value - avg)
    if SStot!=0:
        dict[filename]  = 1 - (SSres / SStot)
        print(filename,': ',dict[filename])
    else:
        print('SStot 等於 0')
		
# 紀錄 路段ID及其準確率 
import json
with open('evaluate.json','w') as f:
    f.write(json.dumps(dict,indent=4))

		