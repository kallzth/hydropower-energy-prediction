# Hydropower Energy Production Prediction

ML project predicting energy output (MW) of a hydroelectric dam
using Linear Regression and SGD Regression.

## Project Overview

Hydroelectric power is a clean, renewable energy source. Accurate
prediction of energy output enables better grid management and
operational planning. This project builds and evaluates a
regression model trained on 8 physical dam parameters.

## Dataset

Source: UCI Machine Learning Repository
Features: 8 input variables | Target: Energy Production (MW)

| Feature              | Unit   | Correlation Strength |
|----------------------|--------|----------------------|
| Water Flow Rate      | m3/s   | Strong (positive)    |
| Head                 | meters | Strong (positive)    |
| Turbine Efficiency   | %      | Moderate             |
| Generator Efficiency | %      | Moderate             |
| Reservoir Level      | meters | Moderate             |
| Gate Opening         | %      | Moderate             |
| Ambient Temperature  | deg C  | Weak                 |
| Barometric Pressure  | mbar   | Weak                 |

## Results

| Model                    | MSE     | RMSE   | MAE    |
|--------------------------|---------|--------|--------|
| Linear Regression        | 29.1804 | 5.4019 | 4.3072 |
| SGD Regression (lr=0.01) | 29.3928 | 5.4215 | 4.3297 |

## Key Findings
- Water Flow Rate: strongest predictor of energy output
- Ambient Temperature: weakest correlation
- SGD learning rate 0.01 achieved best performance
- Residual analysis confirmed no systematic model bias

## Tech Stack
Python · NumPy · Pandas · Matplotlib · Seaborn · Scikit-learn

## How to Run
1. Clone this repo
2. pip install -r requirements.txt
3. Add your dataset to data/hydropower_data.xlsx
4. Open hydropower_energy_prediction.ipynb in Jupyter
5. Run all cells top to bottom

---
Author: Kaleab Zelalem | github.com/kallzth