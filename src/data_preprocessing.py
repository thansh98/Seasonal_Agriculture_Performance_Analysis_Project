"""
Data Preprocessing and Feature Engineering Module
Seasonal Agriculture Performance Analysis
AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026
Implementation Partner: BharatCares | Trainer: Mr. Kartik Hooda
"""

import os
import pandas as pd
import numpy as np

def load_data(raw_data_path: str) -> pd.DataFrame:
    """Loads raw dataset from CSV file."""
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"File not found: {raw_data_path}")
    df = pd.read_csv(raw_data_path)
    print(f"[INFO] Loaded dataset with shape: {df.shape}")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw dataset:
    - Missing value imputation using domain and statistical logic
    - Yield_Tonnes_Ha = Production_Tonnes / Farm_Area_Hectares
    - Rainfall_mm = State & Season median
    - Soil_Moisture_pct = Crop & Season median
    """
    df_clean = df.copy()

    # Track missing values before imputation
    missing_before = df_clean.isnull().sum()
    print("[INFO] Missing values before cleaning:\n", missing_before[missing_before > 0])

    # 1. Yield_Tonnes_Ha: Exactly Production_Tonnes / Farm_Area_Hectares
    mask_yield_nan = df_clean['Yield_Tonnes_Ha'].isnull()
    df_clean['Yield_Imputed_Flag'] = mask_yield_nan.astype(int)
    df_clean.loc[mask_yield_nan, 'Yield_Tonnes_Ha'] = (
        df_clean.loc[mask_yield_nan, 'Production_Tonnes'] / df_clean.loc[mask_yield_nan, 'Farm_Area_Hectares']
    ).round(2)

    # 2. Rainfall_mm: State + Season median
    mask_rain_nan = df_clean['Rainfall_mm'].isnull()
    df_clean['Rainfall_Imputed_Flag'] = mask_rain_nan.astype(int)
    state_season_rain = df_clean.groupby(['State', 'Season'])['Rainfall_mm'].transform('median')
    df_clean['Rainfall_mm'] = df_clean['Rainfall_mm'].fillna(state_season_rain)
    # If any still missing, use season median
    df_clean['Rainfall_mm'] = df_clean['Rainfall_mm'].fillna(df_clean.groupby('Season')['Rainfall_mm'].transform('median'))

    # 3. Soil_Moisture_pct: Crop + Season median
    mask_moist_nan = df_clean['Soil_Moisture_pct'].isnull()
    df_clean['Soil_Moisture_Imputed_Flag'] = mask_moist_nan.astype(int)
    crop_season_moist = df_clean.groupby(['Crop', 'Season'])['Soil_Moisture_pct'].transform('median')
    df_clean['Soil_Moisture_pct'] = df_clean['Soil_Moisture_pct'].fillna(crop_season_moist)
    # If any still missing, use season median
    df_clean['Soil_Moisture_pct'] = df_clean['Soil_Moisture_pct'].fillna(df_clean.groupby('Season')['Soil_Moisture_pct'].transform('median'))

    # Recheck nulls
    remaining_nulls = df_clean.isnull().sum().sum()
    print(f"[INFO] Remaining null values after cleaning: {remaining_nulls}")
    return df_clean

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates domain-specific agricultural and financial features:
    - Financial margins (Profit Margin %, Return on Investment ROI %)
    - Per-hectare metrics (Cost/Ha, Revenue/Ha, Profit/Ha, Water/Ha)
    - Resource & Nutrient balances (NPK Total, NPK ratios)
    - Profitability tiers and categories
    """
    df_feat = df.copy()

    # Economic metrics
    # Avoid division by zero
    df_feat['Profit_Margin_pct'] = np.where(
        df_feat['Revenue_INR'] > 0,
        (df_feat['Profit_INR'] / df_feat['Revenue_INR']) * 100,
        -100.0
    ).round(2)

    df_feat['ROI_pct'] = np.where(
        df_feat['Total_Cost_INR'] > 0,
        (df_feat['Profit_INR'] / df_feat['Total_Cost_INR']) * 100,
        0.0
    ).round(2)

    # Per-hectare normalizations
    df_feat['Cost_Per_Ha_INR'] = (df_feat['Total_Cost_INR'] / df_feat['Farm_Area_Hectares']).round(2)
    df_feat['Revenue_Per_Ha_INR'] = (df_feat['Revenue_INR'] / df_feat['Farm_Area_Hectares']).round(2)
    df_feat['Profit_Per_Ha_INR'] = (df_feat['Profit_INR'] / df_feat['Farm_Area_Hectares']).round(2)
    df_feat['Water_Per_Ha_m3'] = (df_feat['Water_Used_m3'] / df_feat['Farm_Area_Hectares']).round(2)

    # Water economic productivity (INR Revenue generated per m3 water)
    df_feat['Water_Productivity_INR_m3'] = np.where(
        df_feat['Water_Used_m3'] > 0,
        (df_feat['Revenue_INR'] / df_feat['Water_Used_m3']).round(2),
        0.0
    )

    # Soil Nutrients Total
    df_feat['NPK_Total_kg_ha'] = (df_feat['Nitrogen_kg_ha'] + df_feat['Phosphorus_kg_ha'] + df_feat['Potassium_kg_ha']).round(2)

    # Profitability Category
    conditions = [
        df_feat['Profit_INR'] > 100000,
        (df_feat['Profit_INR'] >= 0) & (df_feat['Profit_INR'] <= 100000),
        df_feat['Profit_INR'] < 0
    ]
    labels = ['High Profit (>100k)', 'Moderate Profit (0-100k)', 'Loss Making (<0)']
    df_feat['Profitability_Category'] = np.select(conditions, labels, default='Moderate Profit (0-100k)')

    print(f"[INFO] Features engineered successfully. New shape: {df_feat.shape}")
    return df_feat

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, 'data', 'seasonal_agriculture_performance_dataset.csv')
    processed_path = os.path.join(base_dir, 'data', 'cleaned_seasonal_agriculture_dataset.csv')

    df_raw = load_data(raw_path)
    df_cleaned = clean_data(df_raw)
    df_processed = engineer_features(df_cleaned)

    df_processed.to_csv(processed_path, index=False)
    print(f"[SUCCESS] Cleaned dataset saved to: {processed_path}")

if __name__ == '__main__':
    main()
