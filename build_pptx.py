from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import os

VISUALS = r"d:\Aniket\majja\visuals"
OUT_DIR = r"d:\Aniket\majja"

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

DARK_BG = RGBColor(13, 17, 23)
NAVY = RGBColor(27, 42, 74)
ACCENT = RGBColor(88, 166, 255)
WHITE = RGBColor(255, 255, 255)
LIGHT_GREY = RGBColor(201, 209, 217)
GREEN = RGBColor(63, 185, 80)
RED = RGBColor(215, 25, 28)
ORANGE = RGBColor(245, 166, 35)

def hex2rgb(h):
    h=h.lstrip('#')
    return RGBColor(int(h[0:2],16),int(h[2:4],16),int(h[4:6],16))

blank_layout = prs.slide_layouts[6]  # completely blank

def add_bg(slide, color=DARK_BG):
    bg = slide.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = color
    bg.line.fill.background()

def add_rect(slide, l, t, w, h, color, alpha=None):
    sh = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = color
    sh.line.fill.background()
    return sh

def add_txt(slide, text, l, t, w, h, size=18, bold=False, color=WHITE, align=PP_ALIGN.LEFT, italic=False):
    txb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = txb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = text
    run.font.size = Pt(size); run.font.bold = bold; run.font.italic = italic
    run.font.color.rgb = color
    return txb

def add_img(slide, path, l, t, w, h):
    if os.path.exists(path):
        slide.shapes.add_picture(path, Inches(l), Inches(t), Inches(w), Inches(h))

# ── SLIDE 1: Title ─────────────────────────────────────────────────────────────
sl1 = prs.slides.add_slide(blank_layout)
add_bg(sl1, DARK_BG)
# Left accent bar
add_rect(sl1, 0, 0, 0.06, 7.5, ACCENT)
# Top gradient strip
add_rect(sl1, 0.06, 0, 13.27, 0.08, NAVY)
# Fire emoji label
add_txt(sl1, "🔥  DISASTER MANAGEMENT & MITIGATION — GROUP PROJECT", 0.3, 0.15, 12, 0.5, size=11, color=ACCENT, bold=True)
# Main title
add_txt(sl1, "Wildfire Susceptibility Mapping &\nDisaster Risk Analysis", 0.3, 0.8, 9, 1.8, size=38, bold=True, color=WHITE)
# Subtitle
add_txt(sl1, "Sanjay Gandhi National Park, Mumbai, Maharashtra", 0.3, 2.65, 9, 0.6, size=20, color=ACCENT, bold=True)
# Team box
add_rect(sl1, 0.3, 3.4, 5.5, 2.5, NAVY)
info_lines = [
    ("Team Name:", "FireWatch Analysts"),
    ("Study Area:", "SGNP, Mumbai (104 km²)"),
    ("Methodology:", "GIS + Multi-Criteria AHP"),
    ("Tools Used:", "ArcGIS Pro / Python GIS"),
    ("Date:", "October 2026"),
]
for i, (k, v) in enumerate(info_lines):
    add_txt(sl1, f"{k}", 0.4, 3.55+i*0.42, 1.8, 0.42, size=11, color=ACCENT, bold=True)
    add_txt(sl1, f"{v}", 2.3, 3.55+i*0.42, 3.3, 0.42, size=11, color=LIGHT_GREY)
# Map thumbnail right
add_img(sl1, os.path.join(VISUALS,"map_01_study_area.png"), 6.5, 0.6, 6.5, 6.5)
# Bottom bar
add_rect(sl1, 0.06, 7.1, 13.27, 0.08, ACCENT)

# ── SLIDE 2: Introduction & Problem Statement ───────────────────────────────────
sl2 = prs.slides.add_slide(blank_layout)
add_bg(sl2, DARK_BG)
add_rect(sl2, 0, 0, 0.06, 7.5, RED)
add_rect(sl2, 0.06, 0, 13.27, 0.08, NAVY)
add_txt(sl2, "INTRODUCTION & PROBLEM STATEMENT", 0.3, 0.18, 12, 0.5, size=11, color=RED, bold=True)
add_txt(sl2, "Background & Research Problem", 0.3, 0.55, 10, 0.7, size=28, bold=True, color=WHITE)

