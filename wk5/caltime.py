# 計時
import time
tStart = time.time() # 計時開始


time.sleep(2)
print("delay two seconds")
for x in range(1000):
	x+=1
	print(x)
tEnd = time.time() # 計時結束

print("It cost %f sec"%(tEnd-tStart)) # 格式化
print(tEnd-tStart)  