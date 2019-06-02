from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
# from r1 import calle 

app = Flask(__name__)

# @app.route('/')
# def index():
# 	return 'hi'

@app.route('/api/', methods=['POST'])
# def test():
# 	if request.method=='POST':
# 		data = request.data
# 		print(data)
# 		return 'hi'
# 	#calle(data)

def makecalc():
	
		
	data = request.get_json(force = True)
	print(data)
	print('noht')
	#data1 = json.loads(np.array2string(data))
	#print(data1)
	print('hey!!')
	    
	d = np.asarray(data)
	print(d)
	    #d[0] = data;
	prediction = model.predict([d])
	print(prediction)
	#print()
	#return jsonify(np.array2string(prediction))
	
	    
	    

if __name__ == '__main__':
    modelfile = 'model1.pkl'
    print('found')
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)
    