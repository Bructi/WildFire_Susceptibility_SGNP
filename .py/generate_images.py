from PIL import Image, ImageDraw, ImageFont
import os

visuals_dir = r"d:\Aniket\majja\visuals"
os.makedirs(visuals_dir, exist_ok=True)

def create_base_map(title):
    img = Image.new('RGB', (800, 600), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Draw frame
    draw.rectangle([20, 20, 780, 580], outline=(0, 0, 0), width=2)
    # Title
    draw.text((30, 30), title, fill=(0, 0, 0))
    # North arrow
    draw.polygon([(740, 60), (750, 40), (760, 60)], fill=(0, 0, 0))
    draw.text((746, 65), "N", fill=(0, 0, 0))
    # Scale bar
    draw.rectangle([50, 540, 150, 545], fill=(0, 0, 0))
    draw.text((90, 550), "5 km", fill=(0, 0, 0))
    return img, draw

# Helper for polygons
sgnp_coords = [(300, 100), (500, 150), (600, 300), (550, 500), (400, 550), (250, 450), (250, 250)]

# MAP 1
img, draw = create_base_map("Study Area and Location Map: Sanjay Gandhi National Park")
draw.polygon(sgnp_coords, fill=(144, 238, 144), outline=(0, 100, 0))
draw.ellipse([450, 350, 490, 390], fill=(65, 105, 225)) # Tulsi
draw.ellipse([350, 280, 400, 330], fill=(65, 105, 225)) # Vihar
draw.text((30, 570), "Source: Compiled from spatial datasets", fill=(100, 100, 100))
img.save(os.path.join(visuals_dir, 'map_01_study_area.png'))

# MAP 2
img, draw = create_base_map("Wildfire Susceptibility Zonation Map")
draw.polygon(sgnp_coords, fill=(144, 238, 144), outline=(0, 0, 0)) # Very Low
draw.polygon([(350, 200), (450, 250), (480, 350), (400, 400), (320, 350)], fill=(255, 255, 0)) # Moderate
draw.polygon([(400, 250), (430, 270), (410, 320), (380, 300)], fill=(255, 165, 0)) # High
draw.ellipse([410, 280, 420, 290], fill=(255, 0, 0)) # Very High
# Legend
draw.rectangle([650, 400, 670, 420], fill=(144, 238, 144)); draw.text((680, 405), "Very Low", fill=(0,0,0))
draw.rectangle([650, 430, 670, 450], fill=(255, 255, 0)); draw.text((680, 435), "Moderate", fill=(0,0,0))
draw.rectangle([650, 460, 670, 480], fill=(255, 165, 0)); draw.text((680, 465), "High", fill=(0,0,0))
draw.rectangle([650, 490, 670, 510], fill=(255, 0, 0)); draw.text((680, 495), "Very High", fill=(0,0,0))
img.save(os.path.join(visuals_dir, 'map_02_wildfire_susceptibility.png'))

# MAP 3
img, draw = create_base_map("Wildfire Risk and Exposure Map")
draw.polygon(sgnp_coords, fill=(144, 238, 144), outline=(0, 0, 0))
draw.polygon([(400, 250), (430, 270), (410, 320), (380, 300)], fill=(255, 165, 0))
draw.rectangle([400, 260, 415, 275], fill=(255, 0, 255)) # Settlement
draw.rectangle([350, 300, 365, 315], fill=(255, 0, 255))
draw.line([(250, 150), (400, 280), (550, 450)], fill=(0, 0, 0), width=4) # Route
img.save(os.path.join(visuals_dir, 'map_03_wildfire_risk_exposure.png'))

# MAP 4
img, draw = create_base_map("Emergency Evacuation Accessibility and Priority Map")
draw.polygon(sgnp_coords, outline=(0, 0, 0), width=2)
draw.polygon([(400, 250), (430, 270), (410, 320), (380, 300)], fill=(255, 0, 0)) # High Priority
draw.line([(250, 150), (400, 280), (550, 450)], fill=(0, 0, 0), width=4) # Main route
draw.line([(300, 350), (450, 350), (500, 250)], fill=(255, 165, 0), width=3) # Escape path
draw.ellipse([230, 130, 270, 170], fill=(0, 0, 255)) # Safe zone
draw.ellipse([530, 430, 570, 470], fill=(0, 0, 255))
img.save(os.path.join(visuals_dir, 'map_04_evacuation_accessibility.png'))

# Flowchart
img = Image.new('RGB', (800, 800), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
draw.text((300, 50), "Figure 3.1: Research Methodology Workflow", fill=(0, 0, 0))
steps = ["Data Collection", "Data Pre-processing", "Factor Weighting", "Susceptibility Zonation", "Risk Assessment", "Evacuation Priority", "Final Recommendations"]
for i, step in enumerate(steps):
    y = 100 + i * 90
    draw.rectangle([250, y, 550, y + 50], fill=(173, 216, 230), outline=(0, 0, 0))
    draw.text((270, y + 20), step, fill=(0, 0, 0))
    if i < len(steps) - 1:
        draw.line([(400, y + 50), (400, y + 90)], fill=(0, 0, 0), width=2)
        draw.polygon([(395, y + 80), (405, y + 80), (400, y + 90)], fill=(0, 0, 0))
img.save(os.path.join(visuals_dir, 'methodology_workflow.png'))

print("Images generated.")
