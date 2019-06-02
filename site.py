from flask import request, redirect, render_template
from flask import Flask
import numpy as np
import pickle as p
import re

app = Flask(__name__)

symptoms_dict = np.load('my_file.npy').item()
data = np.zeros(len(symptoms_dict))

@app.route('/')
def hello_world():
    return render_template("normal.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/chat')
def chaat():
    return render_template("chat.html")

@app.route('/here_api_trail1')
def track():
    return render_template("here_api_trail1.html")

@app.route('/signup', methods = ['GET','POST'])
def signup():
    email = request.form["description"]
    print("The email address is '" + email + "'")
    inp = re.findall(r'\w+', email)
    for i in range(len(inp)):
        data[[symptoms_dict[str(inp[i])]]] = 1
    prediction = model.predict([data])
    return (np.array2string(prediction))

@app.route('/chatbot', methods = ['GET','POST'])
def chat():
	return(render_template("/chat.html"))

if __name__ == '__main__':
    modelfile = 'model1.pkl'
    print('found')
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)

