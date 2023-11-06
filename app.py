from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import pickle
import pandas as pd
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

api = Api(app)

sickness = joblib.load('C:/Users/Steve/Documents/ml-oral-exam/backend-predict/sickness.pkl')
dangerous = joblib.load('dangerous.pkl')

@app.route('/')
def get():
    return("Hello World")

@app.route('/disease')
def get():
    try:
        data = request.get_json()
        print(data)
        return jsonify({"message": "JSON array successfully received and processed"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    url_params = request.args
    animalname = url_params['ani']
    symptom1 = url_params['s1']
    try:
        symptom2 = url_params['s2']
    except KeyError:
        symptom2 = ""
    try:
        symptom3 = url_params['s3']
    except KeyError:
        symptom3 = ""
    try:
        symptom4 = url_params['s4']
    except KeyError:
        symptom4 = ""
    try:
        symptom5 = url_params['d5']
    except KeyError:
        symptom5 = ""

    df = pd.DataFrame([[animalname,symptom1,symptom2,symptom3,symptom4,symptom5]],columns=['AnimalName','symptoms1','symptoms2','symptoms3','symptoms4','symptoms5'])
    
    prediction = pipe.predict(df)
    print(prediction[0])
    return str(prediction[0])



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
