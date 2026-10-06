"""
Machine Learning Predictive Modeling Module
Seasonal Agriculture Performance Analysis
AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026
Implementation Partner: BharatCares | Trainer: Mr. Kartik Hooda
"""

import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error

def train_and_evaluate_models(df: pd.DataFrame, output_dir: str):
    """
    Trains and evaluates ML models for:
    1. Yield Prediction (Yield_Tonnes_Ha)
    2. Profit Prediction (Profit_INR)
    """
    os.makedirs(output_dir, exist_ok=True)
    models_dir = os.path.join(output_dir, 'models')
    os.makedirs(models_dir, exist_ok=True)

    feature_cols = [
        'State', 'Crop', 'Season', 'Irrigation_Method', 'Farm_Area_Hectares',
        'Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Sunlight_Hours_Day',
        'Soil_pH', 'Soil_Moisture_pct', 'Nitrogen_kg_ha', 'Phosphorus_kg_ha',
        'Potassium_kg_ha', 'Fertilizer_kg_ha', 'Pesticide_Litre_ha',
        'Seed_Quality_Score', 'Water_Used_m3', 'Disease_Pest_Risk_pct'
    ]

    # One-hot encoding
    X_encoded = pd.get_dummies(df[feature_cols], drop_first=True)
    
    # Target 1: Yield
    y_yield = df['Yield_Tonnes_Ha']
    # Target 2: Profit
    y_profit = df['Profit_INR']

    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    results = []

    # Candidates
    algorithms = {
        'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42),
        'Ridge Regression': Ridge(alpha=1.0)
    }

    # --- TASK 1: YIELD PREDICTION ---
    X_train_y, X_test_y, y_train_y, y_test_y = train_test_split(X_encoded, y_yield, test_size=0.2, random_state=42)
    best_yield_model = None
    best_yield_r2 = -float('inf')

    for name, model in algorithms.items():
        model.fit(X_train_y, y_train_y)
        preds = model.predict(X_test_y)
        r2 = r2_score(y_test_y, preds)
        mae = mean_absolute_error(y_test_y, preds)
        rmse = root_mean_squared_error(y_test_y, preds)
        cv_scores = cross_val_score(model, X_encoded, y_yield, cv=kf, scoring='r2')

        results.append({
            'Target': 'Yield_Tonnes_Ha',
            'Model': name,
            'Test_R2': round(r2, 4),
            'Test_MAE': round(mae, 4),
            'Test_RMSE': round(rmse, 4),
            'CV_R2_Mean': round(cv_scores.mean(), 4),
            'CV_R2_Std': round(cv_scores.std(), 4)
        })

        if r2 > best_yield_r2:
            best_yield_r2 = r2
            best_yield_model = model

    # Save best yield model
    joblib.dump(best_yield_model, os.path.join(models_dir, 'best_yield_model.pkl'))

    # Extract Yield Feature Importance
    if hasattr(best_yield_model, 'feature_importances_'):
        yield_imp = pd.Series(best_yield_model.feature_importances_, index=X_encoded.columns).sort_values(ascending=False)
        yield_imp_df = pd.DataFrame({'Feature': yield_imp.index, 'Importance': yield_imp.values})
        yield_imp_df.to_csv(os.path.join(output_dir, 'yield_feature_importances.csv'), index=False)

    # --- TASK 2: PROFIT PREDICTION ---
    # Also include Market_Price_INR_Tonne, Production_Tonnes, Total_Cost_INR for financial predictor
    feature_cols_profit = feature_cols + ['Market_Price_INR_Tonne', 'Production_Tonnes', 'Total_Cost_INR']
    X_enc_profit = pd.get_dummies(df[feature_cols_profit], drop_first=True)

    X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_enc_profit, y_profit, test_size=0.2, random_state=42)
    best_profit_model = None
    best_profit_r2 = -float('inf')

    for name, model in algorithms.items():
        model.fit(X_train_p, y_train_p)
        preds = model.predict(X_test_p)
        r2 = r2_score(y_test_p, preds)
        mae = mean_absolute_error(y_test_p, preds)
        rmse = root_mean_squared_error(y_test_p, preds)
        cv_scores = cross_val_score(model, X_enc_profit, y_profit, cv=kf, scoring='r2')

        results.append({
            'Target': 'Profit_INR',
            'Model': name,
            'Test_R2': round(r2, 4),
            'Test_MAE': round(mae, 2),
            'Test_RMSE': round(rmse, 2),
            'CV_R2_Mean': round(cv_scores.mean(), 4),
            'CV_R2_Std': round(cv_scores.std(), 4)
        })

        if r2 > best_profit_r2:
            best_profit_r2 = r2
            best_profit_model = model

    joblib.dump(best_profit_model, os.path.join(models_dir, 'best_profit_model.pkl'))

    # Save feature names for inference
    joblib.dump(list(X_encoded.columns), os.path.join(models_dir, 'yield_feature_names.pkl'))
    joblib.dump(list(X_enc_profit.columns), os.path.join(models_dir, 'profit_feature_names.pkl'))

    # Extract Profit Feature Importance
    if hasattr(best_profit_model, 'feature_importances_'):
        profit_imp = pd.Series(best_profit_model.feature_importances_, index=X_enc_profit.columns).sort_values(ascending=False)
        profit_imp_df = pd.DataFrame({'Feature': profit_imp.index, 'Importance': profit_imp.values})
        profit_imp_df.to_csv(os.path.join(output_dir, 'profit_feature_importances.csv'), index=False)

    results_df = pd.DataFrame(results)
    results_df.to_csv(os.path.join(output_dir, 'ml_model_evaluation.csv'), index=False)

    return results_df, yield_imp_df, profit_imp_df

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'cleaned_seasonal_agriculture_dataset.csv')
    reports_dir = os.path.join(base_dir, 'reports')

    df = pd.read_csv(data_path)
    results_df, yield_imp_df, profit_imp_df = train_and_evaluate_models(df, reports_dir)

    print("=== MACHINE LEARNING MODEL PERFORMANCE ===")
    print(results_df.to_string(index=False))

    print("\n=== TOP 10 FEATURES FOR CROP YIELD ===")
    print(yield_imp_df.head(10).to_string(index=False))

    print("\n=== TOP 10 FEATURES FOR ECONOMIC PROFIT ===")
    print(profit_imp_df.head(10).to_string(index=False))

if __name__ == '__main__':
    main()
