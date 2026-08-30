# ============================================================
# app.py — Hydropower Energy Prediction Flask API
# Author: Kaleab Zelalem
# ============================================================

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# —— Load model and scaler at startup —————————————————————————
MODEL_PATH    = os.path.join('models', 'best_model.pkl')
SCALER_PATH   = os.path.join('models', 'scaler.pkl')
FEATURES_PATH = os.path.join('models', 'feature_names.pkl')

model    = joblib.load(MODEL_PATH)
scaler   = joblib.load(SCALER_PATH)
features = joblib.load(FEATURES_PATH)

print(f'Model loaded: {type(model).__name__}')
print(f'Features:     {features}')


# —— Route 1: HTML Form ——————————————————————————————
@app.route('/')
def home():
    return render_template('index.html', features=features)


# —— Route 2: JSON Prediction Endpoint ———————————————————
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Accept both JSON and form submissions
        if request.is_json:
            data = request.get_json()
            input_values = [float(data[f]) for f in features]
        else:
            input_values = [float(request.form[f]) for f in features]

        # Validate input length
        #if len(input_values) != len(features):
            #return jsonify({'error': f'Expected {len(features)} features'}), 400

        # Preprocess: scale the input
        X = np.array(input_values).reshape(1, -1)
        # X_scaled = scaler.transform(X)

        # Predict
        # prediction = model.predict(X_scaled)[0]
        #prediction = round(float(prediction), 2)
        prediction = round(float(model.predict(X)[0]), 2)
        # Return result
        if request.is_json:
            return jsonify({
                'predicted_energy_mw': prediction,
                'model_used': type(model).__name__,
                'inputs': dict(zip(features, input_values))
            })
        else:
            # Form submission — redirect back with result
            return render_template('index.html',
                                   features=features,
                                   prediction=prediction,
                                   inputs=dict(zip(features, input_values)))

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# —— Route 3: Health Check ————————————————————————————
@app.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'model':  type(model).__name__,
        'features': features
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


    