bullets_intro = [
    "Sanjay Gandhi National Park (SGNP) spans 104 km² in northern Mumbai — the world's largest urban national park.",
    "Surrounded by 20+ million residents, it represents a critical Urban-Forest Interface (UFI) with extreme fire risk.",
    "Dry season (Nov–May) creates high fuel loads; recurring brush fires threaten both ecology and human settlements.",
    "Despite recurring threats, no systematic spatial wildfire risk map exists for emergency response planning.",
    "This study applies GIS + Multi-Criteria Decision Analysis (MCDA) to create a comprehensive fire risk framework.",
]
for i, b in enumerate(bullets_intro):
    add_rect(sl2, 0.3, 1.45+i*0.95, 0.06, 0.7, ACCENT)
    add_txt(sl2, b, 0.55, 1.42+i*0.95, 8.5, 0.8, size=13, color=LIGHT_GREY)

add_img(sl2, os.path.join(VISUALS,"map_01_study_area.png"), 9.2, 1.0, 3.8, 5.8)
add_rect(sl2, 0.06, 7.1, 13.27, 0.08, RED)

# ── SLIDE 3: Research Objectives ────────────────────────────────────────────────
sl3 = prs.slides.add_slide(blank_layout)
add_bg(sl3, DARK_BG)
add_rect(sl3, 0, 0, 0.06, 7.5, GREEN)
add_txt(sl3, "RESEARCH OBJECTIVES", 0.3, 0.18, 12, 0.5, size=11, color=GREEN, bold=True)
add_txt(sl3, "What This Study Aims to Achieve", 0.3, 0.55, 10, 0.7, size=28, bold=True, color=WHITE)

objectives = [
    ("01", "Identify", "Identify major environmental & human factors driving wildfire susceptibility in SGNP"),
    ("02", "Develop", "Develop a GIS-based Wildfire Susceptibility Zonation framework using 5 conditioning factors"),
    ("03", "Map", "Map exposure & risk hotspots where high susceptibility intersects human settlements"),
    ("04", "Assess", "Assess emergency evacuation accessibility and identify priority zones for response planning"),
    ("05", "Recommend", "Provide actionable disaster-mitigation & preparedness recommendations for fire management"),
    ("06", "Demonstrate", "Demonstrate how spatial analysis can support wildfire disaster-management decisions"),
]
colors_obj = [hex2rgb('#58a6ff'),hex2rgb('#3fb950'),hex2rgb('#d29922'),hex2rgb('#f85149'),hex2rgb('#bc8cff'),hex2rgb('#39d353')]
for i, (num, verb, desc) in enumerate(objectives):
    col = i % 3; row = i // 3
    x = 0.3 + col * 4.25; y = 1.6 + row * 2.4
    add_rect(sl3, x, y, 3.9, 2.1, NAVY)
    add_txt(sl3, num, x+0.1, y+0.1, 0.8, 0.6, size=22, bold=True, color=colors_obj[i])
    add_txt(sl3, verb, x+0.8, y+0.12, 2.8, 0.5, size=14, bold=True, color=WHITE)
    add_txt(sl3, desc, x+0.1, y+0.65, 3.6, 1.25, size=11, color=LIGHT_GREY)
add_rect(sl3, 0.06, 7.1, 13.27, 0.08, GREEN)

# ── SLIDE 4: Study Area & Data Sources ──────────────────────────────────────────
sl4 = prs.slides.add_slide(blank_layout)
add_bg(sl4, DARK_BG)
add_rect(sl4, 0, 0, 0.06, 7.5, ORANGE)
add_txt(sl4, "STUDY AREA & DATA SOURCES", 0.3, 0.18, 12, 0.5, size=11, color=ORANGE, bold=True)
add_txt(sl4, "Sanjay Gandhi National Park — Geographic Profile", 0.3, 0.55, 8, 0.7, size=22, bold=True, color=WHITE)

