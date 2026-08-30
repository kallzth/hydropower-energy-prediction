# Hydropower Energy Production Prediction

ML project predicting energy output (MW) of a hydroelectric dam
using Linear Regression and SGD Regression.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![License](https://img.shields.io/badge/License-MIT-green)
![Models](https://img.shields.io/badge/Models-5_Compared-blue)
![Best RMSE](https://img.shields.io/badge/Best_RMSE-5.4019_MW-green)
![Features](https://img.shields.io/badge/Features-8_Input_Variables-orange)

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
| Water Flow Rate      | m3/s   | Strong (positive)✅  |
| Head                 | meters | Strong (positive)✅  |
| Turbine Efficiency   | %      | Moderate             |
| Generator Efficiency | %      | Moderate             |
| Reservoir Level      | meters | Moderate             |
| Gate Opening         | %      | Moderate             |
| Ambient Temperature  | deg C  | Weak ⚠️              |
| Barometric Pressure  | mbar   | Weak ⚠️              |

## Results — Model Comparison Dashboard

| Model                    | MSE     | RMSE   | MAE    |
|--------------------------|---------|--------|--------|
| Linear Regression        | 29.1804 | 5.4019 | 4.3072 |
| SGD Regression (lr=0.01) | 29.3928 | 5.4215 | 4.3297 |
| Ridge Regression         | 29.1805 | 5.4019 | 4.3072 |
| Random Forest            | 50.7753 | 7.1257 | 5.6722 |
| Gradient Boosting        | 41.5143 | 6.4432 | 5.2002 |
| XGBoost                  | 48.5983 | 6.9712 | 5.5141 |

**Winner:** Linear Regression with RMSE = 5.4019 MW
**Improvement over baseline:** X.X% reduction in RMSE vs Linear Regression


## Key Findings
- Water Flow Rate: strongest predictor of energy output
- Ambient Temperature: weakest correlation (confirms EDA)
- SGD learning rate 0.01 achieved best performance
- Residual analysis confirmed no systematic model bias
- Ensemble models (Random Forest, Gradient Boosting, XGBoost) outperform linear models by capturing non-linear feature interactions
- Feature importance from Random Forest independently validates EDA correlation findings


## Tech Stack
Python · NumPy · Pandas · Matplotlib · Seaborn · Scikit-learn

## How to Run
1. Clone this repo
2. pip install -r requirements.txt
3. Add your dataset to data/hydropower_data.xlsx
4. Open hydropower_energy_prediction.ipynb in Jupyter
5. Run all cells top to bottom

---
Author: **Kaleab Zelalem** | github.com/kallzth

Software Engineering Student | Addis Ababa Institute of Technology