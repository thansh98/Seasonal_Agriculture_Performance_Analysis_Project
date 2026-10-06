# Seasonal Agriculture Performance Analysis

### AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026

**Implementation Partner:** BharatCares  
**Trainer:** Mr. Kartik Hooda  
**Duration:** 17 August – 30 September 2026  
**Topic:** Data Analytics with AI: Foundation to Implementation

## Overview

A Python data analytics project that compares agricultural performance across Kharif, Rabi, and Zaid seasons. The workflow combines data preprocessing, exploratory visualization, statistical testing, and regression modeling to examine crop yield, resource efficiency, disease and pest risk, and farm profitability.

An interactive Streamlit dashboard supports record filtering, regional comparisons, and yield and profit estimation using locally saved models. The application uses the CSV dataset included in this repository and does not fetch live weather or market data.

## Features

- Filter records by season, state, crop, and irrigation method.
- Compare climate conditions, crop yields, resource use, and farm economics.
- Explore regional performance through interactive Plotly charts.
- Estimate yield and profit for user-entered farm conditions.
- Review summaries addressing 12 agricultural analysis questions.
- Perform statistical tests and compare three regression algorithms.
- Regenerate analysis tables, figures, models, notebooks, and reports.

## Dataset

| Item | Description |
|---|---|
| Raw dataset | [seasonal_agriculture_performance_dataset.csv](data/seasonal_agriculture_performance_dataset.csv) |
| Cleaned dataset | [cleaned_seasonal_agriculture_dataset.csv](data/cleaned_seasonal_agriculture_dataset.csv) |
| Records | 4,000 in each dataset |
| Columns | 28 raw; 40 after preprocessing and feature engineering |
| Seasons | Kharif, Rabi, Zaid |
| States | Andhra Pradesh, Gujarat, Karnataka, Madhya Pradesh, Maharashtra, Punjab, Tamil Nadu, Telangana |
| Crops | Chilli, Cotton, Groundnut, Maize, Pulses, Rice, Sugarcane, Wheat |
| Irrigation methods | Drip, Flood, Rainfed, Sprinkler |

The dataset covers farm identification, location, climate, soil conditions, nutrients, resource inputs, yield, production, market price, cost, revenue, profit, and disease/pest risk. Monetary values are expressed in INR, yield in tonnes per hectare, and water efficiency in tonnes per 1,000 m³.

## Technology Stack

| Purpose | Libraries |
|---|---|
| Data processing | pandas, NumPy |
| Statistical analysis | SciPy |
| Machine learning | scikit-learn, joblib |
| Visualization | Matplotlib, Seaborn, Plotly, statsmodels |
| Dashboard | Streamlit |
| Notebook generation and execution | Jupyter, nbformat, nbclient, ipykernel |

## Project Structure

| Path | Purpose |
|---|---|
| `app.py` | Streamlit dashboard and prediction simulator |
| `requirements.txt` | Python dependencies |
| `data/` | Raw and cleaned datasets and project brief |
| `notebooks/` | Analysis notebook |
| `src/data_preprocessing.py` | Missing-value handling and feature engineering |
| `src/statistical_analysis.py` | Hypothesis tests and correlations |
| `src/ml_models.py` | Model training, evaluation, and persistence |
| `src/visualization.py` | Analysis figure generation |
| `src/build_jupyter_notebook.py` | Notebook generation and execution |
| `src/generate_docx_report.py` | Word report generation |
| `src/generate_presentation.py` | Template-based presentation generation |
| `reports/figures/` | Saved analysis figures |
| `reports/models/` | Saved models and feature-name files |
| `reports/ml_model_evaluation.csv` | Model benchmark results |
| `reports/statistical_anova_tests.csv` | Seasonal ANOVA results |
| `reports/statistical_pairwise_tests.csv` | Pairwise test results |
| `reports/statistical_chi2_tests.csv` | Chi-square test results |
| `reports/environmental_outcome_correlations.csv` | Environmental and outcome correlations |
| `reports/yield_feature_importances.csv` | Yield model feature importance |
| `reports/profit_feature_importances.csv` | Profit model feature importance |

## Installation and Launch