facts = [
    ("Area", "104 km²"),("Location", "19.22°N, 72.91°E"),("Admin", "Mumbai, Maharashtra"),
    ("Elevation", "12 – 480 m ASL"),("Forest Type", "Tropical Deciduous"),("Dry Season", "November – May"),
]
for i, (k, v) in enumerate(facts):
    c = i % 2; r = i // 2
    x = 0.3 + c*3.1; y = 1.5 + r*0.9
    add_rect(sl4, x, y, 2.8, 0.75, NAVY)
    add_txt(sl4, k, x+0.1, y+0.05, 1.2, 0.35, size=10, color=ACCENT, bold=True)
    add_txt(sl4, v, x+0.1, y+0.36, 2.5, 0.35, size=12, color=WHITE, bold=True)

# Data table
add_txt(sl4, "Data Sources", 0.3, 4.4, 5, 0.4, size=13, bold=True, color=ACCENT)
data_rows = [
    ["DEM", "Raster (30m)", "SRTM / NASA EarthData"],
    ["Road Network", "Vector (Lines)", "OpenStreetMap"],
    ["Settlements", "Vector (Points)", "OSM / Census India"],
    ["NDVI/Vegetation", "Raster (250m)", "MODIS Terra"],
    ["Park Boundary", "Vector (Polygon)", "Maharashtra Forest Dept."],
]
headers = ["Data Layer", "Type & Resolution", "Source"]
for j, h in enumerate(headers):
    x = [0.3, 3.1, 6.6][j]; w = [2.7, 3.4, 3.2][j]
    add_rect(sl4, x, 4.85, w-0.05, 0.38, hex2rgb('#1c2128'))
    add_txt(sl4, h, x+0.05, 4.87, w-0.1, 0.34, size=10, bold=True, color=ACCENT)
for r_i, row in enumerate(data_rows):
    bg_col = NAVY if r_i%2==0 else hex2rgb('#0d1117')
    for j, cell in enumerate(row):
        x = [0.3, 3.1, 6.6][j]; w = [2.7, 3.4, 3.2][j]
        add_rect(sl4, x, 5.28+r_i*0.38, w-0.05, 0.36, bg_col)
        add_txt(sl4, cell, x+0.05, 5.30+r_i*0.38, w-0.1, 0.32, size=10, color=LIGHT_GREY)
add_img(sl4, os.path.join(VISUALS,"map_01_study_area.png"), 6.5, 1.3, 6.5, 5.6)
add_rect(sl4, 0.06, 7.1, 13.27, 0.08, ORANGE)

# ── SLIDE 5: Methodology ────────────────────────────────────────────────────────
sl5 = prs.slides.add_slide(blank_layout)
add_bg(sl5, DARK_BG)
add_rect(sl5, 0, 0, 0.06, 7.5, hex2rgb('#bc8cff'))
add_txt(sl5, "RESEARCH METHODOLOGY", 0.3, 0.18, 12, 0.5, size=11, color=hex2rgb('#bc8cff'), bold=True)
add_txt(sl5, "Multi-Criteria GIS Workflow — Step by Step", 0.3, 0.55, 9, 0.7, size=24, bold=True, color=WHITE)
add_img(sl5, os.path.join(VISUALS,"methodology_workflow.png"), 0.2, 1.2, 5.8, 6.0)
# Steps right
steps_r = [
    ("1. Data Collection", "SRTM DEM, OSM Roads/Settlements, MODIS NDVI", "#58a6ff"),
    ("2. Pre-Processing", "Project to WGS84, Clip to SGNP, Resample 30m", "#3fb950"),
    ("3. Reclassification", "Each factor classified into 1–5 vulnerability scale", "#d29922"),
    ("4. Weighted Overlay", "WSI = 0.40×Slope+0.25×NDVI+0.15×Elev+...", "#f85149"),
    ("5. Risk Zonation", "Susceptibility × Exposure = Combined Risk Map", "#bc8cff"),
    ("6. Evacuation Plan", "Network analysis, route accessibility, safe zones", "#39d353"),
]
for i, (title, desc, col) in enumerate(steps_r):
    add_rect(sl5, 6.3, 1.2+i*0.98, 6.8, 0.88, NAVY)
    add_rect(sl5, 6.3, 1.2+i*0.98, 0.05, 0.88, hex2rgb(col))
    add_txt(sl5, title, 6.5, 1.22+i*0.98, 6.3, 0.38, size=12, bold=True, color=WHITE)
    add_txt(sl5, desc, 6.5, 1.58+i*0.98, 6.3, 0.38, size=10, color=LIGHT_GREY)
