from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
import cv2
import os
import glob
import pickle
import face_recognition
import json
from flask_socketio import SocketIO



app = Flask(__name__)
socketio = SocketIO(app)





@app.route('/')
def upload_file():
   return app.send_static_file('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():#if __#if __name__ == '__main__':
#    app.run(debug = True)name__ == '__main__':
#    app.run(debug = True)
   if request.method == 'POST':
      f = request.files['file']	
      u = request.args.get('name')
      print(u)
      if not os.path.exists(u):
            os.mkdir(u) 
      f.save(u+"/"+secure_filename(u + '.jpg' ))
      return 'file uploaded successfully'
		
#if __name__ == '__main__':
#    app.run(debug = True)


@app.route('/')
def hello_world():
    return 'Hello, World!'




@app.route('/predict', methods = ['GET','POST'])
def predict():
    distance_threshold=0.6
    if request.method == 'POST':
        f = request.files['file']	
        u = 'test'
        print(u)	
        f.save("/home/abhishek/hack-in-out-2018/examples/knn_examples/test"+"/"+secure_filename(u + '.jpg' ))
        
    model_path="/home/abhishek/hack-in-out-2018/examples/trained_knn_model.clf"
    knn_clf=None
    for image_file in os.listdir("/home/abhishek/hack-in-out-2018/examples/knn_examples/test"):
        full_file_path = os.path.join("/home/abhishek/hack-in-out-2018/examples/knn_examples/test", image_file)
        X_img_path = full_file_path
    
     # Load a trained KNN model (if one was passed in)
        if knn_clf is None:
            with open(model_path, 'rb') as f:
                knn_clf = pickle.load(f)

    # Load image file and find face locations
        X_img = face_recognition.load_image_file(X_img_path)
        X_face_locations = face_recognition.face_locations(X_img)

    # If no faces are found in the image, return an empty result.
        if len(X_face_locations) == 0:
            return []

    # Find encodings for faces in the test iamge
        faces_encodings = face_recognition.face_encodings(X_img, known_face_locations=X_face_locations)

    # Use the KNN model to find the best matches for the test face
        closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
        are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))] 
     
    #Predict classes and remove classifications that aren't within the threshold
    # return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]
    names = [pred if rec else "unknown" for pred, rec in zip(knn_clf.predict(faces_encodings), are_matches)]
    output = [{'name': x} for x in names]
    return "hii:"
    #return jsonify(names=output)
    # return [pred for pred in knn_clf.predict(faces_encodings]
    # return 'hey'
    



@app.route('/getNoteText',methods=['GET','POST'])
def GetNoteText():
    if request.method == 'POST':
        file = request.files['pic']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        processImage(filename)            

    
   
    else: "ye"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
