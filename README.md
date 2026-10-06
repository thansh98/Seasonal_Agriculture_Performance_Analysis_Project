# Seasonal Agriculture Performance Analysis

### AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026

**Implementation Partner:** BharatCares  
**Trainer:** Mr. Kartik Hooda  
**Duration:** 17 August – 30 September 2026  
**Topic:** Data Analytics with AI: Foundation to Implementation

## Overview

A Python data analytics project that compares agricultural performance across Kharif, Rabi, and Zaid seasons. It combines data cleaning, exploratory visualization, statistical testing, and machine learning to examine crop yield, water use, disease/pest risk, and farm profitability.

The Streamlit dashboard provides interactive filters and a yield/profit simulator using locally saved models. Analysis is based on the CSV files included in this project; the application does not fetch live weather or market data.

## Features

- Filter records by season, state, crop, and irrigation method.
- Compare seasonal climate conditions, crop yields, irrigation efficiency, and farm economics.
- Explore regional performance through interactive Plotly charts.
- Estimate yield and profit for user-entered farm conditions.
- Review answers to 12 agricultural analysis questions.
- Run statistical tests and compare three regression algorithms.
- Regenerate analysis tables, figures, models, and the Jupyter notebook.


## Dataset

| Item | Included data |
|---|---|
| Raw dataset | [seasonal_agriculture_performance_dataset.csv](data/seasonal_agriculture_performance_dataset.csv) |
| Cleaned dataset | [cleaned_seasonal_agriculture_dataset.csv](data/cleaned_seasonal_agriculture_dataset.csv) |
| Records | 4,000 in each dataset |
| Columns | 28 raw; 40 after preprocessing and feature engineering |
| Seasons | Kharif, Rabi, Zaid |
| States | Andhra Pradesh, Gujarat, Karnataka, Madhya Pradesh, Maharashtra, Punjab, Tamil Nadu, Telangana |
| Crops | Chilli, Cotton, Groundnut, Maize, Pulses, Rice, Sugarcane, Wheat |
| Irrigation methods | Drip, Flood, Rainfed, Sprinkler |

Fields cover farm identification, location, climate, soil conditions, nutrients, resource inputs, yield, production, market price, cost, revenue, profit, and disease/pest risk. Monetary values are in INR; yield is in tonnes per hectare; water efficiency is in tonnes per 1,000 m³.

The analysis uses the seasonal agriculture dataset supplied with the project.

## Technologies

| Purpose | Libraries |
|---|---|
| Data processing | pandas, NumPy |
| Statistical analysis | SciPy |
| Machine learning | scikit-learn, joblib |
| Visualization | Matplotlib, Seaborn, Plotly, statsmodels |
| Web dashboard | Streamlit |
| Notebook generation and execution | Jupyter, nbformat, nbclient, ipykernel |


## Project Files

| Path | Purpose |
|---|---|
| `app.py` | Streamlit dashboard and prediction simulator |
| `requirements.txt` | Python dependencies |
| `data/` | Raw/cleaned CSVs and project brief |
| `notebooks/Seasonal_Agriculture_Performance_Analysis.ipynb` | Analysis notebook |
| `src/data_preprocessing.py` | Missing-value handling and derived features |
| `src/statistical_analysis.py` | Hypothesis tests and correlations |
| `src/ml_models.py` | Model training, evaluation, and saving |
| `src/visualization.py` | Analysis figure generation |
| `src/build_jupyter_notebook.py` | Build and execute the notebook |
| `src/generate_docx_report.py` | Word report generation |
| `src/generate_presentation.py` | Template-based presentation generation |
| `reports/figures/` | 10 saved analysis figures |
| `reports/models/` | Yield/profit models and their feature-name files |
| `reports/ml_model_evaluation.csv` | Saved model benchmark results |
| `reports/statistical_anova_tests.csv` | Seasonal statistical test results |
| `reports/statistical_pairwise_tests.csv` | Pairwise test results |
| `reports/statistical_chi2_tests.csv` | Chi-square test results |
| `reports/environmental_outcome_correlations.csv` | Environmental/outcome correlations |
| `reports/yield_feature_importances.csv` | Yield model feature importance |
| `reports/profit_feature_importances.csv` | Profit model feature importance |

## Installation and Run Instructions

Extract the project ZIP and open a terminal inside `seasonal_agriculture_performance_analysis`, where `app.py` and `requirements.txt` are located.

### Windows PowerShell

```powershell
cd seasonal_agriculture_performance_analysis
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install "scikit-learn>=1.4"
python -m streamlit run app.py
```

