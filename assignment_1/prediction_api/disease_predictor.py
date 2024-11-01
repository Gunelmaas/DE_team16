import json
import os

import pandas as pd
from flask import jsonify
import logging
from io import StringIO
import joblib


class DiseasePredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, prediction_input):
        logging.debug(prediction_input)
        if self.model is None:
            try:
                model_repo = os.environ['MODEL_REPO']
                file_path = os.path.join(model_repo, "model.joblib")
                self.model = joblib.load(file_path)
            except KeyError:
                print("MODEL_REPO is undefined")
                self.model = joblib.load('model.joblib')

        df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')
        y_pred = self.model.predict(df)
        status=y_pred[0]
        logging.info(status)
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(status)}), 200
