#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import requests
import json
import csv


# In[2]:


#read data
ima = []
with open("data/clean/Training.csv", "r") as f:
    reader = csv.reader(f)
    ima = next(reader)
    #rest = [row for row in reader]
print(ima)


# In[3]:


df = pd.read_csv('data/clean/Training.csv')

df.head()
X = df.iloc[:, :-1]
y = df['prognosis']


# In[4]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)


# In[5]:


rf_clf = RandomForestClassifier()
rf_clf.fit(X_train, y_train)
a = rf_clf.predict(X_train)
#print(a)
print('yellow')
#print(y_train)
print("Accuracy on split test: ", rf_clf.score(X_test,y_test))


# In[6]:


#testing
df_test = pd.read_csv('data/clean/Testing.csv')
X_acutal_test = df_test.iloc[:, :-1]
y_actual_test = df_test['prognosis']
print("Accuracy on acutal test: ", rf_clf.score(X_acutal_test, y_actual_test))


# In[7]:


symptoms_dict = {}

for index, symptom in enumerate(X):
    symptoms_dict[symptom] = index
symptoms_dict
print(len(symptoms_dict))
np.save('my_file.npy', symptoms_dict)
print('saved') 
input_vector = np.zeros(len(symptoms_dict))


# In[8]:

a = ['cramps','cough'];
a1 = a[0]
#input_vector[[symptoms_dict['cramps'], symptoms_dict['cough']]] = 1
input_vector[[symptoms_dict[str(a[0])], symptoms_dict[str(a[1])]]] = 1
print(len(input_vector))
print(input_vector)


# In[9]:


rf_clf.predict_proba([input_vector])
rf_clf.predict([input_vector])


# In[11]:

	
pickle.dump(rf_clf, open('model1.pkl','wb'))


# In[12]:


model = pickle.load(open('model1.pkl','rb'))
print(rf_clf.predict([input_vector]))
print('so close')
t = rf_clf.predict([input_vector])
print(np.shape(t))
print(len(input_vector))
print('yellow')
print(np.shape([input_vector]))
print('red')
print([input_vector])
# In[ ]:




