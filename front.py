from flask import request, redirect
from flask import Flask
import numpy as np
import pickle as p
import re
app = Flask(__name__)

symptoms_dict = np.load('my_file.npy').item()
data = np.zeros(len(symptoms_dict))

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/signup', methods = ['GET','POST'])
def signup():
    email = request.form["description"]
    print("The email address is '" + email + "'")
    inp = re.findall(r'\w+', email)
    data[[symptoms_dict[str(inp[0])], symptoms_dict[str(inp[1])]]] = 1 
    prediction = model.predict([data])
    return (np.array2string(prediction))



if __name__ == '__main__':
    modelfile = 'model1.pkl'
    print('found')
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)

