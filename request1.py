import requests
import json
import numpy as np
url = 'http://0.0.0.0:5000/api/'
#url = 'http://localhost:5000'
symptoms_dict = np.load('my_file.npy').item()
data = np.zeros(len(symptoms_dict))

inp = ['cramps','cough']
data[[symptoms_dict[str(inp[0])], symptoms_dict[str(inp[1])]]] = 1 
#data = [[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0]]
data = data.tolist()
print(data)
print(len(data))


def calle(data):
	url = 'http://0.0.0.0:5000/api/'
	j_data = json.dumps(data)
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	r = requests.post(url, data=j_data,headers=headers)
	print(r)
	print('yellow')
	print( r.text)
	return (r)


url = 'http://0.0.0.0:5000/api/'
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data,headers=headers)
print(r)
print('yellow')
print( r.text)