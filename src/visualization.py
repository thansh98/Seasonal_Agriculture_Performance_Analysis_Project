"""
Visualization Generation Module
Seasonal Agriculture Performance Analysis
AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026
Implementation Partner: BharatCares | Trainer: Mr. Kartik Hooda
Generates publication-quality charts (DPI=300) saved to reports/figures/
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set aesthetic style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

SEASON_COLORS = {'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'}

def generate_all_plots(df: pd.DataFrame, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    print(f"[INFO] Generating charts in {output_dir}...")

    # 1. Seasonal Climate Distributions (Multi-panel)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    metrics = [
        ('Rainfall_mm', 'Rainfall (mm)', axes[0, 0]),
        ('Avg_Temperature_C', 'Average Temperature (°C)', axes[0, 1]),
        ('Humidity_pct', 'Humidity (%)', axes[1, 0]),
        ('Sunlight_Hours_Day', 'Sunlight Hours / Day', axes[1, 1])
    ]
    for col, label, ax in metrics:
        sns.boxplot(data=df, x='Season', y=col, hue='Season', palette=SEASON_COLORS, ax=ax, width=0.5, boxprops=dict(alpha=0.85), legend=False)
        sns.stripplot(data=df, x='Season', y=col, hue='Season', palette=SEASON_COLORS, ax=ax, size=2, alpha=0.3, jitter=0.2, legend=False)
        ax.set_title(f'Seasonal Variation in {label}', fontsize=12, fontweight='bold', pad=10)
        ax.set_xlabel('Season', fontweight='bold')
        ax.set_ylabel(label, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'seasonal_distributions.png'), dpi=300)
    plt.close()
    print("  [DONE] seasonal_distributions.png")

    # 2. Yield by Crop and Season
    fig, ax = plt.subplots(figsize=(13, 7))
    crop_order = df.groupby('Crop')['Yield_Tonnes_Ha'].mean().sort_values(ascending=False).index
    sns.barplot(data=df, x='Crop', y='Yield_Tonnes_Ha', hue='Season', order=crop_order,
                palette=SEASON_COLORS, errorbar=None, ax=ax)
    ax.set_title('Crop Yield (Tonnes/Ha) by Crop and Season', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Crop Type', fontweight='bold', fontsize=11)
    ax.set_ylabel('Mean Yield (Tonnes / Hectare)', fontweight='bold', fontsize=11)
    ax.tick_params(axis='x', rotation=30)
    ax.legend(title='Season', title_fontsize='11', loc='upper right')
    # Label bars
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f"{height:.1f}", (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, xytext=(0, 2), textcoords='offset points')
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'yield_by_crop_season.png'), dpi=300)
    plt.close()
    print("  [DONE] yield_by_crop_season.png")

    # 3. Irrigation Efficiency and Water Usage
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.barplot(data=df, x='Irrigation_Method', y='Water_Efficiency_t_per_1000m3', hue='Season',
                palette=SEASON_COLORS, errorbar=None, ax=axes[0])
    axes[0].set_title('Water Efficiency (Tonnes / 1000 m3) by Irrigation Method', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Irrigation Method', fontweight='bold')
    axes[0].set_ylabel('Water Efficiency (t / 1000 m3)', fontweight='bold')

    sns.barplot(data=df, x='Irrigation_Method', y='Profit_INR', hue='Season',
                palette=SEASON_COLORS, errorbar=None, ax=axes[1])
    axes[1].set_title('Average Profit (INR) by Irrigation Method & Season', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Irrigation Method', fontweight='bold')
    axes[1].set_ylabel('Mean Profit (INR)', fontweight='bold')
    axes[1].axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'irrigation_efficiency.png'), dpi=300)
    plt.close()
    print("  [DONE] irrigation_efficiency.png")

    # 4. Economic Performance (Revenue, Total Cost, Profit by Season)
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))
    sns.boxplot(data=df, x='Season', y='Revenue_INR', hue='Season', palette=SEASON_COLORS, ax=axes[0], width=0.45, legend=False)
    axes[0].set_title('Revenue Distribution (INR)', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Revenue (INR)', fontweight='bold')

    sns.boxplot(data=df, x='Season', y='Total_Cost_INR', hue='Season', palette=SEASON_COLORS, ax=axes[1], width=0.45, legend=False)
    axes[1].set_title('Total Input Cost Distribution (INR)', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Total Cost (INR)', fontweight='bold')

    sns.boxplot(data=df, x='Season', y='Profit_INR', hue='Season', palette=SEASON_COLORS, ax=axes[2], width=0.45, legend=False)
    axes[2].set_title('Net Profit Distribution (INR)', fontsize=12, fontweight='bold')
    axes[2].set_ylabel('Profit (INR)', fontweight='bold')
    axes[2].axhline(0, color='red', linestyle='--', linewidth=1, label='Break-even (0)')
    axes[2].legend()
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'economic_performance.png'), dpi=300)
    plt.close()
    print("  [DONE] economic_performance.png")

    # 5. Crop Profitability Heatmap (Crop vs Season)
    fig, ax = plt.subplots(figsize=(10, 7))
    pivot_profit = df.pivot_table(index='Crop', columns='Season', values='Profit_INR', aggfunc='mean')
    sns.heatmap(pivot_profit, annot=True, fmt=',.0f', cmap='RdYlGn', center=0, cbar_kws={'label': 'Mean Net Profit (INR)'}, ax=ax)
    ax.set_title('Net Profit (INR) Matrix: Crop vs Season', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Season', fontweight='bold', fontsize=12)
    ax.set_ylabel('Crop', fontweight='bold', fontsize=12)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'crop_profitability_matrix.png'), dpi=300)
    plt.close()
    print("  [DONE] crop_profitability_matrix.png")

    # 6. Disease & Pest Risk vs Environmental Conditions
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.scatterplot(data=df, x='Humidity_pct', y='Disease_Pest_Risk_pct', hue='Season',
                    palette=SEASON_COLORS, alpha=0.6, ax=axes[0], s=25)
    sns.regplot(data=df, x='Humidity_pct', y='Disease_Pest_Risk_pct', scatter=False, ax=axes[0], color='black', line_kws={'linewidth': 1.5})
    axes[0].set_title('Disease & Pest Risk vs Humidity (%)', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Humidity (%)', fontweight='bold')
    axes[0].set_ylabel('Disease/Pest Risk (%)', fontweight='bold')

    sns.boxplot(data=df, x='Season', y='Disease_Pest_Risk_pct', hue='Season', palette=SEASON_COLORS, ax=axes[1], width=0.45, legend=False)
    axes[1].set_title('Seasonal Distribution of Disease/Pest Risk', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Season', fontweight='bold')
    axes[1].set_ylabel('Disease/Pest Risk (%)', fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'disease_pest_risk.png'), dpi=300)
    plt.close()
    print("  [DONE] disease_pest_risk.png")

    # 7. Correlation Heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    corr_cols = [
        'Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Sunlight_Hours_Day', 'Soil_pH', 'Soil_Moisture_pct',
        'NPK_Total_kg_ha', 'Fertilizer_kg_ha', 'Pesticide_Litre_ha', 'Water_Used_m3',
        'Yield_Tonnes_Ha', 'Water_Efficiency_t_per_1000m3', 'Disease_Pest_Risk_pct', 'Profit_INR'
    ]
    corr = df[corr_cols].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, cmap='vlag', annot=True, fmt='.2f', vmin=-1, vmax=1, center=0,
                square=True, linewidths=.5, cbar_kws={'shrink': .8}, ax=ax)
    ax.set_title('Correlation Matrix of Agricultural, Environmental & Economic Features', fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'correlation_heatmap.png'), dpi=300)
    plt.close()
    print("  [DONE] correlation_heatmap.png")

    # 8. State Seasonal Disparity
    fig, ax = plt.subplots(figsize=(14, 7))
    state_order = df.groupby('State')['Profit_INR'].mean().sort_values(ascending=False).index
    sns.barplot(data=df, x='State', y='Profit_INR', hue='Season', order=state_order,
                palette=SEASON_COLORS, errorbar=None, ax=ax)
    ax.set_title('Seasonal Farm Profitability (INR) Across Indian States', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('State', fontweight='bold', fontsize=11)
    ax.set_ylabel('Average Profit (INR)', fontweight='bold', fontsize=11)
    ax.tick_params(axis='x', rotation=30)
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.legend(title='Season', title_fontsize='11', loc='upper right')
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'state_seasonal_disparity.png'), dpi=300)
    plt.close()
    print("  [DONE] state_seasonal_disparity.png")

    # 9. Top Feature Importances (Load from reports if available)
    imp_file = os.path.join(os.path.dirname(output_dir), 'yield_feature_importances.csv')
    if os.path.exists(imp_file):
        imp_df = pd.read_csv(imp_file).head(12)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=imp_df, x='Importance', y='Feature', palette='mako', ax=ax)
        ax.set_title('Top Drivers of Crop Yield (Random Forest Feature Importance)', fontsize=13, fontweight='bold', pad=15)
        ax.set_xlabel('Relative Importance Weight', fontweight='bold')
        ax.set_ylabel('Predictive Feature', fontweight='bold')
        for p in ax.patches:
            width = p.get_width()
            ax.annotate(f"{width:.3f}", (width, p.get_y() + p.get_height() / 2.),
                        ha='left', va='center', fontsize=9, xytext=(5, 0), textcoords='offset points')
        plt.tight_layout()
        fig.savefig(os.path.join(output_dir, 'feature_importance.png'), dpi=300)
        plt.close()
        print("  [DONE] feature_importance.png")

    # 10. Executive Dashboard Overview Infographic
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    # KPI 1: Profitability breakdown
    profit_share = df.groupby(['Season', 'Profitability_Category']).size().unstack(fill_value=0)
    profit_share_pct = (profit_share.T / profit_share.sum(axis=1)).T * 100
    profit_share_pct.plot(kind='bar', stacked=True, ax=axes[0, 0], colormap='Spectral', edgecolor='black', alpha=0.85)
    axes[0, 0].set_title('Share of Farms by Profitability Category (%)', fontsize=12, fontweight='bold')
    axes[0, 0].set_ylabel('Percentage (%)', fontweight='bold')
    axes[0, 0].legend(title='Category', loc='lower left')
    axes[0, 0].tick_params(axis='x', rotation=0)

    # KPI 2: Water efficiency across seasons
    sns.boxplot(data=df, x='Season', y='Water_Efficiency_t_per_1000m3', hue='Season', palette=SEASON_COLORS, ax=axes[0, 1], width=0.45, legend=False)
    axes[0, 1].set_title('Water Efficiency (Tonnes / 1000 m3 Water Used)', fontsize=12, fontweight='bold')
    axes[0, 1].set_ylabel('Efficiency (t / 1000 m3)', fontweight='bold')

    # KPI 3: Yield vs Rainfall by Season
    sns.scatterplot(data=df, x='Rainfall_mm', y='Yield_Tonnes_Ha', hue='Season', palette=SEASON_COLORS, alpha=0.5, ax=axes[1, 0], s=20)
    axes[1, 0].set_title('Crop Yield vs Rainfall (mm) by Season', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Rainfall (mm)', fontweight='bold')
    axes[1, 0].set_ylabel('Yield (Tonnes/Ha)', fontweight='bold')

    # KPI 4: Net Profit vs Total Cost
    sns.scatterplot(data=df, x='Total_Cost_INR', y='Profit_INR', hue='Season', palette=SEASON_COLORS, alpha=0.5, ax=axes[1, 1], s=20)
    axes[1, 1].axhline(0, color='red', linestyle='--', linewidth=0.8)
    axes[1, 1].set_title('Farm Profit vs Total Production Cost (INR)', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Total Cost (INR)', fontweight='bold')
    axes[1, 1].set_ylabel('Net Profit (INR)', fontweight='bold')

    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'key_questions_summary.png'), dpi=300)
    plt.close()
    print("  [DONE] key_questions_summary.png")

    print("[SUCCESS] All 10 publication-ready figures generated successfully.")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'cleaned_seasonal_agriculture_dataset.csv')
    figures_dir = os.path.join(base_dir, 'reports', 'figures')
    df = pd.read_csv(data_path)
    generate_all_plots(df, figures_dir)

if __name__ == '__main__':
    main()