If PowerShell prevents activation, use the virtual environment directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install "scikit-learn>=1.4"
.\.venv\Scripts\python.exe -m streamlit run app.py
```


Open the local URL printed by Streamlit, normally `http://localhost:8501`. The cleaned CSV and all four model artifacts are included, so preprocessing and training are not required before the first launch. If saved models are incompatible with your installed scikit-learn version, regenerate them using the training command below.

## Dashboard Sections

1. Executive Summary
2. Seasonal Climate Dynamics
3. Water & Irrigation Efficiency
4. Farm Economics & Margins
5. Regional Performance
6. AI Yield & Profit Simulator
7. 12 Key Analytical Questions

The simulator accepts farm, climate, nutrient, irrigation, price, and cost inputs. It predicts yield first, uses predicted production as an input to the profit model, and displays estimated financial outcomes. Its current implementation fixes soil moisture at 25% and disease/pest risk at 45%.

## Reproduce the Analysis

Run these commands from the project root in order:

```bash
python src/data_preprocessing.py
python src/statistical_analysis.py
python src/ml_models.py
python src/visualization.py
```

Preprocessing imputes missing yield using production divided by farm area, missing rainfall using state/season medians, and missing soil moisture using crop/season medians, with seasonal fallback medians. It adds imputation flags, financial ratios, per-hectare measures, water productivity, total NPK, and profitability categories.

Open the included notebook:

```bash
jupyter notebook notebooks/Ansh_Seasonal_Agriculture_Performance_Analysis.ipynb
```

## Dataset Findings

The following seasonal means were checked against the included cleaned dataset:

| Metric | Kharif | Rabi | Zaid |
|---|---:|---:|---:|
| Rainfall (mm) | 852.11 | 435.93 | 299.34 |
| Temperature (°C) | 28.45 | 23.49 | 31.04 |
| Yield (t/ha) | 5.63 | 5.09 | 4.63 |
| Net profit per farm (INR) | 178,914.65 | 87,689.47 | -24,804.82 |
| ROI (%) | 35.45 | 17.60 | -2.47 |

Kharif has the highest average yield and profit in this dataset. Zaid has a negative average profit despite higher temperatures. These comparisons describe the observed records and do not establish that season or irrigation method alone causes the differences.

## Saved Machine Learning Results

The training script uses an 80/20 random train/test split and five-fold shuffled cross-validation, both with random seed 42. Categorical features are one-hot encoded. Three algorithms are evaluated for yield and profit.

Values below come from [ml_model_evaluation.csv](reports/ml_model_evaluation.csv); they are saved results, not a fresh training run.

| Target | Model | Test R² | Test MAE | Test RMSE | Mean CV R² |
|---|---|---:|---:|---:|---:|
| Yield (t/ha) | Random Forest | 0.9628 | 0.7539 | 2.6795 | 0.9616 |
| Yield (t/ha) | Gradient Boosting | 0.9751 | 0.6412 | 2.1903 | 0.9736 |
| Yield (t/ha) | Ridge Regression | 0.8077 | 2.3138 | 6.0898 | 0.8109 |
| Profit (INR) | Random Forest | 0.9733 | 56,816.55 | 86,604.48 | 0.9681 |
| Profit (INR) | Gradient Boosting | 0.9814 | 48,706.73 | 72,192.39 | 0.9787 |
| Profit (INR) | Ridge Regression | 0.6498 | 217,712.26 | 313,447.55 | 0.5985 |

Gradient Boosting has the highest recorded test R² for both targets. Yield uses 19 input fields before encoding; profit additionally uses market price, production, and total cost.

## Interpretation and Limitations

- R² is a regression fit measure, not a percentage prediction accuracy.
- Validation uses random splits, not unseen seasons, future years, or held-out regions.
- Profit evaluation uses recorded production, while the dashboard uses predicted production. Saved profit scores do not measure error across the complete two-stage simulator.
- Production, price, and cost are closely tied to the profit target; high fit should not be treated as proof of reliable pre-season forecasting.
- Missing-value imputation is performed before model splitting, so validation does not isolate preprocessing within each training fold.
- Dashboard answers include prewritten summaries; use the included data and result tables to verify numerical claims.
- The application uses local data and models. Internet access is needed for package installation and the externally hosted sidebar image.
- No license file is included in the archive; no open-source license is asserted here.

## Acknowledgments

Prepared under the AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026, in partnership with BharatCares, with training and mentorship from Mr. Kartik Hooda.
