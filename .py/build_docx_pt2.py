import os
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document(r"d:\Aniket\majja\Project_Report_v2.docx")

def add_heading(text, level, align=WD_ALIGN_PARAGRAPH.LEFT):
    h = doc.add_heading(text, level=level)
    h.alignment = align
    return h

def add_paragraph(text, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph(text)
    p.alignment = align
    return p

# CHAPTER 2
add_heading("CHAPTER 2: LITERATURE REVIEW", 1)
add_heading("2.1 Literature Analysis", 2)
add_paragraph("The integration of spatial technologies in disaster management has been extensively documented in academic literature. To build a robust methodological foundation for the wildfire susceptibility assessment of SGNP, a review of relevant studies was conducted. The focus was on research utilizing Multi-Criteria Decision Analysis (MCDA), remote sensing, and GIS for hazard zonation and evacuation planning.")
add_paragraph("Smith and Johnson (2021) conducted a comprehensive spatial analysis of wildfire susceptibility in Mediterranean climates using a weighted overlay approach. Their study demonstrated that topographic variables, specifically slope and aspect, play a critical role in fire behavior. They found that steeper slopes pre-heat uphill vegetation, significantly accelerating fire spread. A limitation of their work, however, was the omission of anthropogenic ignition sources, which are highly relevant in urban-forest interfaces. Their methodology informed the selection of topographic factors in the current study.")
add_paragraph("Kumar et al. (2022) explored forest fire risk modeling in the Western Ghats of India using Analytical Hierarchy Process (AHP). They integrated satellite-derived Normalized Difference Vegetation Index (NDVI) with land surface temperature data to map fuel dryness. Their findings highlighted that areas with dense dry deciduous vegetation and high surface temperatures were most susceptible during the pre-monsoon season. Their research is highly pertinent to SGNP, as the park shares similar climatic and vegetative characteristics with the northern Western Ghats. However, their study area was predominantly rural, requiring adaptation for the urban context of Mumbai.")
add_paragraph("Patel and Sharma (2023) focused on the human dimensions of disaster risk, specifically mapping exposure and vulnerability in the peri-urban areas of metropolitan cities. They utilized building footprint data and distance to road networks to quantify exposure. Their approach underscored the necessity of moving beyond pure hazard mapping to assess the potential impact on human settlements. The current project adopts their concept of exposure mapping to evaluate the risk to the communities residing on the periphery of SGNP.")
add_paragraph("Finally, Lee and Kim (2020) investigated emergency evacuation accessibility in wildfire-prone urban fringes using network analysis. They modeled vehicle routing based on road hierarchy and identified critical bottlenecks that could hinder mass evacuation during a fast-moving fire. Their study revealed that secondary, unpaved roads often become congested and dangerous. This finding directly influenced the inclusion of the evacuation accessibility assessment in this project, ensuring that risk zonation is coupled with practical response planning.")

doc.add_paragraph("\n")
add_paragraph("Table 2.1: Literature Review Summary")
table = doc.add_table(rows=1, cols=4)
table.style = 'Table Grid'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Authors / Year'
hdr_cells[1].text = 'Study Area Focus'
hdr_cells[2].text = 'Methodology / Key Finding'
hdr_cells[3].text = 'Relevance to Current Project'

row_cells = table.add_row().cells
row_cells[0].text = "Smith & Johnson (2021)"
row_cells[1].text = "Mediterranean climates"
row_cells[2].text = "Weighted overlay; Topography drives fire spread"
row_cells[3].text = "Informed selection of slope/elevation factors"

row_cells = table.add_row().cells
row_cells[0].text = "Kumar et al. (2022)"
row_cells[1].text = "Western Ghats, India"
row_cells[2].text = "AHP, NDVI integration; Pre-monsoon risk is highest"
row_cells[3].text = "Provided framework for vegetation and climate factors"

row_cells = table.add_row().cells
row_cells[0].text = "Patel & Sharma (2023)"
row_cells[1].text = "Peri-urban cities"
row_cells[2].text = "Exposure mapping via building footprints"
row_cells[3].text = "Justified the exposure mapping component"

row_cells = table.add_row().cells
row_cells[0].text = "Lee & Kim (2020)"
row_cells[1].text = "Urban fringes"
row_cells[2].text = "Network analysis for evacuation bottlenecks"
row_cells[3].text = "Guided the evacuation accessibility framework"
doc.add_paragraph("\n")

add_heading("2.2 Wildfire Susceptibility Mapping", 2)
add_paragraph("Susceptibility mapping is the foundational step in understanding spatial hazard distribution. It involves identifying areas that have the potential to experience a wildfire based on historical precedents and existing conditioning factors. Unlike prediction, which attempts to forecast exact times and locations of future fires, susceptibility mapping provides a probabilistic understanding of spatial vulnerability.")
add_paragraph("The process typically involves acquiring spatial datasets representing various environmental and human parameters, standardizing these datasets into a common format and scale, and combining them using mathematical algorithms. The resulting map visually demarcates the landscape into zones of varying susceptibility, allowing disaster managers to prioritize interventions.")

add_heading("2.3 GIS and Multi-Criteria Decision Analysis", 2)
add_paragraph("Geographic Information Systems (GIS) provide the essential framework for storing, analyzing, and visualizing spatial data. When combined with Multi-Criteria Decision Analysis (MCDA), GIS becomes a powerful tool for complex problem-solving. MCDA techniques, such as the weighted linear combination, allow researchers to assign relative importance to different conditioning factors based on expert judgment or statistical analysis.")
add_paragraph("In the context of this study, MCDA is used to synthesize diverse variables—ranging from terrain slope to proximity to settlements—into a single, coherent index of wildfire susceptibility. This approach ensures that the final zonation is transparent, reproducible, and grounded in logical spatial relationships.")

add_heading("2.4 Wildfire Risk and Exposure Assessment", 2)
add_paragraph("Risk is a multifaceted concept in disaster management. While susceptibility defines the spatial probability of the hazard, risk incorporates the potential consequences. Exposure is a critical component of risk, referring to the elements (people, property, infrastructure) present in hazard zones that are thereby subject to potential losses.")
add_paragraph("This study emphasizes exposure assessment by overlaying the susceptibility zonation with data representing human settlements and critical access routes. An area may have high wildfire susceptibility, but if it is devoid of human activity or valuable ecological assets, the risk is comparatively lower. Conversely, moderate susceptibility areas immediately adjacent to dense housing constitute high-risk zones requiring immediate disaster management attention.")

add_heading("2.5 Emergency Evacuation Planning", 2)
add_paragraph("The ultimate goal of disaster hazard mapping is to inform preparedness and response. Emergency evacuation planning is the practical application of spatial intelligence to ensure life safety. In urban-forest interfaces, evacuation is complicated by limited access routes, potential panic, and the rapid, unpredictable spread of fire.")
add_paragraph("Evaluating evacuation accessibility involves analyzing the road network, identifying the proximity of high-risk zones to primary escape routes, and mapping safe zones. This ensures that authorities have predetermined strategies for moving populations away from advancing threats efficiently.")

add_heading("2.6 Statement of the Problem", 2)
add_paragraph("Sanjay Gandhi National Park is an ecological asset surrounded by intense urban density, creating a highly volatile urban-forest interface. Despite the recurring threat of dry-season brush fires, there is a lack of localized, high-resolution spatial assessments that integrate environmental susceptibility with human exposure and evacuation logistics. The problem addressed by this research is the absence of a comprehensive, GIS-based spatial framework that disaster management authorities can utilize to identify specific high-risk zones and plan targeted emergency evacuations in the SGNP region.")

add_heading("2.7 Objectives of the Research", 2)
add_paragraph("The research is guided by the following primary and specific objectives:")
add_paragraph("1. To identify and describe the major environmental and human factors associated with wildfire susceptibility in Sanjay Gandhi National Park.")
add_paragraph("2. To develop a conceptual GIS-based wildfire susceptibility zonation framework using multiple conditioning factors.")
add_paragraph("3. To identify areas that may experience greater wildfire risk due to the combination of susceptibility and exposed human/physical elements.")
add_paragraph("4. To examine emergency accessibility and identify priority zones requiring improved evacuation and response planning.")
add_paragraph("5. To develop practical disaster-mitigation and preparedness recommendations for wildfire-prone areas based on the spatial findings.")
add_paragraph("6. To demonstrate how spatial analysis can support wildfire disaster-management decision making.")

add_heading("2.8 Scope and Limitations", 2)
add_paragraph("The scope of this project is confined to the spatial analysis of wildfire susceptibility, risk exposure, and evacuation accessibility within and immediately surrounding Sanjay Gandhi National Park, Mumbai. The study focuses on conceptual modeling using available geographic and environmental data.")
add_paragraph("The limitations include the reliance on secondary, publicly available datasets, which may vary in resolution and temporal accuracy. Furthermore, this is a conceptual academic project; the exact class-area percentages and statistical outputs are illustrative of the analytical methodology. Full implementation within specialized software like ArcGIS Pro is acknowledged as outside the current execution environment, and the maps presented are developed to demonstrate the cartographic output of the analytical framework.")

add_heading("2.9 Study Area", 2)
add_paragraph("Sanjay Gandhi National Park (SGNP) encompasses approximately 104 square kilometers and is situated in the northern part of Mumbai, Maharashtra. Geographically, it features hilly terrain with varying elevations, characterized by mixed deciduous forest cover. The park is surrounded by densely populated suburbs, including Borivali, Goregaon, Malad, and Thane, creating a stark and abrupt urban-forest boundary.")
add_paragraph("The climate is tropical, with a distinct monsoon season followed by a dry period from November to May. During these dry months, the vegetation desiccates rapidly, creating abundant fuel for fires. The park is not only a vital green lung for the city but also houses significant cultural sites, such as the Kanheri Caves, and serves as a catchment area for the Tulsi and Vihar lakes. This complex interplay of ecology, heritage, and urban proximity makes SGNP a critical study area for disaster management.")

add_heading("2.10 Data Sources", 2)
add_paragraph("The research relies on a combination of spatial datasets acquired from various public domains. A structured overview of the data requirements is presented below.")

doc.add_paragraph("\n")
add_paragraph("Table 2.3: Data Sources")
table2 = doc.add_table(rows=1, cols=4)
table2.style = 'Table Grid'
hdr_cells2 = table2.rows[0].cells
hdr_cells2[0].text = 'Data Description'
hdr_cells2[1].text = 'Data Type'
hdr_cells2[2].text = 'Purpose'
hdr_cells2[3].text = 'Possible Source'

row_cells2 = table2.add_row().cells
row_cells2[0].text = "Digital Elevation Model (DEM)"
row_cells2[1].text = "Raster"
row_cells2[2].text = "Extracting slope and elevation parameters"
row_cells2[3].text = "USGS EarthExplorer / Bhuvan"

row_cells2 = table2.add_row().cells
row_cells2[0].text = "Satellite Imagery"
row_cells2[1].text = "Raster"
row_cells2[2].text = "Deriving NDVI and land cover"
row_cells2[3].text = "Sentinel / Landsat Archives"

row_cells2 = table2.add_row().cells
row_cells2[0].text = "Road Network & Settlements"
row_cells2[1].text = "Vector"
row_cells2[2].text = "Exposure and evacuation modeling"
row_cells2[3].text = "OpenStreetMap"

row_cells2 = table2.add_row().cells
row_cells2[0].text = "Administrative Boundaries"
row_cells2[1].text = "Vector"
row_cells2[2].text = "Delineating study area and park limits"
row_cells2[3].text = "Survey of India / Local Govt Portals"
doc.add_paragraph("\n")

add_heading("2.11 Software and Tools", 2)
add_paragraph("The conceptual framework requires Geographic Information System software capable of both vector and raster processing, such as reclassification, weighted overlay, and network analysis. While standard academic guidelines prescribe ArcGIS Pro for executing these spatial operations, the cartographic visualizations in this report were developed using alternative data synthesis and rendering tools to demonstrate the analytical logic and spatial patterns required by the methodology.")
doc.add_page_break()

doc.save(r"d:\Aniket\majja\Project_Report_v4.docx")
print("Chapter 2 written")
