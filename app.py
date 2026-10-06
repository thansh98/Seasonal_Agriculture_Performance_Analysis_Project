"""
Seasonal Agriculture Performance Analysis - Interactive Web Application
AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026
Implementation Partner: BharatCares | Trainer: Mr. Kartik Hooda
Author: AICTE - IBM SkillsBuild Data Analytics Intern
"""

import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib

# Page configuration
st.set_page_config(
    page_title="Seasonal Agriculture Performance Analysis | IBM SkillsBuild & AICTE",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data and models
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'cleaned_seasonal_agriculture_dataset.csv')
    df = pd.read_csv(data_path)
    return df

@st.cache_resource
def load_models():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, 'reports', 'models')
    
    yield_model = joblib.load(os.path.join(models_dir, 'best_yield_model.pkl'))
    profit_model = joblib.load(os.path.join(models_dir, 'best_profit_model.pkl'))
    yield_cols = joblib.load(os.path.join(models_dir, 'yield_feature_names.pkl'))
    profit_cols = joblib.load(os.path.join(models_dir, 'profit_feature_names.pkl'))
    return yield_model, profit_model, yield_cols, profit_cols

df = load_data()
yield_model, profit_model, yield_cols, profit_cols = load_models()

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        color: #1b4332;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #2b8a3e;
        margin-bottom: 0.3rem;
        font-weight: 600;
    }
    .badge-bar {
        font-size: 0.9rem;
        color: #495057;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 15px;
        border-left: 5px solid #2d6a4f;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .kpi-title { font-size: 0.85rem; color: #6c757d; text-transform: uppercase; }
    .kpi-value { font-size: 1.6rem; font-weight: bold; color: #1b4332; }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-header">🌾 Seasonal Agriculture Performance Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026</div>', unsafe_allow_html=True)
st.markdown('<div class="badge-bar">🤝 <b>Implementation Partner:</b> BharatCares | ⏱️ <b>Duration:</b> 17th Aug – 30th Sept 2026 | 👨‍🏫 <b>Trainer:</b> Mr. Kartik Hooda</div>', unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.image("https://images.unsplash.com/photo-1500937386664-56d1dfef3854?auto=format&fit=crop&w=400&q=80", use_column_width=True)
st.sidebar.header("🔍 Global Dataset Filters")

selected_seasons = st.sidebar.multiselect(
    "Select Season(s):",
    options=['Kharif', 'Rabi', 'Zaid'],
    default=['Kharif', 'Rabi', 'Zaid']
)

selected_states = st.sidebar.multiselect(
    "Select State(s):",
    options=sorted(df['State'].unique()),
    default=sorted(df['State'].unique())
)

selected_crops = st.sidebar.multiselect(
    "Select Crop(s):",
    options=sorted(df['Crop'].unique()),
    default=sorted(df['Crop'].unique())
)

selected_irrigation = st.sidebar.multiselect(
    "Select Irrigation Method:",
    options=sorted(df['Irrigation_Method'].unique()),
    default=sorted(df['Irrigation_Method'].unique())
)

# Apply filters
filtered_df = df[
    (df['Season'].isin(selected_seasons)) &
    (df['State'].isin(selected_states)) &
    (df['Crop'].isin(selected_crops)) &
    (df['Irrigation_Method'].isin(selected_irrigation))
]

if filtered_df.empty:
    st.warning("⚠️ No data available for the selected filter combination. Please broaden your selection.")
    st.stop()

# Top KPI Banner
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Farms Filtered", f"{len(filtered_df):,}", f"{(len(filtered_df)/len(df)*100):.1f}% of total")
with col2:
    st.metric("Mean Yield (t/ha)", f"{filtered_df['Yield_Tonnes_Ha'].mean():.2f}", f"Std: {filtered_df['Yield_Tonnes_Ha'].std():.2f}")
with col3:
    st.metric("Water Efficiency", f"{filtered_df['Water_Efficiency_t_per_1000m3'].mean():.2f} t/km³", "Tonnes / 1000m³")
with col4:
    st.metric("Average Profit (INR)", f"₹{filtered_df['Profit_INR'].mean():,.0f}", f"Margin: {filtered_df['Profit_Margin_pct'].median():.1f}%")
with col5:
    st.metric("Pest & Disease Risk", f"{filtered_df['Disease_Pest_Risk_pct'].mean():.1f}%", f"Rainfall: {filtered_df['Rainfall_mm'].mean():.0f}mm")

st.markdown("---")

# Main Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Executive Summary",
    "⛅ Seasonal Climate Dynamics",
    "💧 Water & Irrigation Efficiency",
    "💰 Farm Economics & Margins",
    "🗺️ Regional Performance",
    "🤖 AI Yield & Profit Simulator",
    "📋 12 Key Analytical Questions"
])

# ----------------- TAB 1: EXECUTIVE SUMMARY -----------------
with tab1:
    st.subheader("Seasonal Performance Comparison: Kharif vs Rabi vs Zaid")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        # Profit by Season
        fig_profit = px.box(
            filtered_df, x="Season", y="Profit_INR", color="Season",
            color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'},
            title="Net Farm Profit Distribution Across Seasons (INR)",
            points="outliers"
        )
        fig_profit.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Break-Even Point (₹0)")
        fig_profit.update_layout(showlegend=False)
        st.plotly_chart(fig_profit, use_container_width=True)

    with col_b:
        # Yield by Season
        fig_yield = px.box(
            filtered_df, x="Season", y="Yield_Tonnes_Ha", color="Season",
            color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'},
            title="Crop Yield Distribution Across Seasons (Tonnes/Ha)",
            points="outliers"
        )
        fig_yield.update_layout(showlegend=False)
        st.plotly_chart(fig_yield, use_container_width=True)

    # Seasonal Summary Table
    st.markdown("### Aggregated Seasonal Benchmarks")
    summary_cols = ['Yield_Tonnes_Ha', 'Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 
                    'Water_Used_m3', 'Water_Efficiency_t_per_1000m3', 'Disease_Pest_Risk_pct',
                    'Total_Cost_INR', 'Revenue_INR', 'Profit_INR', 'ROI_pct']
    
    summary_table = filtered_df.groupby('Season')[summary_cols].mean().round(2)
    st.dataframe(summary_table.T, use_container_width=True)

    st.info("""
    **Core Insights:**
    1. **Monsoon Boost (Kharif):** Yields and profits peak in Kharif driven by 852mm rainfall and high water efficiency (5.89 t/1000m³), yielding an average profit of ₹178,915.
    2. **Winter Stability (Rabi):** Optimal temperature (23.5°C) and lower humidity lower disease risk to 40.5% with steady profitability of ₹87,689.
    3. **Summer Penalty (Zaid):** High evaporation, high irrigation demand (6,420 m³), and reduced yields cause average farm profits to collapse into the negative (-₹24,805).
    """)

# ----------------- TAB 2: CLIMATE DYNAMICS -----------------
with tab2:
    st.subheader("Environmental & Climatic Drivers Across Seasons")
    c1, c2 = st.columns(2)
    with c1:
        fig_clim = px.scatter(
            filtered_df, x="Avg_Temperature_C", y="Rainfall_mm", color="Season",
            size="Humidity_pct", hover_data=['Crop', 'State', 'Profit_INR'],
            color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'},
            title="Climate Clusters: Temperature vs Rainfall vs Humidity"
        )
        st.plotly_chart(fig_clim, use_container_width=True)
    with c2:
        fig_pest = px.scatter(
            filtered_df, x="Humidity_pct", y="Disease_Pest_Risk_pct", color="Season",
            trendline="ols",
            color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'},
            title="Disease & Pest Risk vs Relative Humidity (%)"
        )
        st.plotly_chart(fig_pest, use_container_width=True)

    st.markdown("### Soil Moisture and Sunlight Interaction")
    c3, c4 = st.columns(2)
    with c3:
        fig_soil = px.violin(filtered_df, x="Season", y="Soil_Moisture_pct", color="Season", box=True,
                             color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'})
        st.plotly_chart(fig_soil, use_container_width=True)
    with c4:
        fig_sun = px.histogram(filtered_df, x="Sunlight_Hours_Day", color="Season", barmode="overlay",
                               color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'})
        st.plotly_chart(fig_sun, use_container_width=True)

# ----------------- TAB 3: WATER & IRRIGATION -----------------
with tab3:
    st.subheader("Resource Usage & Irrigation Method Performance")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        fig_irrig_eff = px.bar(
            filtered_df.groupby(['Irrigation_Method', 'Season'])['Water_Efficiency_t_per_1000m3'].mean().reset_index(),
            x="Irrigation_Method", y="Water_Efficiency_t_per_1000m3", color="Season", barmode="group",
            color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'},
            title="Water Efficiency (t / 1000 m³) by Irrigation Method"
        )
        st.plotly_chart(fig_irrig_eff, use_container_width=True)

    with col_w2:
        fig_irrig_prof = px.bar(
            filtered_df.groupby(['Irrigation_Method', 'Season'])['Profit_INR'].mean().reset_index(),
            x="Irrigation_Method", y="Profit_INR", color="Season", barmode="group",
            color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'},
            title="Net Profit (INR) by Irrigation Method and Season"
        )
        fig_irrig_prof.add_hline(y=0, line_dash="dash", line_color="gray")
        st.plotly_chart(fig_irrig_prof, use_container_width=True)

    st.success("""
    💡 **Micro-Irrigation Breakthrough:**
    - **Drip Irrigation** maintains high efficiency across all seasons and is the ONLY method guaranteeing positive farm profits during the harsh Zaid summer (+₹21,291).
    - **Flood Irrigation** wastes water during summer, causing steep losses averaging -₹69,787 per farm in Zaid.
    """)

# ----------------- TAB 4: ECONOMICS -----------------
with tab4:
    st.subheader("Crop Profitability Matrix & Financial Returns")
    crop_season_profit = filtered_df.pivot_table(index='Crop', columns='Season', values='Profit_INR', aggfunc='mean')
    
    fig_heat = px.imshow(
        crop_season_profit,
        text_auto='.0f',
        color_continuous_scale="RdYlGn",
        title="Crop Profitability Heatmap (Mean Net Profit in INR)"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    col_e1, col_e2 = st.columns(2)
    with col_e1:
        fig_cost_rev = px.scatter(
            filtered_df, x="Total_Cost_INR", y="Revenue_INR", color="Crop",
            hover_data=['Season', 'Profit_INR'],
            title="Revenue vs Input Cost (INR)"
        )
        fig_cost_rev.add_shape(type="line", x0=0, y0=0, x1=1200000, y1=1200000, line=dict(color="red", dash="dash"))
        st.plotly_chart(fig_cost_rev, use_container_width=True)

    with col_e2:
        cat_counts = filtered_df.groupby(['Season', 'Profitability_Category']).size().reset_index(name='Count')
        fig_cat = px.bar(cat_counts, x="Season", y="Count", color="Profitability_Category",
                         color_discrete_map={'High Profit (>100k)': '#2b8a3e', 'Moderate Profit (0-100k)': '#74c0fc', 'Loss Making (<0)': '#fa5252'},
                         title="Share of Farms in Profit vs Loss Categories")
        st.plotly_chart(fig_cat, use_container_width=True)

# ----------------- TAB 5: REGIONAL PERFORMANCE -----------------
with tab5:
    st.subheader("State-Level Seasonal Disparities")
    fig_state = px.bar(
        filtered_df.groupby(['State', 'Season'])['Profit_INR'].mean().reset_index(),
        x="State", y="Profit_INR", color="Season", barmode="group",
        color_discrete_map={'Kharif': '#2b8a3e', 'Rabi': '#1971c2', 'Zaid': '#e8590c'},
        title="State-Wise Farm Profitability Across Seasons (INR)"
    )
    fig_state.add_hline(y=0, line_dash="dash", line_color="gray")
    st.plotly_chart(fig_state, use_container_width=True)

    st.markdown("### District Level Yield Rankings")
    dist_stats = filtered_df.groupby(['State', 'District'])[['Yield_Tonnes_Ha', 'Profit_INR', 'Water_Efficiency_t_per_1000m3']].mean().round(2).reset_index()
    st.dataframe(dist_stats.sort_values(by='Profit_INR', ascending=False), use_container_width=True)

# ----------------- TAB 6: AI SIMULATOR -----------------
with tab6:
    st.subheader("🤖 AI Real-Time Yield & Farm Profitability Simulator")
    st.write("Leverage trained Gradient Boosting models (Yield R² = 97.5%, Profit R² = 98.1%) to evaluate farm configurations.")

    with st.form("simulator_form"):
        sim_col1, sim_col2, sim_col3 = st.columns(3)
        with sim_col1:
            in_season = st.selectbox("Season:", ['Kharif', 'Rabi', 'Zaid'])
            in_crop = st.selectbox("Crop:", sorted(df['Crop'].unique()))
            in_state = st.selectbox("State:", sorted(df['State'].unique()))
            in_method = st.selectbox("Irrigation Method:", sorted(df['Irrigation_Method'].unique()))
            in_area = st.number_input("Farm Area (Hectares):", min_value=0.1, max_value=20.0, value=3.0, step=0.5)

        with sim_col2:
            in_rainfall = st.slider("Rainfall (mm):", 100.0, 1500.0, 600.0)
            in_temp = st.slider("Avg Temperature (°C):", 15.0, 40.0, 26.0)
            in_humidity = st.slider("Humidity (%):", 25.0, 95.0, 65.0)
            in_sunlight = st.slider("Sunlight Hours / Day:", 4.0, 12.0, 7.5)
            in_ph = st.slider("Soil pH:", 4.5, 9.0, 6.8)

        with sim_col3:
            in_n = st.number_input("Nitrogen (kg/ha):", 40.0, 200.0, 120.0)
            in_p = st.number_input("Phosphorus (kg/ha):", 20.0, 100.0, 55.0)
            in_k = st.number_input("Potassium (kg/ha):", 40.0, 180.0, 100.0)
            in_fertilizer = st.number_input("Total Fertilizer (kg/ha):", 100.0, 300.0, 185.0)
            in_pesticide = st.number_input("Pesticide (L/ha):", 1.0, 10.0, 5.0)
            in_seed_score = st.slider("Seed Quality Score (0 to 1):", 0.5, 1.0, 0.85)
            in_water = st.number_input("Water Used (m³):", 500, 15000, 5000, step=500)
            in_price = st.number_input("Expected Market Price (INR / Tonne):", 10000, 120000, 35000, step=5000)
            in_cost = st.number_input("Total Expected Cost (INR):", 50000, 1200000, 450000, step=50000)

        submit_btn = st.form_submit_button("🚀 Run Predictive AI Simulation", use_container_width=True)

    if submit_btn:
        # Construct inference vector
        sim_input = {
            'State': in_state,
            'Crop': in_crop,
            'Season': in_season,
            'Irrigation_Method': in_method,
            'Farm_Area_Hectares': in_area,
            'Rainfall_mm': in_rainfall,
            'Avg_Temperature_C': in_temp,
            'Humidity_pct': in_humidity,
            'Sunlight_Hours_Day': in_sunlight,
            'Soil_pH': in_ph,
            'Soil_Moisture_pct': 25.0,
            'Nitrogen_kg_ha': in_n,
            'Phosphorus_kg_ha': in_p,
            'Potassium_kg_ha': in_k,
            'Fertilizer_kg_ha': in_fertilizer,
            'Pesticide_Litre_ha': in_pesticide,
            'Seed_Quality_Score': in_seed_score,
            'Water_Used_m3': in_water,
            'Disease_Pest_Risk_pct': 45.0
        }
        sim_df = pd.DataFrame([sim_input])
        sim_encoded = pd.get_dummies(sim_df)
        
        # Align features with yield model
        X_yield = pd.DataFrame(0, index=[0], columns=yield_cols)
        for col in yield_cols:
            if col in sim_encoded.columns:
                X_yield[col] = sim_encoded[col].values[0]
            elif col in sim_df.columns:
                X_yield[col] = sim_df[col].values[0]

        pred_yield = float(yield_model.predict(X_yield)[0])
        pred_prod = pred_yield * in_area

        # Align features with profit model
        sim_df_profit = sim_df.copy()
        sim_df_profit['Market_Price_INR_Tonne'] = in_price
        sim_df_profit['Production_Tonnes'] = pred_prod
        sim_df_profit['Total_Cost_INR'] = in_cost
        sim_enc_p = pd.get_dummies(sim_df_profit)

        X_profit = pd.DataFrame(0, index=[0], columns=profit_cols)
        for col in profit_cols:
            if col in sim_enc_p.columns:
                X_profit[col] = sim_enc_p[col].values[0]
            elif col in sim_df_profit.columns:
                X_profit[col] = sim_df_profit[col].values[0]

        pred_profit = float(profit_model.predict(X_profit)[0])
        pred_rev = pred_profit + in_cost
        pred_margin = (pred_profit / pred_rev) * 100 if pred_rev > 0 else 0

        st.markdown("### 🎯 Simulation Output")
        res_col1, res_col2, res_col3, res_col4 = st.columns(4)
        with res_col1:
            st.metric("Predicted Yield", f"{pred_yield:.2f} t/ha", f"Total: {pred_prod:.1f} tonnes")
        with res_col2:
            st.metric("Predicted Net Profit", f"₹{pred_profit:,.0f}", f"Margin: {pred_margin:.1f}%")
        with res_col3:
            st.metric("Estimated Revenue", f"₹{pred_rev:,.0f}", f"₹{(pred_rev/in_area):,.0f} / ha")
        with res_col4:
            profit_status = "🟢 Highly Profitable" if pred_profit > 100000 else ("🟡 Moderately Profitable" if pred_profit >= 0 else "🔴 Loss Making")
            st.metric("Viability Status", profit_status)

# ----------------- TAB 7: 12 KEY QUESTIONS -----------------
with tab7:
    st.subheader("📋 Comprehensive Evidence-Based Answers to the 12 Major Project Questions")
    
    questions_answers = [
        ("1. How does agricultural performance vary across seasons?",
         "Agricultural performance varies dramatically across seasons. Kharif records the highest average yields (5.63 t/ha) and the highest profitability (₹178,915). Rabi sustains high yield stability (5.09 t/ha) and healthy profitability (₹87,689). Zaid exhibits the lowest yields (4.63 t/ha) and net negative average profits (-₹24,805) due to severe summer heat and heavy irrigation overheads."),
        
        ("2. What major seasonal patterns can be observed?",
         "Climatic and biological patterns follow distinct rhythms: Kharif experiences 852mm rainfall and 71.8% humidity, which fuels rapid vegetative growth but drives pest risk to 54.5%. Rabi enjoys mild temperatures (23.5°C) and moderate humidity (57.9%), creating ideal conditions for wheat and pulses with low disease incidence (40.5%). Zaid is defined by peak temperatures (31.0°C), low rainfall (299mm), and high evaporation."),
        
        ("3. Which characteristics change between seasons?",
         "The most volatile characteristics across seasons are Rainfall (F=3448, p<1e-300), Temperature (F=2678), Humidity (F=1574), Soil Moisture (F=1642), and Disease/Pest Risk (F=1049). In contrast, fertilizer application (184-187 kg/ha) and soil macronutrients (NPK) remain relatively static, reflecting fixed farmer dosing habits regardless of season."),
         
        ("4. What differences exist between agricultural activities in different seasons?",
         "In Kharif, farming is synchronized with the southwest monsoon, requiring heavy disease monitoring and weed control. In Rabi, agricultural activities shift to winter irrigation scheduling and harvesting during cool dry months. In Zaid, activities revolve around intensive supplemental irrigation, heat stress mitigation, and short-duration cash cropping."),
         
        ("5. Are there noticeable variations in resource usage across seasons?",
         "Yes. Water usage peaks in Zaid (mean 6,420 m³) despite lower yields, dragging water efficiency down to 4.41 t/1000m³. In contrast, Kharif leverages natural precipitation to achieve a peak water efficiency of 5.89 t/1000m³ while using an average of 6,102 m³."),
         
        ("6. Are there relationships between seasonal environmental conditions and agricultural performance?",
         "Strong relationships exist. Disease & pest risk correlates strongly with Rainfall (r = 0.62) and Humidity (r = 0.55). Sunlight hours correlate positively with crop ripening in Rabi. High summer temperatures without micro-irrigation suppress water efficiency and net profitability."),
         
        ("7. How do economic outcomes vary across seasons?",
         "Kharif generates the highest farm revenues (₹710,719) and highest profit margins (average ROI 35.5%). Rabi provides solid returns (ROI 17.6%). Zaid suffers an average ROI of -2.5%, with 54.2% of farms recording net operating losses due to high costs that cannot be offset by summer yields."),
         
        ("8. Are some seasonal patterns consistent across different regions or categories?",
         "Yes. Across all 8 states (Andhra Pradesh, Maharashtra, Punjab, Tamil Nadu, Telangana, Karnataka, Gujarat, Madhya Pradesh), Kharif is consistently the most profitable season, and Zaid is universally the lowest-performing. Furthermore, Drip irrigation consistently outperforms flood irrigation across all states and seasons."),
         
        ("9. Are there unusual or unexpected seasonal patterns?",
         "An unexpected pattern is that Zaid farms experience net losses despite having higher average sunlight hours (8.18 hrs/day) and equivalent fertilizer input. The root cause is high irrigation electricity/labor costs combined with extreme summer evapotranspiration and sub-optimal flood irrigation."),
         
        ("10. What insights can be derived from the observed seasonal differences?",
         "Fixed input packages (applying the same fertilizer and pesticide rates in all seasons) are fundamentally flawed. High summer input costs without precision irrigation directly destroy farmer profitability. High-value cash crops (Chilli, Sugarcane) are resilient to seasonal swings, while staple grains require subsidized water or minimum support price protection."),
         
        ("11. What conclusions can reasonably be drawn from the available data?",
         "Seasonal differences are statistically significant (p < 0.0001 for all environmental, yield, water efficiency, and financial metrics). Precision micro-irrigation (Drip) is the single most transformative intervention, lifting summer farms from severe losses (-₹69k) to positive profits (+₹21k). Machine learning models (Gradient Boosting) can accurately predict yield and profit (R² > 97%)."),
         
        ("12. How could the findings support better seasonal agricultural planning?",
         "Findings provide a roadmap for policy and farm planning: (a) Subsidize 100% drip irrigation adoption in summer-cultivated areas; (b) Issue seasonal prophylactic pest alerts during Kharif monsoon weeks; (c) Discourage water-intensive flood crops during Zaid in favor of drought-tolerant pulses or vegetables; (d) Calibrate crop credit limits based on seasonal ROI rather than uniform annual loan limits.")
    ]

    for q, a in questions_answers:
        with st.expander(f"📌 {q}", expanded=False):
            st.markdown(f"**Analysis & Findings:**\n\n{a}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #495057; font-size: 0.95rem;'><b>AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026</b><br>Implementation Partner: <b>BharatCares</b> | Focus: <i>Data Analytics with AI: Foundation to Implementation</i> | Trainer: <b>Mr. Kartik Hooda</b></div>", unsafe_allow_html=True)