add_rect(sl5, 0.06, 7.1, 13.27, 0.08, hex2rgb('#bc8cff'))

# ── SLIDE 6: Susceptibility Map ──────────────────────────────────────────────────
sl6 = prs.slides.add_slide(blank_layout)
add_bg(sl6, DARK_BG)
add_rect(sl6, 0, 0, 0.06, 7.5, RED)
add_txt(sl6, "FINDINGS — MAP 1 & MAP 2", 0.3, 0.18, 12, 0.5, size=11, color=RED, bold=True)
add_txt(sl6, "Wildfire Susceptibility Zonation Results", 0.3, 0.55, 9, 0.7, size=24, bold=True, color=WHITE)
add_img(sl6, os.path.join(VISUALS,"map_02_wildfire_susceptibility.png"), 0.2, 1.2, 5.8, 5.8)
key_finds = [
    ("Very High (9.5%)", "9.9 km² — Steep slopes + High NDVI periphery near settlements", "#d7191c"),
    ("High (19.7%)", "20.5 km² — Degraded areas near Borivali & Dahisar gates", "#fdae61"),
    ("Moderate (28.1%)", "29.2 km² — Mixed forest-urban transition zones", "#e6e600"),
    ("Low (24.5%)", "25.4 km² — Dense core forest with low ignition probability", "#a6d96a"),
    ("Very Low (18.2%)", "18.9 km² — Core forest & water bodies", "#1a9641"),
]
add_txt(sl6, "Key Findings:", 6.3, 1.2, 6, 0.4, size=13, bold=True, color=ACCENT)
for i,(cls,desc,col) in enumerate(key_finds):
    add_rect(sl6, 6.3, 1.75+i*1.05, 0.18, 0.85, hex2rgb(col))
    add_txt(sl6, cls, 6.6, 1.77+i*1.05, 6.3, 0.38, size=12, bold=True, color=WHITE)
    add_txt(sl6, desc, 6.6, 2.10+i*1.05, 6.3, 0.38, size=10, color=LIGHT_GREY)
add_img(sl6, os.path.join(VISUALS,"chart_01_factor_weights.png"), 6.1, 6.2, 6.9, 1.1)
add_rect(sl6, 0.06, 7.1, 13.27, 0.08, RED)

# ── SLIDE 7: Risk & Evacuation ─────────────────────────────────────────────────
sl7 = prs.slides.add_slide(blank_layout)
add_bg(sl7, DARK_BG)
add_rect(sl7, 0, 0, 0.06, 7.5, hex2rgb('#f85149'))
add_txt(sl7, "FINDINGS — MAP 3 & MAP 4", 0.3, 0.18, 12, 0.5, size=11, color=hex2rgb('#f85149'), bold=True)
add_txt(sl7, "Risk Exposure & Evacuation Accessibility", 0.3, 0.55, 9, 0.6, size=24, bold=True, color=WHITE)
add_img(sl7, os.path.join(VISUALS,"map_03_wildfire_risk_exposure.png"), 0.15, 1.2, 6.4, 5.8)
add_img(sl7, os.path.join(VISUALS,"map_04_evacuation_accessibility.png"), 6.8, 1.2, 6.4, 5.8)
# Labels
add_txt(sl7, "Map 3: Risk Exposure", 0.15, 7.0, 6.4, 0.38, size=11, bold=True, color=hex2rgb('#f46d43'), align=PP_ALIGN.CENTER)
add_txt(sl7, "Map 4: Evacuation Accessibility", 6.8, 7.0, 6.4, 0.38, size=11, bold=True, color=hex2rgb('#fde725'), align=PP_ALIGN.CENTER)
add_rect(sl7, 0.06, 7.1, 13.27, 0.08, hex2rgb('#f85149'))

