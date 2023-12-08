from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import pandas as pd
from IOT_NIDS.pipeline.predictions import Pred
from sklearn.preprocessing import MinMaxScaler

app= Flask(__name__)


@app.route('/',methods=['GET'])
def homePage():
    return render_template("index2.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    upload_dir = 'uploaded files/'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
        
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    # You can now pass the file to your prediction function
    obj = Pred()
    prediction_result=obj.predictionPipeline(file_path)
    return  jsonify({'result': prediction_result[0]})

if __name__ == '__main__':
    app.run(debug=True)
