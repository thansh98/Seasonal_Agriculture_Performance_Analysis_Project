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

---

## 🎯 Official Internship Submission Deliverables

| Deliverable Type | Required Filename | Generated File in Repository | Format | Status |
|---|---|---|:---:|:---:|
| **Code File** | `YourName_ProjectName.ipynb` | [`YourName_ProjectName.ipynb`](file:///C:/Users/anshp/.gemini/antigravity/scratch/seasonal_agriculture_performance_analysis/YourName_ProjectName.ipynb) / [`Ansh_Seasonal_Agriculture_Performance_Analysis.ipynb`](file:///C:/Users/anshp/.gemini/antigravity/scratch/seasonal_agriculture_performance_analysis/Ansh_Seasonal_Agriculture_Performance_Analysis.ipynb) | `.ipynb` / `.py` | ✅ Ready (1.7 MB, Full Outputs) |
| **Requirements File** | `requirements.txt` | [`requirements.txt`](file:///C:/Users/anshp/.gemini/antigravity/scratch/seasonal_agriculture_performance_analysis/requirements.txt) | `.txt` | ✅ Ready (All dependencies) |
| **Project Report** | `YourName_ProjectReport.docx` | [`YourName_ProjectReport.docx`](file:///C:/Users/anshp/.gemini/antigravity/scratch/seasonal_agriculture_performance_analysis/YourName_ProjectReport.docx) / [`Ansh_ProjectReport.docx`](file:///C:/Users/anshp/.gemini/antigravity/scratch/seasonal_agriculture_performance_analysis/Ansh_ProjectReport.docx) | `.docx` | ✅ Ready (Formal Word Doc) |
| **README File** | `README.md` | [`README.md`](file:///C:/Users/anshp/.gemini/antigravity/scratch/seasonal_agriculture_performance_analysis/README.md) | `.md` | ✅ Ready |

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
├── data/                                      # Datasets and submission templates
│   ├── seasonal_agriculture_performance_dataset.csv     # Raw dataset (4,000 farms)
│   ├── cleaned_seasonal_agriculture_dataset.csv          # Cleaned & feature-engineered dataset
│   ├── Major_Project_Requirements.pdf                    # Official project prompt
│   └── Major_Project_PPT_Submission_Template.pptx        # Official presentation template
│
├── notebooks/                                 # Jupyter Notebooks
│   └── Seasonal_Agriculture_Performance_Analysis.ipynb # Complete executed analysis notebook (1.7 MB)
│
├── reports/                                   # Project outputs, figures, and models
│   ├── figures/                               # 10 High-resolution 300 DPI figures
│   │   ├── seasonal_distributions.png         # Rainfall, Temperature, Humidity, Sunlight distributions
│   │   ├── yield_by_crop_season.png           # Mean crop yield across seasons
│   │   ├── irrigation_efficiency.png          # Drip vs Flood vs Sprinkler vs Rainfed analysis
│   │   ├── economic_performance.png           # Revenue, Cost, and Profit distributions
│   │   ├── crop_profitability_matrix.png      # Crop vs Season net profit heatmap
│   │   ├── disease_pest_risk.png              # Humidity/Rainfall vs Pest Risk regressions
│   │   ├── correlation_heatmap.png            # Feature correlation matrix
│   │   ├── state_seasonal_disparity.png       # State-wise profit across seasons
│   │   ├── feature_importance.png             # ML predictive drivers for yield and profit
│   │   └── key_questions_summary.png          # Executive infographic
│   ├── models/                                # Trained ML model artifacts
│   │   ├── best_yield_model.pkl               # Gradient Boosting Yield Predictor (R2 = 0.975)
│   │   └── best_profit_model.pkl              # Gradient Boosting Profit Predictor (R2 = 0.981)
│   ├── IBM_SkillsBuild_Seasonal_Agriculture_Performance_Analysis.pptx # Completed presentation deck
│   ├── statistical_anova_tests.csv            # Parametric & non-parametric ANOVA results
│   ├── statistical_pairwise_tests.csv         # Mann-Whitney U tests with Bonferroni correction
│   └── ml_model_evaluation.csv                # Model comparison benchmark table
│
├── src/                                       # Modular Python source code
│   ├── data_preprocessing.py                  # Cleaning & feature engineering pipeline
│   ├── statistical_analysis.py                # Hypothesis testing & correlation analysis
│   ├── ml_models.py                           # Supervised ML training and cross-validation
│   ├── visualization.py                       # High-res figure generation
│   ├── generate_presentation.py               # PowerPoint automation script
│   └── build_jupyter_notebook.py              # Notebook generation & inline execution
│
├── app.py                                     # Interactive Streamlit Web Dashboard
├── PROJECT_REPORT.md                          # Comprehensive formal academic report
├── requirements.txt                           # Python dependencies
└── README.md                                  # Project overview and quickstart guide
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

## 🚀 Quickstart Guide

### 1. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/anshp/Seasonal-Agriculture-Performance-Analysis.git
cd Seasonal-Agriculture-Performance-Analysis
pip install -r requirements.txt
```

### 2. Launch the Streamlit Interactive Web App
Launch the interactive decision dashboard in your browser:
```bash
streamlit run app.py
```
*Explore seasonal comparisons, filter by state/crop/irrigation, run real-time ML simulations, and review the 12 key project answers.*

### 3. Open the Jupyter Notebook
Inspect the fully executed analysis:
```bash
jupyter notebook notebooks/Seasonal_Agriculture_Performance_Analysis.ipynb
```

### 4. Run Pipelines from Source
- **Data Preprocessing:** `python src/data_preprocessing.py`
- **Statistical Tests:** `python src/statistical_analysis.py`
- **Model Training:** `python src/ml_models.py`
- **Generate Figures:** `python src/visualization.py`
- **Build Presentation:** `python src/generate_presentation.py`

---

## 📋 Answers to the 12 Key Project Questions

1. **How does agricultural performance vary across seasons?**  
   Kharif delivers peak yields (5.63 t/ha) and profit (₹178,915). Rabi sustains high yield stability (5.09 t/ha) and healthy profitability (₹87,689). Zaid exhibits the lowest yields (4.63 t/ha) and net negative average profits (-₹24,805) due to heat stress and high irrigation overheads.
2. **What major seasonal patterns can be observed?**  
   Monsoon abundance in Kharif (852mm rain, 71.8% humidity) supports high vegetative growth but elevated pest risk (54.5%). Mild winter in Rabi (23.5°C) provides balanced growth with suppressed disease (40.5%). Summer in Zaid has high heat (31.0°C), low rainfall (299mm), and high evaporation.
3. **Which characteristics change between seasons?**  
   Rainfall ($F=3448$), Temperature ($F=2678$), Humidity ($F=1574$), Soil Moisture ($F=1642$), and Disease/Pest Risk ($F=1049$) vary drastically. Fertilizer dosing (184–187 kg/ha) and NPK levels remain static across seasons.
4. **What differences exist between agricultural activities in different seasons?**  
   Kharif activities focus on monsoon sowing, flood drainage, weed suppression, and active pest control. Rabi activities focus on winter irrigation scheduling and dry harvesting. Zaid activities revolve around supplemental irrigation and heat protection.
5. **Are there noticeable variations in resource usage across seasons?**  
   Yes. Water consumption peaks in Zaid (6,420 m³) despite lower yields, collapsing water efficiency to 4.41 t/1000m³. Kharif achieves peak water efficiency of 5.89 t/1000m³.
6. **Are there relationships between seasonal environmental conditions and agricultural performance?**  
   Yes. Disease/pest risk correlates strongly with Rainfall ($r = 0.624$) and Humidity ($r = 0.545$). High summer temperatures without micro-irrigation suppress water efficiency and net profitability.
7. **How do economic outcomes vary across seasons?**  
   Kharif generates the highest farm revenues (₹710,719) and profit margins (ROI 35.5%). Rabi provides solid returns (ROI 17.6%). Zaid suffers an average ROI of -2.5%, with 54.2% of farms recording net operating losses.
8. **Are some seasonal patterns consistent across different regions or categories?**  
   Yes. Across all 8 monitored states, Kharif is consistently the most lucrative season, and Zaid is the least profitable. Furthermore, Drip irrigation consistently outperforms flood irrigation across all states and seasons.
9. **Are there unusual or unexpected seasonal patterns?**  
   Zaid farms experience net losses despite receiving peak daily sunlight (8.18 hrs/day) and equivalent fertilizer inputs, driven by high irrigation costs and excessive evapotranspiration.
10. **What insights can be derived from the observed seasonal differences?**  
    Applying uniform input packages across all seasons leads to severe misallocation. High-value cash crops (Chilli, Sugarcane) maintain strong margins year-round, while staple grains require subsidized water or minimum support price protection.
11. **What conclusions can reasonably be drawn from the available data?**  
    Seasonal factors are statistically significant ($p < 0.0001$). Precision micro-irrigation (Drip) is the single most transformative intervention, lifting summer farms from severe losses (-₹69k) to positive profits (+₹21k). Machine learning models forecast yield and profit with high fidelity ($R^2 > 97\%$).
12. **How could the findings support better seasonal agricultural planning?**  
    (a) Subsidize 100% drip irrigation adoption for summer cultivation; (b) Issue prophylactic pest warnings during early Kharif; (c) Discourage water-intensive flood crops in Zaid in favor of drought-tolerant pulses or vegetables; (d) Calibrate seasonal agri-credit limits based on empirical seasonal ROI.

---

## 📜 Acknowledgments & Program Citation
Developed under the **AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026** (17th August to 30th September 2026), conducted in partnership with **BharatCares**, under the training and mentorship of **Mr. Kartik Hooda** (*Focus Topic: Data Analytics with AI: Foundation to Implementation*).
