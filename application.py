from flask import Flask, request, render_template
from flask_cors import CORS,cross_origin

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

@app.route('/')
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CustomData(
            carat = float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )

        pred_df = data.get_data_as_dataframe()

        print(pred_df)

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)
        results = round(pred[0],2)
        return render_template('index.html',results=results)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000,debug=True)