Extract the project ZIP, then open a terminal in the `seasonal_agriculture_performance_analysis` folder containing `app.py` and `requirements.txt`.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If virtual environment activation is blocked, run its Python executable directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local URL printed by Streamlit, normally [http://localhost:8501](http://localhost:8501).

The cleaned dataset and saved model artifacts are included for the first launch. If a saved model cannot be loaded because of scikit-learn version incompatibility, use the original training environment or retrain the models with the installed dependencies using the commands below.

## Dashboard Sections

1. Executive Summary
2. Seasonal Climate Dynamics
3. Water & Irrigation Efficiency
4. Farm Economics & Margins
5. Regional Performance
6. AI Yield & Profit Simulator
7. 12 Key Analytical Questions

The simulator accepts farm, climate, nutrient, irrigation, price, and cost inputs. It predicts yield, derives production, and passes predicted production to the profit model. The current implementation fixes soil moisture at 25% and disease/pest risk at 45%.

## Reproduce the Analysis

Run the following commands from the project root in order:

```bash
python src/data_preprocessing.py
python src/statistical_analysis.py
python src/ml_models.py
python src/visualization.py
```

Preprocessing estimates missing yield from production divided by farm area. Missing rainfall is filled using state/season medians, and missing soil moisture using crop/season medians, with seasonal fallback medians. Derived fields include imputation flags, financial ratios, per-hectare measures, water productivity, total NPK, and profitability categories.

To browse and open the included notebook:

```bash
jupyter notebook notebooks
```

To rebuild and execute the notebook:

```bash
python src/build_jupyter_notebook.py
```

After generating figures, create the Word report:

```bash
python src/generate_docx_report.py
```

These scripts overwrite their corresponding generated outputs. Back up any manually edited generated files before running them.

## Seasonal Findings

The following values summarize seasonal means reported for the included cleaned dataset:

| Metric | Kharif | Rabi | Zaid |
|---|---:|---:|---:|
| Rainfall (mm) | 852.11 | 435.93 | 299.34 |
| Temperature (°C) | 28.45 | 23.49 | 31.04 |
| Yield (t/ha) | 5.63 | 5.09 | 4.63 |
| Net profit per farm (INR) | 178,914.65 | 87,689.47 | -24,804.82 |
| ROI (%) | 35.45 | 17.60 | -2.47 |

Kharif records the highest average yield and profit in this dataset. Zaid records negative average profit. These comparisons describe the included observations and do not establish that season or irrigation method alone causes the differences.

## Machine Learning Results

Model evaluation uses an 80/20 random train/test split and five-fold shuffled cross-validation with random seed 42. Categorical variables are one-hot encoded.

The following saved results are reported in [ml_model_evaluation.csv](reports/ml_model_evaluation.csv):

| Target | Model | Test R² | Test MAE | Test RMSE | Mean CV R² |
|---|---|---:|---:|---:|---:|
| Yield (t/ha) | Random Forest | 0.9628 | 0.7539 | 2.6795 | 0.9616 |
| Yield (t/ha) | Gradient Boosting | 0.9751 | 0.6412 | 2.1903 | 0.9736 |
| Yield (t/ha) | Ridge Regression | 0.8077 | 2.3138 | 6.0898 | 0.8109 |
| Profit (INR) | Random Forest | 0.9733 | 56,816.55 | 86,604.48 | 0.9681 |
| Profit (INR) | Gradient Boosting | 0.9814 | 48,706.73 | 72,192.39 | 0.9787 |
| Profit (INR) | Ridge Regression | 0.6498 | 217,712.26 | 313,447.55 | 0.5985 |

Gradient Boosting achieves the highest recorded test R² for both targets. The yield model uses 19 input fields before encoding; the profit model additionally uses market price, production, and total cost. MAE and RMSE use the corresponding target units.

## Interpretation and Limitations

- R² measures regression fit; it is not a percentage prediction accuracy.
- Random-split validation does not demonstrate performance on future years or held-out regions.
- Profit evaluation uses recorded production, while the dashboard uses predicted production. Saved profit scores therefore do not quantify the complete two-stage simulator's error.
- Production, price, and cost are closely related to profit. High model fit does not establish reliable pre-season forecasting.
- Missing-value imputation occurs before model splitting, so validation does not isolate preprocessing within each training fold.
- Dashboard answers include prewritten summaries. Numerical claims should be checked against the included dataset and output tables.
- The application uses local data and models. Package installation and the externally hosted sidebar image require internet access.
- No open-source license is asserted unless a license file is added by the project owner.

## Acknowledgments

Prepared under the AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026, in partnership with BharatCares, with training and mentorship from Mr. Kartik Hooda.
