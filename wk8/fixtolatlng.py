import json

#def swap(a,b):
#	t = a
#	a = b
#	b = t

with open("static.json","r") as f:
	data = json.load(f)

for rid in data.copy():
	t1 = data[rid][0]
	data[rid][0] = data[rid][1]
	data[rid][1] = t1
	print(data[rid][0])
	print(data[rid][1])
	t2 = data[rid][2]
	data[rid][2] = data[rid][3]
	data[rid][3] = t2
	
with open("staticv2.json","w") as f:
	json.dump(data,f,indent=4)