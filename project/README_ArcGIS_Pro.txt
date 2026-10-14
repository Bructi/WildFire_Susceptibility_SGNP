================================================================================
ARCGIS PRO DISASTER MANAGEMENT & MITIGATION PROJECT WORKSPACE
================================================================================
Project Name: SGNP_Wildfire.aprx
Study Area:   Sanjay Gandhi National Park (SGNP), Mumbai, Maharashtra, India
Methodology:  Multi-Criteria Evaluation (AHP) Wildfire Susceptibility & Risk Zonation
Coordinate:   WGS 1984 Web Mercator (EPSG:3857) / WGS 84 (EPSG:4326)

FOLDER DIRECTORY STRUCTURE:
--------------------------------------------------------------------------------
project/
├── SGNP_Wildfire.aprx                   <- Main ArcGIS Pro 3.x Project File
├── Rasters/                             <- Georeferenced GeoTIFF Rasters (EPSG:4326)
│   ├── DEM_SRTM_30m.tif                 <- SRTM 30m Digital Elevation Model (12m - 468m)
│   ├── Slope_Degrees.tif                <- Slope derived from DEM (0° - 48°)
│   ├── NDVI_Vegetation_Fuel.tif         <- Fuel Dryness Fraction (-0.20 to 0.82)
│   ├── WUI_Proximity_Distance_m.tif     <- Euclidean distance to Urban Interface (m)
│   ├── Road_Network_Distance_m.tif      <- Euclidean distance to road corridors (m)
│   ├── Wildfire_Susceptibility_Index.tif<- Continuous AHP WSI Raster (0.0 to 1.0)
│   └── WSI_Reclassified_5Classes.tif    <- 5 Discrete Classes (1=Very Low .. 5=Very High)
├── Shapefiles/                          <- Vector Shapefiles (.shp, .shx, .dbf, .prj)
│   ├── SGNP_Boundary.*                  <- Legal Protected Area Boundary (103.84 km²)
│   ├── Freshwater_Reservoirs.*          <- Tulsi Lake & Vihar Lake Polygons
│   ├── WUI_500m_Buffer.*                <- 500m Urban-Wildland Interface Buffer
│   ├── Fire_Brigade_Stations.*          <- Municipal Emergency Stations (Points)
│   ├── Fire_Watchtowers.*               <- Lookout Towers & High Elevation Posts
│   ├── Evacuation_Routes.*              <- Primary Paved & Highway Evacuation Lines
│   ├── Safe_Assembly_Zones.*            <- Certified Emergency Evacuation Staging
│   ├── Ignition_Hotspots.*              <- Historical / Modeled Fire Ignition Points
│   └── Heritage_Tourist_Assets.*        <- Kanheri Caves, Safari, Tribal Padas
└── Tables/                              <- Analytical Attribute Tables
    ├── AHP_Factor_Weight_Matrix.csv     <- Pairwise Comparison Matrix (CR = 0.042)
    └── WSI_Zone_Area_Statistics.csv     <- Zonation Area Breakdowns (km² and %)

HOW TO OPEN IN ARCGIS PRO / QGIS:
--------------------------------------------------------------------------------
Option A (ArcGIS Pro):
  Double-click 'SGNP_Wildfire.aprx' or open ArcGIS Pro -> Open Project -> browse to SGNP_Wildfire.aprx.
  The project references the layers inside 'Rasters/' and 'Shapefiles/'.

Option B (QGIS / Other GIS):
  Open QGIS -> Layer -> Add Layer -> Add Raster Layer (select rasters in Rasters/)
  Add Layer -> Add Vector Layer (select shapefiles in Shapefiles/).
================================================================================
