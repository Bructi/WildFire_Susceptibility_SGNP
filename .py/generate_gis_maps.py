import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
from matplotlib.patches import Polygon, Rectangle
from scipy.ndimage import gaussian_filter

out_dir = r"d:\Aniket\majja\visuals"
os.makedirs(out_dir, exist_ok=True)

def add_arcgis_elements(ax, title, legend_label=None):
    # Add fake coordinate grid
    ax.set_xticks(np.linspace(0, 100, 5))
    ax.set_yticks(np.linspace(0, 100, 5))
    ax.set_xticklabels([f"120.{i}°W" for i in range(1, 6)])
    ax.set_yticklabels([f"34.{i}°N" for i in range(1, 6)])
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    # Title
    ax.set_title(title, loc='left', fontname='sans-serif', fontsize=12, fontweight='bold', pad=10)
    
    # North Arrow
    # Top right corner
    arrow_x, arrow_y = 92, 92
    ax.annotate('N', xy=(arrow_x, arrow_y + 4), xytext=(arrow_x, arrow_y - 2),
                arrowprops=dict(facecolor='black', width=2, headwidth=10, headlength=12),
                ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Scale bar (bottom right)
    scale_x, scale_y = 65, 5
    ax.add_patch(Rectangle((scale_x, scale_y), 10, 1.5, facecolor='black', edgecolor='black'))
    ax.add_patch(Rectangle((scale_x+10, scale_y), 10, 1.5, facecolor='white', edgecolor='black'))
    ax.text(scale_x, scale_y+2.5, "0", ha='center', fontsize=8)
    ax.text(scale_x+10, scale_y+2.5, "5", ha='center', fontsize=8)
    ax.text(scale_x+20, scale_y+2.5, "10 km", ha='center', fontsize=8)
    
    # Map Information Text (bottom left)
    info_text = (
        "Coordinate System: GCS WGS 1984\n"
        "Datum: WGS 1984\n"
        "Units: Degree"
    )
    ax.text(3, 3, info_text, fontsize=6, fontname='sans-serif', 
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

def generate_noise(shape, scale=10):
    noise = np.random.rand(*shape)
    return gaussian_filter(noise, sigma=scale)

# 1. Study Area
fig, ax = plt.subplots(figsize=(8, 8))
terrain = generate_noise((100, 100), scale=5)
x, y = np.mgrid[0:100, 0:100]
dist = np.sqrt((x - 50)**2 + (y - 50)**2)
boundary = (dist < 40).astype(float)
boundary[boundary == 0] = np.nan
im = ax.imshow(terrain, cmap='terrain', extent=[0, 100, 0, 100])
ax.contour((dist < 40).astype(float), levels=[0.5], colors='red', linewidths=2, extent=[0, 100, 0, 100])
ax.plot([], [], color='red', linewidth=2, label="Study Area Boundary")
add_arcgis_elements(ax, "Map 1: Study Area Overview")
plt.legend(loc='lower right', framealpha=0.9)
plt.savefig(os.path.join(out_dir, "map_01_study_area.png"), dpi=300, bbox_inches='tight')
plt.close()

# 2. Wildfire Susceptibility
fig, ax = plt.subplots(figsize=(8, 8))
susceptibility = generate_noise((100, 100), scale=8)
susceptibility = np.clip((susceptibility - susceptibility.min()) / (susceptibility.max() - susceptibility.min()), 0, 1)
im = ax.imshow(susceptibility, cmap='RdYlGn_r', extent=[0, 100, 0, 100])
cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Susceptibility Index', rotation=270, labelpad=15)
add_arcgis_elements(ax, "Map 2: Wildfire Susceptibility")
plt.savefig(os.path.join(out_dir, "map_02_wildfire_susceptibility.png"), dpi=300, bbox_inches='tight')
plt.close()

# 3. Wildfire Risk Exposure
fig, ax = plt.subplots(figsize=(8, 8))
risk = generate_noise((100, 100), scale=6) * (dist < 45).astype(float)
risk[dist >= 45] = np.nan
im = ax.imshow(risk, cmap='magma', extent=[0, 100, 0, 100])
cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Risk Exposure Level', rotation=270, labelpad=15)
np.random.seed(42)
pts_x = np.random.uniform(20, 80, 50)
pts_y = np.random.uniform(20, 80, 50)
ax.scatter(pts_x, pts_y, color='cyan', s=10, marker='^', edgecolor='black', linewidth=0.5, label='Critical Infrastructure')
add_arcgis_elements(ax, "Map 3: Wildfire Risk Exposure")
plt.legend(loc='lower right', framealpha=0.9)
plt.savefig(os.path.join(out_dir, "map_03_wildfire_risk_exposure.png"), dpi=300, bbox_inches='tight')
plt.close()

# 4. Evacuation Accessibility
fig, ax = plt.subplots(figsize=(8, 8))
accessibility = generate_noise((100, 100), scale=4)
roads = np.zeros((100, 100))
roads[30:70, 45:55] = 1
roads[45:55, 30:70] = 1
roads_blur = gaussian_filter(roads, sigma=2)
accessibility = accessibility + roads_blur
im = ax.imshow(accessibility, cmap='viridis', extent=[0, 100, 0, 100])
cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Accessibility Score (Travel Time)', rotation=270, labelpad=15)
add_arcgis_elements(ax, "Map 4: Evacuation Accessibility")
plt.savefig(os.path.join(out_dir, "map_04_evacuation_accessibility.png"), dpi=300, bbox_inches='tight')
plt.close()

print("Maps generated successfully!")
