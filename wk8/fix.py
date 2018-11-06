import json 

with open("ValueData.json","r") as f:
	data = json.load(f)

for i in data.copy():
	data['6'+str(i)] = data[i]
	del data[i]

with open("ValueData.json","w") as f:
	json.dump(data,f,indent=4)
