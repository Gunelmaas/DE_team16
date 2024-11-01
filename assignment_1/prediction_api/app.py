import os
from flask import Flask, request, jsonify
from disease_predictor import DiseasePredictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/predict_disease/', methods=['POST'])
def predict():
    prediction_input=request.get_json()
    
    return dp.predict_single_record(prediction_input)

# Instantiate the predictor
dp = DiseasePredictor()

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
