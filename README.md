# Seasonal Agriculture Performance Analysis
### AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026
**Implementation Partner:** BharatCares | **Trainer:** Mr. Kartik Hooda  
**Duration:** 6 Weeks (17th August – 30th September 2026) | **Topic:** Data Analytics with AI: Foundation to Implementation

![Project Status](https://img.shields.io/badge/Project-Completed-success)
![Python Version](https://img.shields.io/badge/Python-3.12-blue)
![Machine Learning](https://img.shields.io/badge/ML-Gradient%20Boosting%20%7C%20Random%20Forest-green)
![Streamlit App](https://img.shields.io/badge/Web%20App-Streamlit%201.38-red)
![Partner](https://img.shields.io/badge/Partner-BharatCares%20%7C%20IBM%20SkillsBuild-blueviolet)

---
git add .

---

## 🔗 Dataset Information & Links
* **Dataset Name:** Multi-State Seasonal Agriculture Performance Dataset
* **Local Repository Path:** [`data/seasonal_agriculture_performance_dataset.csv`](file:///C:/Users/anshp/.gemini/antigravity/scratch/seasonal_agriculture_performance_analysis/data/seasonal_agriculture_performance_dataset.csv)
* **Processed Dataset Path:** [`data/cleaned_seasonal_agriculture_dataset.csv`](file:///C:/Users/anshp/.gemini/antigravity/scratch/seasonal_agriculture_performance_analysis/data/cleaned_seasonal_agriculture_dataset.csv)
* **Scope:** 4,000 Farm Observations across 8 States (Andhra Pradesh, Gujarat, Karnataka, Madhya Pradesh, Maharashtra, Punjab, Tamil Nadu, Telangana)
* **Crops Tracked:** Chilli, Cotton, Groundnut, Maize, Pulses, Rice, Sugarcane, Wheat
* **Attributes:** 28 Parameters covering Environmental conditions, Soil chemistry, Irrigation methods, Resource inputs, Production yields, and Farm economics.

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.12
* **Data Processing & Feature Engineering:** `pandas` (v2.2+), `numpy` (v1.24+)
* **Inferential Statistics & Hypothesis Testing:** `scipy.stats` (One-Way ANOVA, Kruskal-Wallis H, Mann-Whitney U, Chi-Square)
* **Machine Learning & Predictive Analytics:** `scikit-learn` (Gradient Boosting Regressor, Random Forest Regressor, Ridge Regression, K-Fold Cross Validation)
* **Data Visualization:** `matplotlib`, `seaborn`, `plotly.express` (interactive visual analytics)
* **Statistical Modeling & Trendlines:** `statsmodels` (OLS regression trendlines)
* **Interactive Decision Web App:** `streamlit` (v1.38+)
* **Documentation & Automation:** `python-docx` (Word doc generation), `python-pptx` (PowerPoint automation), `jupyter`, `nbformat`, `nbclient`

---

## 📌 Project Overview

```
seasonal_agriculture_performance_analysis/
│
├── data/                                     
│   ├── seasonal_agriculture_performance_dataset.csv     
│   ├── cleaned_seasonal_agriculture_dataset.csv        
│   ├── Major_Project_Requirements.pdf                   
│     
│
├── notebooks/                               
│   └── Seasonal_Agriculture_Performance_Analysis.ipynb 
│
├── reports/                                
│   ├── figures/                               
│   │   ├── seasonal_distributions.png        
│   │   ├── yield_by_crop_season.png          
│   │   ├── irrigation_efficiency.png          
│   │   ├── economic_performance.png           
│   │   ├── crop_profitability_matrix.png      
│   │   ├── disease_pest_risk.png             
│   │   ├── correlation_heatmap.png            
│   │   ├── state_seasonal_disparity.png       
│   │   ├── feature_importance.png          
│   │   └── key_questions_summary.png         
│   ├── models/                                
│   │   ├── best_yield_model.pkl               
│   │   └── best_profit_model.pkl           
│   ├── statistical_anova_tests.csv           
│   ├── statistical_pairwise_tests.csv     
│   └── ml_model_evaluation.csv               
│
├── src/                                
│   ├── data_preprocessing.py               
│   ├── statistical_analysis.py           
│   ├── ml_models.py                           
│   ├── visualization.py                      
│   ├── generate_presentation.py              
│   └── build_jupyter_notebook.py            
│
├── app.py                                                        
├── requirements.txt                           
└── README.md                                  
```

---

## 🔍 Key Findings Summary

| Metric | Kharif (Monsoon) | Rabi (Winter) | Zaid (Summer) | Statistical Test & Significance |
|---|---|---|---|---|
| **Rainfall (mm)** | **852.1 mm** | 435.9 mm | 299.3 mm | ANOVA $F = 3,448$, $p < 10^{-300}$ (Significant) |
| **Average Temperature** | 28.5°C | **23.5°C** | 31.0°C | ANOVA $F = 2,678$, $p < 10^{-300}$ (Significant) |
| **Relative Humidity** | **71.8%** | 57.9% | 52.0% | ANOVA $F = 1,574$, $p < 10^{-300}$ (Significant) |
| **Average Yield (t/ha)**| **5.63 t/ha** | 5.09 t/ha | 4.63 t/ha | Kruskal-Wallis $H = 70.59$, $p = 4.69 \times 10^{-16}$ |
| **Water Efficiency** | **5.89 t/km³** | 5.19 t/km³ | 4.41 t/km³ | Kruskal-Wallis $H = 56.81$, $p = 4.61 \times 10^{-13}$ |
| **Disease/Pest Risk** | **54.5%** | 40.5% | 38.2% | Kruskal-Wallis $H = 1,430$, $p < 10^{-300}$ |
| **Gross Revenue** | **₹710,719** | ₹601,526 | ₹519,172 | ANOVA $F = 24.89$, $p = 1.81 \times 10^{-11}$ |
| **Net Farm Profit** | **+₹178,915** | **+₹87,689** | **-₹24,805** | Kruskal-Wallis $H = 101.9$, $p = 7.36 \times 10^{-23}$ |
| **Mean ROI (%)** | **35.5%** | 17.6% | **-2.5%** | Kruskal-Wallis $H = 98.06$, $p = 5.08 \times 10^{-22}$ |

### 💡 Core Takeaways
1. **The Summer (Zaid) Deficit:** Zaid crops suffer from net negative average profit (**-₹24,805**) and an average ROI of **-2.5%**. Over 54% of farms in summer lose money due to high evaporation, severe water pumping costs (6,420 m³), and reduced yields under traditional flood irrigation.
2. **Micro-Irrigation Reversal:** Transitioning from Flood irrigation to **Drip irrigation** turns summer losses (-₹69,787) into positive earnings (+₹21,291) while boosting water efficiency from 3.8 to 6.2 t / 1000 m³.
3. **Pest Surge in Monsoon:** High humidity and monsoon rains trigger pest vulnerability of 54.5% in Kharif, requiring proactive pest protection.

---

## 🤖 Machine Learning Performance

| Prediction Task | Algorithm | Test $R^2$ | Test MAE | Test RMSE | 5-Fold CV $R^2$ |
|---|---|---|---|---|---|
| **Crop Yield (t/ha)** | **Gradient Boosting** | **0.9751** | **0.6412** | **2.1903** | **0.9736** |
| Crop Yield (t/ha) | Random Forest | 0.9628 | 0.7539 | 2.6795 | 0.9616 |
| Crop Yield (t/ha) | Ridge Regression | 0.8077 | 2.3138 | 6.0898 | 0.8109 |
| **Net Profit (INR)** | **Gradient Boosting** | **0.9814** | **₹48,707** | **₹72,192** | **0.9787** |
| Net Profit (INR) | Random Forest | 0.9733 | ₹56,817 | ₹86,604 | 0.9681 |
| Net Profit (INR) | Ridge Regression | 0.6498 | ₹217,712| ₹313,448| 0.5985 |

---


## 📜 Acknowledgments & Program Citation
Developed under the **AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026** (17th August to 30th September 2026), conducted in partnership with **BharatCares**, under the training and mentorship of **Mr. Kartik Hooda** (*Focus Topic: Data Analytics with AI: Foundation to Implementation*).
