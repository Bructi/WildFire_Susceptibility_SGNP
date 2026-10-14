import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, ArrowStyle
import matplotlib.patheffects as pe

OUT = r"d:\Aniket\majja\visuals"
os.makedirs(OUT, exist_ok=True)

def generate_pipeline_diagram():
    fig = plt.figure(figsize=(15, 9), dpi=200, facecolor="#0f172a")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor("#0f172a")
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Title
    ax.text(7.5, 8.45, "MULTI-CRITERIA WILDFIRE SYSTEM ARCHITECTURE & LOGISTICS PIPELINE",
            ha="center", va="center", color="#38bdf8", fontsize=15, fontweight="black",
            path_effects=[pe.withStroke(linewidth=1.5, foreground="#0369a1")])
    ax.text(7.5, 8.08, "Sanjay Gandhi National Park (SGNP) — Disaster Management & Mitigation Framework",
            ha="center", va="center", color="#94a3b8", fontsize=10.5, fontweight="medium")

    # 3 Main Phase Columns
    # Phase 1: Data Ingestion
    # Phase 2: Multi-Criteria Evaluation (AHP)
    # Phase 3: Risk & Evacuation Logistics
    cols = [
        {
            "num": "PHASE 01",
            "title": "DATA INGESTION & HARMONIZATION",
            "subtitle": "Satellite Remote Sensing & Vector Geodatabase",
            "x": 0.6, "y": 0.7, "w": 4.1, "h": 6.8,
            "theme": "#0284c7", "card_bg": "#1e293b", "border": "#38bdf8",
            "items": [
                ("SRTM 30m Digital Elevation Model", "Elevation relief (12m - 468m AMSL) & continuous slope surface"),
                ("Sentinel-2 / Landsat NDVI", "Vegetation fuel dryness fraction & canopy biomass density"),
                ("OSM & Municipal Urban Footprints", "500m WUI buffer polygons & peripheral human settlements"),
                ("Forest Boundary & Hydrology Masks", "SGNP legal border (103.84 km²), Tulsi & Vihar water bodies")
            ]
        },
        {
            "num": "PHASE 02",
            "title": "ANALYTICAL HIERARCHY PROCESS (AHP)",
            "subtitle": "Pairwise Multi-Criteria Evaluation (MCE)",
            "x": 5.45, "y": 0.7, "w": 4.1, "h": 6.8,
            "theme": "#d97706", "card_bg": "#1e293b", "border": "#f59e0b",
            "items": [
                ("Pairwise Comparison Matrix", "Expert-weighted Saaty rating across 4 critical drivers"),
                ("Eigenvector Weight Derivation", "Slope (35%) • Fuel/NDVI (30%) • WUI (25%) • Roads (10%)"),
                ("Mathematical Consistency Audit", "CI = 0.038 | RI = 0.900 | CR = 0.042 (< 0.10 => Verified)"),
                ("Weighted Raster Overlay (WSI)", "Continuous 0.0 - 1.0 Wildfire Susceptibility Index & 5 Classes")
            ]
        },
        {
            "num": "PHASE 03",
            "title": "RISK ZONATION & EVACUATION",
            "subtitle": "Disaster Exposure & Tactical Suppression",
            "x": 10.3, "y": 0.7, "w": 4.1, "h": 6.8,
            "theme": "#059669", "card_bg": "#1e293b", "border": "#10b981",
            "items": [
                ("5-Tier Susceptibility Zonation", "Very Low (18.2%) to Very High (9.5% critical ridge zone)"),
                ("Hazard x Exposure Risk Matrix", "Perimeter vulnerability intersecting peripheral communities"),
                ("Emergency Suppression Network", "4 Municipal Fire Stations with 15/30-min drive perimeters"),
                ("Tactical Evacuation Logistics", "3 Lookout Towers (88.4% optical view) & Safe Staging Zones")
            ]
        }
    ]

    for col in cols:
        # Outer Card
        outer_box = FancyBboxPatch((col["x"], col["y"]), col["w"], col["h"],
                                   boxstyle="round,pad=0.08", facecolor=col["card_bg"],
                                   edgecolor=col["border"], linewidth=2.0, zorder=2)
        ax.add_patch(outer_box)

        # Header Badge
        badge_box = FancyBboxPatch((col["x"] + 0.2, col["y"] + col["h"] - 0.7), col["w"] - 0.4, 0.55,
                                   boxstyle="round,pad=0.04", facecolor=col["theme"],
                                   edgecolor="#ffffff", linewidth=1.0, zorder=3)
        ax.add_patch(badge_box)
        ax.text(col["x"] + col["w"]/2, col["y"] + col["h"] - 0.32, col["num"],
                ha="center", va="center", color="#ffffff", fontsize=8.5, fontweight="black", zorder=4)
        ax.text(col["x"] + col["w"]/2, col["y"] + col["h"] - 0.52, col["title"],
                ha="center", va="center", color="#ffffff", fontsize=9.2, fontweight="black", zorder=4)

        ax.text(col["x"] + col["w"]/2, col["y"] + col["h"] - 0.95, col["subtitle"],
                ha="center", va="center", color="#cbd5e1", fontsize=8.2, fontweight="medium", zorder=4)

        # Separator line
        ax.plot([col["x"] + 0.3, col["x"] + col["w"] - 0.3],
                [col["y"] + col["h"] - 1.15, col["y"] + col["h"] - 1.15],
                color=col["border"], lw=1.2, alpha=0.5, zorder=3)

        # 4 Items inside column
        item_y_starts = [col["y"] + 4.25, col["y"] + 2.85, col["y"] + 1.45, col["y"] + 0.05]
        for idx, (head, desc) in enumerate(col["items"]):
            iy = item_y_starts[idx]
            ibox = FancyBboxPatch((col["x"] + 0.22, iy), col["w"] - 0.44, 1.15,
                                  boxstyle="round,pad=0.04", facecolor="#0f172a",
                                  edgecolor="#334155", linewidth=1.2, zorder=3)
            ax.add_patch(ibox)
            
            # Bullet step tag
            c = Circle((col["x"] + 0.45, iy + 0.8), 0.16, facecolor=col["theme"], edgecolor="#ffffff", lw=0.8, zorder=4)
            ax.add_patch(c)
            ax.text(col["x"] + 0.45, iy + 0.8, str(idx+1), ha="center", va="center",
                    color="#ffffff", fontsize=7.5, fontweight="bold", zorder=5)

            ax.text(col["x"] + 0.72, iy + 0.8, head, color="#f8fafc", fontsize=8.8, fontweight="bold", va="center", zorder=4)
            ax.text(col["x"] + 0.35, iy + 0.35, desc, color="#94a3b8", fontsize=7.5, va="center", zorder=4)

    # Connecting Arrows between Columns
    # Arrow 1 -> 2
    ax.annotate("", xy=(5.35, 4.1), xytext=(4.80, 4.1),
                arrowprops=dict(facecolor="#f59e0b", edgecolor="#ffffff", width=3.5, headwidth=11, headlength=12),
                zorder=10)
    ax.text(5.08, 4.4, "AHP MODEL", ha="center", color="#f59e0b", fontsize=7.8, fontweight="black")

    # Arrow 2 -> 3
    ax.annotate("", xy=(10.20, 4.1), xytext=(9.65, 4.1),
                arrowprops=dict(facecolor="#10b981", edgecolor="#ffffff", width=3.5, headwidth=11, headlength=12),
                zorder=10)
    ax.text(9.92, 4.4, "ZONATION", ha="center", color="#10b981", fontsize=7.8, fontweight="black")

    # Footer banner
    foot_box = FancyBboxPatch((0.6, 0.08), 13.8, 0.42, boxstyle="round,pad=0.03",
                              facecolor="#1e293b", edgecolor="#334155", lw=1.0, zorder=2)
    ax.add_patch(foot_box)
    ax.text(7.5, 0.28, "Verified Multi-Criteria AHP Framework • Mathematical Consistency Ratio CR = 0.042 < 0.10 • Fully Integrated GIS Geodatabase",
            ha="center", va="center", color="#38bdf8", fontsize=8.5, fontweight="bold", zorder=3)

    out_path = os.path.join(OUT, "system_architecture_pipeline.png")
    plt.savefig(out_path, dpi=200, facecolor=fig.get_facecolor())
    plt.close()
    print("Generated:", out_path)

