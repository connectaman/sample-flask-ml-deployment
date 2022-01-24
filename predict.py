from preprocessing import encoding 
import os
from os import path
import pandas as pd
import numpy as np
import joblib
# Defining the root path of the directory
root = path.dirname(path.abspath(__file__))
# Label Encoder path
label_path = path.join(path.join(root,'artifacts'),'label.pkl')
# Model path
model_path = path.join(path.join(root,'model'),'lr_65_r2.pkl')
# Load my Label Encoder
lb = joblib.load(label_path)
# Load model
lr = joblib.load(model_path)

def predict_insurance(data):
    age = data['age']
    gender = encoding.encode_gender(data['gender'])
    bmi = data['bmi']
    children = data['children']
    smoker = encoding.encode_smoker(data['smoker'])
    region = lb.transform([data['region']]) 
    res = lr.predict([[age,gender,bmi,children,smoker,region]])
    return {"result":res,"model":"lr_65_r2","ver":"v1"}