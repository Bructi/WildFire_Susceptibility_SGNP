import zipfile, os, shutil
from PIL import Image

REPORT_PATH = r"d:\Aniket\majja\DMM Report.docx"
BACKUP_PATH = r"d:\Aniket\majja\DMM Report_Original_Backup.docx"
VISUALS = r"d:\Aniket\majja\visuals"

if not os.path.exists(BACKUP_PATH):
    shutil.copyfile(REPORT_PATH, BACKUP_PATH)
    print("Created backup at:", BACKUP_PATH)

image_mapping = {
    "image1.jpg": os.path.join(VISUALS, "map_01_study_area.png"),
    "image2.jpg": os.path.join(VISUALS, "methodology_workflow.png"),
    "image3.jpg": os.path.join(VISUALS, "map_03_wildfire_risk_exposure.png"),
    "image4.jpg": os.path.join(VISUALS, "map_04_evacuation_accessibility.png"),
    "image5.jpg": os.path.join(VISUALS, "chart_02_susceptibility_dist.png"),
    "image6.jpg": os.path.join(VISUALS, "map_02_wildfire_susceptibility.png"),
    "image7.jpg": os.path.join(VISUALS, "chart_01_factor_weights.png"),
}

temp_dir = os.path.join(VISUALS, "_temp_report_media")
os.makedirs(temp_dir, exist_ok=True)

converted_bytes = {}
for img_name, png_path in image_mapping.items():
    if os.path.exists(png_path):
        im = Image.open(png_path)
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        target_jpg = os.path.join(temp_dir, img_name)
        im.save(target_jpg, "JPEG", quality=95, optimize=True)
        with open(target_jpg, "rb") as f:
            converted_bytes["word/media/" + img_name] = f.read()

temp_docx = r"d:\Aniket\majja\DMM_Report_Updated_Clean.docx"
with zipfile.ZipFile(BACKUP_PATH, 'r') as zin:
    with zipfile.ZipFile(temp_docx, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename in converted_bytes:
                zout.writestr(item, converted_bytes[item.filename])
            else:
                zout.writestr(item, zin.read(item.filename))

# Overwrite REPORT_PATH safely
shutil.copyfile(temp_docx, REPORT_PATH)
if os.path.exists(temp_docx):
    os.remove(temp_docx)
shutil.rmtree(temp_dir, ignore_errors=True)
print("SUCCESS: DMM Report.docx successfully updated with high-resolution large-text maps!")
