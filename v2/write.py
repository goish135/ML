#開啟檔案
fp = open("程式說明.txt","a")

#寫入 picture and text! 到檔案
#fp.write("123456")
fp.write("7891011"+'\n')
fp.write('678984'+'\n')

fp.close()