# ── SLIDE 8: Results & Recommendations ─────────────────────────────────────────
sl8 = prs.slides.add_slide(blank_layout)
add_bg(sl8, DARK_BG)
add_rect(sl8, 0, 0, 0.06, 7.5, GREEN)
add_txt(sl8, "RESULTS, DISCUSSION & RECOMMENDATIONS", 0.3, 0.18, 12, 0.5, size=11, color=GREEN, bold=True)
add_txt(sl8, "Conclusion & Actionable Mitigation Plan", 0.3, 0.55, 9, 0.6, size=24, bold=True, color=WHITE)

findings_l = [
    ("29.2 km²", "of SGNP under High/Very High wildfire susceptibility"),
    ("17.4 km²", "of human settlements exposed to high risk fire zones"),
    ("5 Hotspots", "identified at critical urban-forest interface gates"),
    ("3 Safe Zones", "mapped for emergency assembly during evacuation"),
]
add_txt(sl8, "Key Statistical Findings", 0.3, 1.3, 5.5, 0.4, size=13, bold=True, color=ACCENT)
for i, (val, desc) in enumerate(findings_l):
    add_rect(sl8, 0.3, 1.8+i*1.2, 5.5, 1.05, NAVY)
    add_txt(sl8, val, 0.5, 1.83+i*1.2, 2, 0.5, size=20, bold=True, color=ACCENT)
    add_txt(sl8, desc, 0.5, 2.25+i*1.2, 5, 0.45, size=11, color=LIGHT_GREY)

recs = [
    ("🌿", "Buffer Zones", "Physical firebreaks along highest-risk urban-forest interfaces before dry season"),
    ("🔥", "Fuel Management", "Controlled removal of dry brush in Very High susceptibility zones"),
    ("🚧", "Access Control", "Restrict human access to high-risk zones during Nov–May dry months"),
    ("📡", "Surveillance", "Deploy thermal cameras/drone monitoring at peripheral hotspots"),
    ("🚒", "Pre-positioning", "Fire brigade assets pre-positioned based on evacuation priority maps"),
]
add_txt(sl8, "Mitigation Recommendations", 6.2, 1.3, 6.8, 0.4, size=13, bold=True, color=GREEN)
for i, (icon, title, desc) in enumerate(recs):
    add_rect(sl8, 6.2, 1.8+i*1.05, 6.8, 0.95, NAVY)
    add_txt(sl8, icon, 6.3, 1.83+i*1.05, 0.5, 0.6, size=18)
    add_txt(sl8, title, 6.85, 1.83+i*1.05, 5.8, 0.38, size=12, bold=True, color=WHITE)
    add_txt(sl8, desc, 6.85, 2.15+i*1.05, 6.0, 0.55, size=10, color=LIGHT_GREY)

add_rect(sl8, 0.06, 7.1, 13.27, 0.08, GREEN)

# Save
out_path = os.path.join(OUT_DIR, "SGNP_Wildfire_Presentation.pptx")
prs.save(out_path)
print(f"PPTX saved: {out_path}")
print(f"Slide count: {len(prs.slides)}")
import os
sz = os.path.getsize(out_path)
print(f"File size: {sz:,} bytes ({sz/1024:.1f} KB)")