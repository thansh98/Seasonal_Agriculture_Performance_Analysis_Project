"""
Word Document (.docx) Project Report Generator
Seasonal Agriculture Performance Analysis
AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026
Implementation Partner: BharatCares | Trainer: Mr. Kartik Hooda
Generates a formal, professionally formatted Word document (.docx)
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets cell padding."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def generate_report(output_docx_path: str, figures_dir: str):
    doc = Document()

    # Page Margins (1 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Palette
    NAVY = RGBColor(16, 44, 87)
    GREEN = RGBColor(43, 138, 62)
    DARK_GRAY = RGBColor(60, 60, 60)

    # ==================== COVER / TITLE SECTION ====================
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(36)
    title_p.paragraph_format.space_after = Pt(12)
    run_title = title_p.add_run("Seasonal Agriculture Performance Analysis")
    run_title.font.name = 'Calibri'
    run_title.font.size = Pt(26)
    run_title.font.bold = True
    run_title.font.color.rgb = NAVY

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_p.paragraph_format.space_after = Pt(28)
    run_sub = sub_p.add_run("Major Project Report\nAICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026")
    run_sub.font.name = 'Calibri'
    run_sub.font.size = Pt(15)
    run_sub.font.bold = True
    run_sub.font.color.rgb = GREEN

    # Metadata Box Table
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Candidate Name", "[Your Name / Ansh]"),
        ("College / University", "[Your College / University Name]"),
        ("Internship Program", "AICTE | IBM SkillsBuild Data Analytics with AI"),
        ("Implementation Partner", "BharatCares (CSRBOX)"),
        ("Program Duration", "6 Weeks (17th August – 30th September 2026)"),
        ("Lead Trainer & Mentor", "Mr. Kartik Hooda")
    ]
    for i, (k, v) in enumerate(meta_data):
        row = meta_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.text = k
        c1.text = v
        c0.paragraphs[0].runs[0].font.bold = True
        c0.paragraphs[0].runs[0].font.size = Pt(11)
        c1.paragraphs[0].runs[0].font.size = Pt(11)
        set_cell_background(c0, "F0F4F8")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 80, 80, 120, 120)
        set_cell_margins(c1, 80, 80, 120, 120)

    doc.add_page_break()

    # ==================== TABLE OF CONTENTS SUMMARY ====================
    h1 = doc.add_heading("Executive Summary", level=1)
    h1.runs[0].font.color.rgb = NAVY

    p_exec = doc.add_paragraph(
        "Agricultural activities in India are fundamentally governed by seasonal weather cycles, monsoon dynamics, "
        "and resource availability. This major project report presents an empirical, end-to-end data analytics and machine learning "
        "investigation of a multi-state agricultural dataset comprising 4,000 farm observations across 8 states, 8 crops, and 3 distinct seasons: "
        "Kharif (Monsoon), Rabi (Winter), and Zaid (Summer)."
    )
    p_exec.runs[0].font.size = Pt(11)

    p_exec2 = doc.add_paragraph(
        "Through data preprocessing, domain-specific feature engineering, inferential hypothesis testing (One-Way ANOVA, Kruskal-Wallis H, "
        "Mann-Whitney U, Chi-Square), and supervised machine learning (Gradient Boosting Regressors achieving R² = 97.5% for Yield and R² = 98.1% for Profit), "
        "this project establishes critical seasonal performance benchmarks and develops data-driven policy recommendations for climate-resilient agriculture."
    )
    p_exec2.runs[0].font.size = Pt(11)

    # Key Findings Bullets
    doc.add_heading("Key Project Highlights:", level=2).runs[0].font.color.rgb = GREEN
    findings = [
        "Monsoon Primacy (Kharif): Delivers the highest average farm profit (INR 178,915; ROI 35.5%) driven by natural rainfall (852.1 mm) and superior water efficiency (5.89 t / 1000 m³).",
        "Winter Stability (Rabi): Characterized by steady yields (5.09 t/ha) and healthy profitability (INR 87,689; ROI 17.6%) supported by moderate temperatures (23.5°C) and suppressed disease risk (40.5%).",
        "The Summer Deficit (Zaid): Over 54% of summer farms operate at a net loss (mean profit: -INR 24,805; ROI -2.5%) due to intense summer heat (31.0°C), heavy supplemental water demands (6,420 m³), and reduced yields under flood irrigation.",
        "Micro-Irrigation as a Game Changer: Transitioning from Flood irrigation to Drip irrigation increases water productivity by 2.3x and turns summer losses (-INR 69,787) into positive earnings (+INR 21,291).",
        "Machine Learning Predictive Precision: Gradient Boosting models achieved 97.5% R² for Crop Yield prediction and 98.1% R² for Farm Profitability prediction."
    ]
    for f in findings:
        bp = doc.add_paragraph(f, style='List Bullet')
        bp.runs[0].font.size = Pt(10.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ==================== SECTION 1: PROBLEM STATEMENT ====================
    doc.add_heading("1. Problem Statement & Objectives", level=1).runs[0].font.color.rgb = NAVY
    doc.add_paragraph(
        "Agricultural activities are influenced by seasonal variations in environmental conditions, farming practices, "
        "resource availability, and market conditions. As a result, agricultural performance differs significantly from one season to another.\n\n"
        "However, raw agricultural data does not clearly explain how performance changes across seasons or what patterns can be observed "
        "in different seasonal conditions. The core objective of this project is to analyze the multi-state agricultural dataset and "
        "investigate seasonal differences in agricultural performance by identifying meaningful patterns, trends, relationships, "
        "and variations within the available data."
    )

    # ==================== SECTION 2: DATASET ARCHITECTURE ====================
    doc.add_heading("2. Dataset Architecture & Preprocessing", level=1).runs[0].font.color.rgb = NAVY
    doc.add_paragraph(
        "The dataset contains 4,000 farm records spanning 8 Indian states (Andhra Pradesh, Gujarat, Karnataka, Madhya Pradesh, "
        "Maharashtra, Punjab, Tamil Nadu, Telangana) and 8 crops (Chilli, Cotton, Groundnut, Maize, Pulses, Rice, Sugarcane, Wheat) "
        "across 28 original features."
    )

    # Data Cleaning logic
    doc.add_heading("2.1 Data Cleaning & Imputation Methodology", level=2).runs[0].font.color.rgb = GREEN
    doc.add_paragraph(
        "1. Yield_Tonnes_Ha (32 missing): Agronomic identity Yield = Production (Tonnes) / Farm Area (Ha) was used to mathematically reconstruct missing yields with exact precision.\n"
        "2. Rainfall_mm (48 missing): Imputed using the median rainfall of each specific (State, Season) cohort to preserve regional precipitation distributions.\n"
        "3. Soil_Moisture_pct (40 missing): Imputed using the median soil moisture of each (Crop, Season) cohort."
    )

    # Feature Engineering
    doc.add_heading("2.2 Feature Engineering", level=2).runs[0].font.color.rgb = GREEN
    doc.add_paragraph(
        "Engineered domain features include Profit Margin (%), Return on Investment (ROI %), Cost Per Hectare, Revenue Per Hectare, "
        "Profit Per Hectare, Water Economic Productivity (INR Revenue / m³ water), NPK Total Macronutrients, and Profitability Tiers."
    )

    # ==================== SECTION 3: STATISTICAL HYPOTHESIS TESTING ====================
    doc.add_heading("3. Inferential Statistical Hypothesis Testing", level=1).runs[0].font.color.rgb = NAVY
    doc.add_paragraph(
        "To establish whether observed seasonal variations are statistically significant or attributable to random chance, "
        "we conducted One-Way ANOVA (parametric), Kruskal-Wallis H tests (non-parametric), Chi-Square tests of independence, "
        "and Mann-Whitney U pairwise tests with Bonferroni correction."
    )

    # ANOVA Table
    anova_table = doc.add_table(rows=7, cols=6)
    anova_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Metric", "Kharif Mean", "Rabi Mean", "Zaid Mean", "ANOVA F", "Significant?"]
    for j, h in enumerate(headers):
        cell = anova_table.rows[0].cells[j]
        cell.text = h
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_background(cell, "D9E2EC")
        set_cell_margins(cell, 60, 60, 80, 80)

    anova_rows = [
        ("Rainfall (mm)", "852.11", "435.93", "299.34", "3448.02 (p<0.001)", "Yes"),
        ("Avg Temperature (°C)", "28.45", "23.49", "31.04", "2678.74 (p<0.001)", "Yes"),
        ("Relative Humidity (%)", "71.81", "57.89", "52.01", "1574.77 (p<0.001)", "Yes"),
        ("Water Efficiency (t/km³)", "5.89", "5.19", "4.41", "6.95 (p<0.001)", "Yes"),
        ("Pest/Disease Risk (%)", "54.47", "40.48", "38.22", "1049.47 (p<0.001)", "Yes"),
        ("Net Profit (INR)", "178,915", "87,689", "-24,805", "34.29 (p<0.001)", "Yes")
    ]
    for r_idx, r_data in enumerate(anova_rows, start=1):
        for c_idx, val in enumerate(r_data):
            cell = anova_table.rows[r_idx].cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            set_cell_margins(cell, 50, 50, 70, 70)
            if r_idx % 2 == 1:
                set_cell_background(cell, "F8F9FA")

    # Add Figure 1
    fig1 = os.path.join(figures_dir, 'seasonal_distributions.png')
    if os.path.exists(fig1):
        doc.add_paragraph().paragraph_format.space_before = Pt(8)
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.add_run().add_picture(fig1, width=Inches(6.0))
        p_caption = doc.add_paragraph("Figure 1: Seasonal distributions of Rainfall, Temperature, Humidity, and Sunlight Hours.")
        p_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_caption.runs[0].font.italic = True
        p_caption.runs[0].font.size = Pt(9)

    # ==================== SECTION 4: IRRIGATION & WATER MANAGEMENT ====================
    doc.add_heading("4. Resource Usage & Irrigation Efficiency", level=1).runs[0].font.color.rgb = NAVY
    doc.add_paragraph(
        "Water resource analysis demonstrated that Drip irrigation is the single most transformative intervention. "
        "While traditional Flood irrigation causes massive financial distress in summer (-INR 69,787 per farm), "
        "Drip irrigation maintains high yield and positive net operating income (+INR 21,291)."
    )

    fig2 = os.path.join(figures_dir, 'irrigation_efficiency.png')
    if os.path.exists(fig2):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.add_run().add_picture(fig2, width=Inches(6.0))
        p_caption2 = doc.add_paragraph("Figure 2: Water efficiency and Net Farm Profit by Irrigation Method across Seasons.")
        p_caption2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_caption2.runs[0].font.italic = True
        p_caption2.runs[0].font.size = Pt(9)

    # ==================== SECTION 5: MACHINE LEARNING MODELING ====================
    doc.add_heading("5. Machine Learning Predictive Modeling", level=1).runs[0].font.color.rgb = NAVY
    doc.add_paragraph(
        "We trained and evaluated supervised learning models to predict two key targets: (1) Crop Yield (Tonnes/Ha) and (2) Farm Profitability (INR). "
        "Gradient Boosting Regressor significantly outperformed traditional linear approaches, demonstrating robust predictive capability across 5-Fold cross validation."
    )

    ml_table = doc.add_table(rows=4, cols=5)
    ml_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    ml_headers = ["Target Variable", "Algorithm", "Test R²", "Test MAE", "5-Fold CV R²"]
    for j, h in enumerate(ml_headers):
        cell = ml_table.rows[0].cells[j]
        cell.text = h
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_background(cell, "D9E2EC")
        set_cell_margins(cell, 60, 60, 80, 80)

    ml_data = [
        ("Yield (Tonnes/Ha)", "Gradient Boosting", "0.9751", "0.6412 t/ha", "0.9736"),
        ("Yield (Tonnes/Ha)", "Random Forest", "0.9628", "0.7539 t/ha", "0.9616"),
        ("Farm Profit (INR)", "Gradient Boosting", "0.9814", "INR 48,707", "0.9787")
    ]
    for r_idx, r_vals in enumerate(ml_data, start=1):
        for c_idx, val in enumerate(r_vals):
            cell = ml_table.rows[r_idx].cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            set_cell_margins(cell, 50, 50, 70, 70)
            if r_idx % 2 == 1:
                set_cell_background(cell, "F8F9FA")

    fig3 = os.path.join(figures_dir, 'feature_importance.png')
    if os.path.exists(fig3):
        p_img3 = doc.add_paragraph()
        p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img3.add_run().add_picture(fig3, width=Inches(5.5))
        p_caption3 = doc.add_paragraph("Figure 3: Feature importance weights of Crop Yield drivers from Gradient Boosting model.")
        p_caption3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_caption3.runs[0].font.italic = True
        p_caption3.runs[0].font.size = Pt(9)

    # ==================== SECTION 6: 12 KEY RESEARCH QUESTIONS ====================
    doc.add_page_break()
    doc.add_heading("6. Answers to the 12 Major Project Research Questions", level=1).runs[0].font.color.rgb = NAVY

    questions_data = [
        ("Q1: How does agricultural performance vary across seasons?",
         "Agricultural performance varies significantly. Kharif records the highest average yields (5.63 t/ha) and profit (INR 178,915). Rabi maintains yield stability (5.09 t/ha) and healthy profit (INR 87,689). Zaid exhibits the lowest yields (4.63 t/ha) and net negative average profits (-INR 24,805) due to heat stress and heavy irrigation overheads."),
        ("Q2: What major seasonal patterns can be observed?",
         "Monsoon surge in Kharif (852mm rainfall, 71.8% humidity) supports high biomass but elevates disease/pest risk to 54.5%. Winter conditions in Rabi (23.5°C) suppress disease risk to 40.5%. Summer in Zaid has high heat (31.0°C), low rainfall (299mm), and high evaporation."),
        ("Q3: Which characteristics change between seasons?",
         "Climatic and biological parameters vary dynamically across seasons (p < 0.0001 for Rainfall, Temperature, Humidity, Soil Moisture, and Pest Risk). In contrast, fertilizer application (184–187 kg/ha) and soil macronutrients remain static, showing uniform farmer dosing habits irrespective of season."),
        ("Q4: What differences exist between agricultural activities in different seasons?",
         "Kharif activities focus on monsoon sowing, flood drainage, weed management, and intensive chemical/biological pest protection. Rabi activities revolve around supplemental winter irrigation, cool-weather maintenance, and dry harvesting. Zaid requires daily supplemental irrigation and heat protection."),
        ("Q5: Are there noticeable variations in resource usage across seasons?",
         "Yes. Water consumption reaches its highest levels in Zaid (6,420 m³) despite yielding the lowest harvest, dragging water efficiency down to 4.41 t/1000m³. Kharif achieves peak water efficiency of 5.89 t/1000m³ utilizing monsoon rainfall."),
        ("Q6: Are there relationships between seasonal environmental conditions and agricultural performance?",
         "Yes. Disease/pest risk correlates strongly with Rainfall (r = 0.624) and Humidity (r = 0.545). Excessive summer heat without drip irrigation directly depresses water productivity and farm returns."),
        ("Q7: How do economic outcomes vary across seasons?",
         "Kharif generates the highest farm revenues (INR 710,719) and profit margins (ROI 35.5%). Rabi provides solid returns (ROI 17.6%). Zaid suffers an average ROI of -2.5%, with 54.2% of farms recording net operating losses."),
        ("Q8: Are some seasonal patterns consistent across different regions or categories?",
         "Yes. Across all 8 monitored states, Kharif is consistently the most lucrative season, and Zaid is the least profitable. Furthermore, Drip irrigation consistently outperforms flood irrigation across all states and seasons."),
        ("Q9: Are there unusual or unexpected seasonal patterns?",
         "Zaid farms experience net losses despite receiving peak daily sunlight (8.18 hrs/day) and standard fertilizer inputs, driven by high irrigation pumping costs and excessive evapotranspiration under inefficient flood irrigation."),
        ("Q10: What insights can be derived from the observed seasonal differences?",
         "Applying uniform input packages year-round leads to resource misallocation. High-value cash crops (Chilli, Sugarcane) maintain positive margins throughout all seasons, whereas staple grain farmers need subsidized water or price support to remain viable."),
        ("Q11: What conclusions can reasonably be drawn from the available data?",
         "Seasonal factors significantly drive agricultural outcomes (p < 0.0001). Precision micro-irrigation is the single most transformative intervention, turning summer farm losses (-INR 69k under flood) into positive profits (+INR 21k under drip). Gradient Boosting algorithms forecast yield and profit with high accuracy (R² > 97%)."),
        ("Q12: How could the findings support better seasonal agricultural planning?",
         "(a) Subsidize 100% drip irrigation adoption for summer cultivation; (b) Issue prophylactic pest warnings during early Kharif when humidity exceeds 70%; (c) Discourage water-intensive flood crops in Zaid in favor of drought-tolerant pulses or vegetables; (d) Calibrate seasonal agri-credit limits based on empirical seasonal ROI.")
    ]

    for q, a in questions_data:
        qp = doc.add_paragraph()
        q_run = qp.add_run(q)
        q_run.bold = True
        q_run.font.size = Pt(11)
        q_run.font.color.rgb = GREEN
        
        ap = doc.add_paragraph(a)
        ap.runs[0].font.size = Pt(10)
        ap.paragraph_format.space_after = Pt(8)

    # ==================== SECTION 7: RECOMMENDATIONS & POLICY ====================
    doc.add_heading("7. Strategic Policy & Farm Recommendations", level=1).runs[0].font.color.rgb = NAVY
    recs = [
        "Mandate Micro-Irrigation for Summer Crops: Direct PMKSY micro-irrigation subsidies specifically to farmers cultivating summer crops.",
        "Establish Weather-Indexed Early Pest Warnings: Deploy real-time mobile advisory alerts to farmers when relative humidity exceeds 70% during the monsoon.",
        "Restructure Seasonal Agricultural Credit Limits: Shift banking credit limits to reflect seasonal ROI dynamics rather than fixed annual ceilings.",
        "Promote Summer Crop Diversification: Shift farmers from flood-irrigated cereal crops toward drought-tolerant pulses (moong, urad) and vegetables."
    ]
    for r in recs:
        doc.add_paragraph(r, style='List Bullet').runs[0].font.size = Pt(10.5)

    # Save document
    doc.save(output_docx_path)
    print(f"[SUCCESS] Generated Word document report at: {output_docx_path}")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    figures_dir = os.path.join(base_dir, 'reports', 'figures')
    
    # Generate both requested naming conventions
    docx1 = os.path.join(base_dir, 'YourName_ProjectReport.docx')
    docx2 = os.path.join(base_dir, 'Ansh_ProjectReport.docx')
    
    generate_report(docx1, figures_dir)
    generate_report(docx2, figures_dir)

if __name__ == '__main__':
    main()