def generate_arcgis_workflow_diagram():
    fig = plt.figure(figsize=(15, 7.5), dpi=200, facecolor="#0f172a")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor("#0f172a")
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(7.5, 6.95, "ARCGIS PRO FAIL-SAFE ZERO-CRASH LAUNCH WORKFLOW",
            ha="center", va="center", color="#38bdf8", fontsize=15, fontweight="black",
            path_effects=[pe.withStroke(linewidth=1.5, foreground="#0369a1")])
    ax.text(7.5, 6.55, "Universal Step-by-Step Procedure for 100% Reliable Execution Across Any ArcGIS Pro Version (2.8 - 3.4)",
            ha="center", va="center", color="#94a3b8", fontsize=10.0, fontweight="medium")

    steps = [
        ("1", "NEW BLANK MAP", "Launch ArcGIS Pro\nSelect 'Map' blank template\nAvoid corrupt APRX schemas", "#0284c7"),
        ("2", "FOLDER LINK", "Open Catalog Pane\nRight-click 'Folders'\nConnect to project/ directory", "#3b82f6"),
        ("3", "IMPORT LAYERS", "Drag GeoTIFF Rasters &\nShapefiles from project/\nDirect OGC standard binding", "#6366f1"),
        ("4", "BUILD PYRAMIDS", "Prompt: 'Build pyramids?'\nALWAYS CLICK YES!\nPrevents RAM overload crash", "#d97706"),
        ("5", "SET CRS", "Map Properties -> CRS\nSet EPSG:3857 or EPSG:4326\nEliminates on-the-fly lag", "#10b981"),
        ("6", "SAVE NATIVE APRX", "File -> Save As\n'SGNP_Local_Verified.aprx'\nCustom hardware profile", "#059669")
    ]

    card_w = 2.05
    spacing = 0.35
    start_x = 0.55

    for i, (num, title, body, col) in enumerate(steps):
        cx = start_x + i * (card_w + spacing)
        cy = 1.3
        ch = 4.6

        # Step card
        card = FancyBboxPatch((cx, cy), card_w, ch, boxstyle="round,pad=0.06",
                              facecolor="#1e293b", edgecolor=col, linewidth=2.0, zorder=2)
        ax.add_patch(card)

        # Number circle badge on top
        nb = Circle((cx + card_w/2, cy + ch - 0.45), 0.38, facecolor=col, edgecolor="#ffffff", lw=1.8, zorder=4)
        ax.add_patch(nb)
        ax.text(cx + card_w/2, cy + ch - 0.45, num, ha="center", va="center",
                color="#ffffff", fontsize=13, fontweight="black", zorder=5)

        # Title
        ax.text(cx + card_w/2, cy + ch - 1.15, title, ha="center", va="center",
                color="#f8fafc", fontsize=9.2, fontweight="black", zorder=4)

        # Divider
        ax.plot([cx + 0.2, cx + card_w - 0.2], [cy + ch - 1.45, cy + ch - 1.45], color=col, lw=1.2, zorder=3)

        # Body text
        ax.text(cx + card_w/2, cy + 1.8, body, ha="center", va="center",
                color="#cbd5e1", fontsize=8.2, fontweight="medium", linespacing=1.4, zorder=4)

        # Status tag
        status_bg = "#059669" if i in [3, 5] else "#334155"
        status_txt = "CRITICAL STEP" if i == 3 else ("100% READY" if i == 5 else f"STEP 0{num}")
        stag = FancyBboxPatch((cx + 0.2, cy + 0.35), card_w - 0.4, 0.45, boxstyle="round,pad=0.03",
                              facecolor=status_bg, edgecolor="#ffffff", lw=0.6, zorder=3)
        ax.add_patch(stag)
        ax.text(cx + card_w/2, cy + 0.58, status_txt, ha="center", va="center",
                color="#ffffff", fontsize=7.2, fontweight="black", zorder=4)

        # Forward arrow to next step
        if i < len(steps) - 1:
            ax.annotate("", xy=(cx + card_w + spacing - 0.05, cy + ch/2), xytext=(cx + card_w + 0.05, cy + ch/2),
                        arrowprops=dict(facecolor="#f59e0b", edgecolor="#ffffff", width=2.4, headwidth=8, headlength=9),
                        zorder=10)

    # Footer note
    foot_box = FancyBboxPatch((0.55, 0.3), 13.9, 0.55, boxstyle="round,pad=0.03",
                              facecolor="#1e293b", edgecolor="#334155", lw=1.0, zorder=2)
    ax.add_patch(foot_box)
    ax.text(7.5, 0.58, "Pro Tip: If GPU driver crashes occur, switch Rendering Engine from DirectX 11 to OpenGL in Project -> Options -> Display and click 'Clear Cache Now'.",
            ha="center", va="center", color="#38bdf8", fontsize=8.6, fontweight="bold", zorder=3)

    out_path = os.path.join(OUT, "arcgis_pro_workflow.png")
    plt.savefig(out_path, dpi=200, facecolor=fig.get_facecolor())
    plt.close()
    print("Generated:", out_path)

if __name__ == "__main__":
    generate_pipeline_diagram()
    generate_arcgis_workflow_diagram()
