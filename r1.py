import requests
import json
import numpy as np
url = 'http://localhost:5000/api/'
#url = 'http://localhost:5000'
symptoms_dict = np.load('my_file.npy').item()
data = np.zeros(len(symptoms_dict))

inp = ['cramps','cough']
data[[symptoms_dict[str(inp[0])], symptoms_dict[str(inp[1])]]] = 1 
data = data.tolist()
print(data)
print(len(data))
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data,headers=headers)
print(r)
print('yellow')
print( r.text)


# def calle(j_data):
# 	url = 'http://0.0.0.0:5000/test/'
# 	j_data = json.dumps(data)
# 	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
# 	r = requests.post(url, data=j_data,headers=headers)
# 	print(r)
# 	print('yellow')
# 	print( r.text)
# 	return (r)

# print(calle(j_data))