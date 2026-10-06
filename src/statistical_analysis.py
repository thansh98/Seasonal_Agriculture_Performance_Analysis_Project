"""
Statistical Analysis and Hypothesis Testing Module
Seasonal Agriculture Performance Analysis
AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026
Implementation Partner: BharatCares | Trainer: Mr. Kartik Hooda
"""

import os
import pandas as pd
import numpy as np
from scipy import stats

def run_seasonal_anova(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs One-Way ANOVA and Kruskal-Wallis H tests across Seasons (Kharif, Rabi, Zaid)
    for all environmental, resource, and outcome variables.
    """
    numeric_cols = [
        'Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Sunlight_Hours_Day',
        'Soil_pH', 'Soil_Moisture_pct', 'Nitrogen_kg_ha', 'Phosphorus_kg_ha', 'Potassium_kg_ha',
        'Fertilizer_kg_ha', 'Pesticide_Litre_ha', 'Seed_Quality_Score',
        'Yield_Tonnes_Ha', 'Production_Tonnes', 'Water_Used_m3', 'Water_Efficiency_t_per_1000m3',
        'Disease_Pest_Risk_pct', 'Total_Cost_INR', 'Revenue_INR', 'Profit_INR',
        'Profit_Margin_pct', 'ROI_pct', 'Profit_Per_Ha_INR'
    ]

    results = []
    seasons = ['Kharif', 'Rabi', 'Zaid']
    
    for col in numeric_cols:
        groups = [df[df['Season'] == s][col].dropna() for s in seasons]
        
        # Means
        k_mean = groups[0].mean()
        r_mean = groups[1].mean()
        z_mean = groups[2].mean()

        # One-Way ANOVA (Parametric)
        f_stat, p_val_anova = stats.f_oneway(*groups)

        # Kruskal-Wallis (Non-Parametric)
        h_stat, p_val_kw = stats.kruskal(*groups)

        results.append({
            'Variable': col,
            'Kharif_Mean': round(k_mean, 2),
            'Rabi_Mean': round(r_mean, 2),
            'Zaid_Mean': round(z_mean, 2),
            'ANOVA_F': round(f_stat, 2),
            'ANOVA_p_val': f"{p_val_anova:.2e}" if p_val_anova < 0.001 else round(p_val_anova, 4),
            'Kruskal_H': round(h_stat, 2),
            'Kruskal_p_val': f"{p_val_kw:.2e}" if p_val_kw < 0.001 else round(p_val_kw, 4),
            'Significant_0.05': 'Yes' if p_val_anova < 0.05 else 'No'
        })

    res_df = pd.DataFrame(results)
    return res_df

def run_chi_square_tests(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs Chi-Square Test of Independence for categorical seasonal associations.
    """
    cat_pairs = [
        ('Irrigation_Method', 'Season'),
        ('Profitability_Category', 'Season'),
        ('Crop', 'Season'),
        ('State', 'Profitability_Category')
    ]

    results = []
    for var1, var2 in cat_pairs:
        contingency = pd.crosstab(df[var1], df[var2])
        chi2, p, dof, _ = stats.chi2_contingency(contingency)
        results.append({
            'Relationship': f"{var1} vs {var2}",
            'Chi2_Stat': round(chi2, 2),
            'p_value': f"{p:.2e}" if p < 0.001 else round(p, 4),
            'Degrees_of_Freedom': dof,
            'Significant': 'Yes' if p < 0.05 else 'No'
        })

    return pd.DataFrame(results)

def run_pairwise_tests(df: pd.DataFrame, key_metrics=None) -> pd.DataFrame:
    """
    Performs Mann-Whitney U pairwise tests between seasons with Bonferroni correction.
    """
    if key_metrics is None:
        key_metrics = ['Yield_Tonnes_Ha', 'Profit_INR', 'Water_Efficiency_t_per_1000m3', 
                       'Rainfall_mm', 'Disease_Pest_Risk_pct']
    
    pairs = [('Kharif', 'Rabi'), ('Kharif', 'Zaid'), ('Rabi', 'Zaid')]
    results = []
    for m in key_metrics:
        for s1, s2 in pairs:
            v1 = df[df['Season'] == s1][m].dropna()
            v2 = df[df['Season'] == s2][m].dropna()
            u_stat, p_val = stats.mannwhitneyu(v1, v2, alternative='two-sided')
            results.append({
                'Metric': m,
                'Comparison': f"{s1} vs {s2}",
                'Mean_Diff': round(v1.mean() - v2.mean(), 2),
                'U_Statistic': round(u_stat, 2),
                'p_value': f"{p_val:.2e}" if p_val < 0.001 else round(p_val, 4),
                'Significant (Bonferroni alpha=0.017)': 'Yes' if p_val < (0.05 / 3) else 'No'
            })
    return pd.DataFrame(results)

def compute_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes Pearson and Spearman correlation between environmental conditions and performance outcomes.
    """
    env_cols = ['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Sunlight_Hours_Day', 'Soil_pH', 'Soil_Moisture_pct']
    out_cols = ['Yield_Tonnes_Ha', 'Water_Efficiency_t_per_1000m3', 'Profit_INR', 'Disease_Pest_Risk_pct', 'ROI_pct']

    corr_matrix = pd.DataFrame(index=env_cols, columns=out_cols)
    for e in env_cols:
        for o in out_cols:
            r, _ = stats.pearsonr(df[e], df[o])
            corr_matrix.loc[e, o] = round(r, 3)

    return corr_matrix

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'cleaned_seasonal_agriculture_dataset.csv')
    reports_dir = os.path.join(base_dir, 'reports')
    os.makedirs(reports_dir, exist_ok=True)

    df = pd.read_csv(data_path)

    anova_df = run_seasonal_anova(df)
    chi2_df = run_chi_square_tests(df)
    pairwise_df = run_pairwise_tests(df)
    corr_df = compute_correlations(df)

    print("=== SEASONAL ANOVA & KRUSKAL-WALLIS RESULTS ===")
    print(anova_df.to_string())

    print("\n=== CHI-SQUARE TESTS OF INDEPENDENCE ===")
    print(chi2_df.to_string())

    print("\n=== PAIRWISE MANN-WHITNEY TESTS ===")
    print(pairwise_df.to_string())

    print("\n=== CORRELATION MATRIX (ENV VS OUTCOMES) ===")
    print(corr_df.to_string())

    # Save to CSV
    anova_df.to_csv(os.path.join(reports_dir, 'statistical_anova_tests.csv'), index=False)
    chi2_df.to_csv(os.path.join(reports_dir, 'statistical_chi2_tests.csv'), index=False)
    pairwise_df.to_csv(os.path.join(reports_dir, 'statistical_pairwise_tests.csv'), index=False)
    corr_df.to_csv(os.path.join(reports_dir, 'environmental_outcome_correlations.csv'))
    print(f"\n[SUCCESS] Statistical reports saved to {reports_dir}")

if __name__ == '__main__':
    main()
