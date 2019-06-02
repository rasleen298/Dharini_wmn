from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
#from request1 import calle 

app = Flask(__name__)

symptoms_dict = np.load('my_file.npy').item()
data = np.zeros(len(symptoms_dict))

inp = ['cramps','cough']
data[[symptoms_dict[str(inp[0])], symptoms_dict[str(inp[1])]]] = 1 
#print(calle(data))
@app.route('/api', methods=['GET'])
def test():
	
# def test():
# 	a = calle(data)
# 	print(a)
# 	print(a.text)
# 	return (a)
# def test():
# 	if request.method == 'GET':
# 		print('wtf')
# 		return('<form action="/test" method="post"><input type="submit" value="Send" /></form>')
# 	elif request.method=='POST':
# 		return("OKKK")
# 	else:
# 		return("kjbcwl	")
# def test():
#     if request.method=='GET':

#     	return('<form action="/test" method="post"><input type="submit" value="Send" /></form>')

#     elif request.method=='POST':
#         return "OK this is a post method"
#     else:
#         return("ok")
def makecalc():
	if request.method == 'GET':			
		
		data = request.get_json()
		print('hey!!')
		    
		d = np.asarray(data)
		print(d)
		    #d[0] = data;
		prediction = model.predict([d])
		print(prediction)
		return jsonify(np.array2string(prediction))
		# return jsonify(np.array2string(prediction))
	    # if prediction is not None:
	    # 	prediction= float(prediction)
	    
	    

if __name__ == '__main__':
    modelfile = 'model1.pkl'
    print('found')
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')
    #app.run(port=5000,debug=True)
    #app.run(debug=True, host='0.0.0.0')
