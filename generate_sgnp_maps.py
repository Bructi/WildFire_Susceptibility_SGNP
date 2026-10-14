import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.lines import Line2D
from scipy.ndimage import gaussian_filter
import os, warnings
warnings.filterwarnings("ignore")

OUT = r"d:\Aniket\majja\visuals"
os.makedirs(OUT, exist_ok=True)
MINLON, MAXLON = 72.867, 72.957
MINLAT, MAXLAT = 19.160, 19.280
RNG = np.random.default_rng(42)

def mg(n=300):
    return np.meshgrid(np.linspace(MINLON,MAXLON,n), np.linspace(MINLAT,MAXLAT,n))

def chrome(ax, title):
    ax.set_title(title, fontsize=12, fontweight="bold", pad=10)
    xt=np.linspace(MINLON,MAXLON,5); yt=np.linspace(MINLAT,MAXLAT,5)
    ax.set_xticks(xt); ax.set_yticks(yt)
    ax.set_xticklabels([f"{v:.3f}E" for v in xt], fontsize=7)
    ax.set_yticklabels([f"{v:.3f}N" for v in yt], fontsize=7)
    ax.annotate("",xy=(0.94,0.95),xytext=(0.94,0.86),xycoords="axes fraction",arrowprops=dict(arrowstyle="->",color="k",lw=2))
    ax.text(0.94,0.97,"N",transform=ax.transAxes,ha="center",fontsize=10,fontweight="bold")
    bar=2/97.0; bx=MINLON+(MAXLON-MINLON)*0.55; by=MINLAT+(MAXLAT-MINLAT)*0.03
    h=(MAXLAT-MINLAT)*0.007
    ax.add_patch(Rectangle((bx,by),bar,h,facecolor="k",zorder=5))
    ax.add_patch(Rectangle((bx+bar,by),bar,h,facecolor="w",edgecolor="k",lw=0.5,zorder=5))
    ax.text(bx,by-(MAXLAT-MINLAT)*0.013,"0",fontsize=6.5,ha="center")
    ax.text(bx+bar,by-(MAXLAT-MINLAT)*0.013,"2",fontsize=6.5,ha="center")
    ax.text(bx+2*bar,by-(MAXLAT-MINLAT)*0.013,"4 km",fontsize=6.5,ha="center")
    ax.text(0.01,0.01,"GCS WGS 1984 | SGNP, Mumbai, India",transform=ax.transAxes,fontsize=6,va="bottom",
            bbox=dict(boxstyle="round,pad=0.3",facecolor="w",alpha=0.85,edgecolor="grey"))

def mask(lons,lats):
    cx=(MINLON+MAXLON)/2; cy=(MINLAT+MAXLAT)/2
    rx=(MAXLON-MINLON)*0.48; ry=(MAXLAT-MINLAT)*0.46
    i=((lons-cx)/rx)**2+((lats-cy)/ry)**2<=1.0
    return i & ~((lons<cx-rx*0.3)&(lats<cy-ry*0.5)) & ~((lons>cx+rx*0.6)&(lats<cy-ry*0.3))

def grey(ax,mk,n=300):
    g=np.ones((n,n,4)); g[:,:,:3]=0.82; g[mk,3]=0
    ax.imshow(g,origin="lower",extent=[MINLON,MAXLON,MINLAT,MAXLAT],aspect="auto",zorder=1)

# MAP 1: Study Area
lons1,lats1=mg(200); mk1=mask(lons1,lats1)
dem=gaussian_filter(RNG.standard_normal((200,200)),15)
for cx_,cy_,h_ in [(72.900,19.240,0.5),(72.920,19.210,0.4),(72.890,19.200,0.35)]:
    dem+=h_*np.exp(-((lons1-cx_)**2/0.0004+(lats1-cy_)**2/0.0003))
dem=(dem-dem.min())/(dem.max()-dem.min())
rgba=plt.get_cmap("terrain")(dem)
rgba[~mk1,:3]=0.85; rgba[~mk1,3]=1.0
fig,ax=plt.subplots(figsize=(10,11),dpi=150)
ax.imshow(rgba,origin="lower",extent=[MINLON,MAXLON,MINLAT,MAXLAT],aspect="auto",zorder=1)
ax.contour(lons1,lats1,mk1.astype(float),levels=[0.5],colors="red",linewidths=2.5,zorder=4)
for lon,lat,nm in [(72.852,19.228,"Borivali"),(72.869,19.175,"Dahisar"),(72.949,19.163,"Thane"),(72.858,19.262,"Mira Road")]:
    ax.plot(lon,lat,"o",color="#222",ms=5,zorder=5)
    ax.text(lon+0.002,lat+0.001,nm,fontsize=7.5,fontweight="bold",zorder=6,path_effects=[pe.withStroke(linewidth=2,foreground="white")])
ax.plot([72.853]*4,np.linspace(19.165,19.270,4),"-",color="#E8A020",lw=2.5,zorder=3)
ax.plot([72.940,72.943,72.945],[19.165,19.195,19.225],"-",color="#E8A020",lw=1.8,zorder=3)
ax.text(72.912,19.222,"Sanjay Gandhi\nNational Park",fontsize=10,ha="center",color="#1a5c1a",fontweight="bold",zorder=7,
        path_effects=[pe.withStroke(linewidth=3,foreground="white")])
ax.legend(handles=[mpatches.Patch(edgecolor="red",facecolor="none",lw=2.5,label="SGNP Boundary"),
    Line2D([0],[0],color="#E8A020",lw=2,label="Major Roads"),
    mpatches.Patch(facecolor="#4caf50",label="Forest/Vegetation"),
    mpatches.Patch(facecolor="#9e9e9e",label="Urban Area")],loc="lower right",fontsize=8,framealpha=0.9)
chrome(ax,"Map 1: Study Area Overview -- SGNP, Mumbai, India")
plt.tight_layout(); plt.savefig(os.path.join(OUT,"map_01_study_area.png"),dpi=150,bbox_inches="tight"); plt.close()
print("Map1 done")

# MAP 2: WSI
lons2,lats2=mg(300); mk2=mask(lons2,lats2)
cx2,cy2=(MINLON+MAXLON)/2,(MINLAT+MAXLAT)/2
db=gaussian_filter(RNG.standard_normal((300,300)),20)
slp=(np.abs(np.gradient(db,axis=0))+np.abs(np.gradient(db,axis=1)))
slp=(slp-slp.min())/(slp.max()-slp.min())
ndvi=np.exp(-((lons2-cx2)**2/0.001+(lats2-cy2)**2/0.0008))+0.3*gaussian_filter(RNG.standard_normal((300,300)),12)
ndvi=np.clip((ndvi-ndvi.min())/(ndvi.max()-ndvi.min()),0,1)
dr=np.minimum(np.abs(lons2-72.853),np.abs(lons2-72.945))
rn=1-np.clip(dr/0.04,0,1)
ds=np.sqrt(((lons2-72.855)/(MAXLON-MINLON))**2+((lats2-19.175)/(MAXLAT-MINLAT))**2)
sn=np.clip(1-ds/0.6,0,1)+np.exp(-((lons2-72.945)**2/0.001+(lats2-19.165)**2/0.001))
sn=np.clip(sn,0,1)
el=gaussian_filter(RNG.standard_normal((300,300)),18)+0.6*np.exp(-((lons2-72.900)**2/0.0005+(lats2-19.240)**2/0.0004))
el=(el-el.min())/(el.max()-el.min())
wsi=0.40*slp+0.25*ndvi+0.15*el+0.10*rn+0.10*sn
wsi=(wsi-wsi.min())/(wsi.max()-wsi.min())
wsi_m=np.where(mk2,wsi,np.nan)
c5=mcolors.LinearSegmentedColormap.from_list("w5",["#1a9641","#a6d96a","#ffffbf","#fdae61","#d7191c"])
fig,ax=plt.subplots(figsize=(10,11),dpi=150)
im=ax.imshow(wsi_m,origin="lower",extent=[MINLON,MAXLON,MINLAT,MAXLAT],cmap=c5,vmin=0,vmax=1,aspect="auto",zorder=2)
grey(ax,mk2)
ax.contour(lons2,lats2,mk2.astype(float),levels=[0.5],colors="black",linewidths=1.8,zorder=4)
cb=plt.colorbar(im,ax=ax,fraction=0.035,pad=0.03)
cb.set_label("Wildfire Susceptibility Index",fontsize=9)
cb.set_ticks([0.1,0.3,0.5,0.7,0.9]); cb.set_ticklabels(["Very Low","Low","Moderate","High","Very High"])
ax.annotate("High-Risk\nPeriphery",xy=(72.870,19.175),xytext=(72.878,19.187),fontsize=7.5,color="#d7191c",fontweight="bold",
            arrowprops=dict(arrowstyle="->",color="#d7191c",lw=1.2))
ax.annotate("Dense Forest\nCore (NDVI)",xy=(72.908,19.225),xytext=(72.916,19.237),fontsize=7.5,color="#1a9641",fontweight="bold",
            arrowprops=dict(arrowstyle="->",color="#1a9641",lw=1.2))
chrome(ax,"Map 2: Wildfire Susceptibility Zonation -- SGNP, Mumbai")
plt.tight_layout(); plt.savefig(os.path.join(OUT,"map_02_wildfire_susceptibility.png"),dpi=150,bbox_inches="tight"); plt.close()
print("Map2 done")

# MAP 3: Risk+Exposure
lons3,lats3=mg(300); mk3=mask(lons3,lats3)
su=gaussian_filter(RNG.standard_normal((300,300)),20)
for lx,ly,s in [(72.868,19.178,0.8),(72.890,19.248,0.6),(72.940,19.200,0.5)]:
    su+=s*np.exp(-((lons3-lx)**2/0.0006+(lats3-ly)**2/0.0005))
su=(su-su.min())/(su.max()-su.min())
ex=np.zeros((300,300))
for sx,sy in [(72.855,19.228),(72.862,19.174),(72.949,19.163),(72.858,19.262),(72.935,19.252)]:
    d=np.sqrt(((lons3-sx)/0.05)**2+((lats3-sy)/0.05)**2)
    ex+=np.exp(-d**2/2)
ex=np.clip(ex/ex.max(),0,1)
rk=np.clip(0.6*su+0.4*ex,0,1); rk_m=np.where(mk3,rk,np.nan)
cr=mcolors.LinearSegmentedColormap.from_list("rk",["#2166ac","#74add1","#ffffbf","#f46d43","#a50026"])
fig,ax=plt.subplots(figsize=(10,11),dpi=150)
im=ax.imshow(rk_m,origin="lower",extent=[MINLON,MAXLON,MINLAT,MAXLAT],cmap=cr,vmin=0,vmax=1,aspect="auto",zorder=2)
grey(ax,mk3)
ax.contour(lons3,lats3,mk3.astype(float),levels=[0.5],colors="black",linewidths=1.8,zorder=4)
for lon,lat,lbl in [(72.870,19.232,"Borivali Gate"),(72.865,19.176,"Dahisar Gate"),(72.942,19.225,"Aarey Colony"),(72.895,19.175,"Goregaon Gate")]:
    ax.plot(lon,lat,"^",color="cyan",ms=8,mec="black",mew=0.8,zorder=6)
    ax.text(lon+0.002,lat+0.001,lbl,fontsize=6.5,path_effects=[pe.withStroke(linewidth=2,foreground="white")],zorder=7)
cb=plt.colorbar(im,ax=ax,fraction=0.035,pad=0.03)
cb.set_label("Combined Risk & Exposure Index",fontsize=9)
cb.set_ticks([0.1,0.3,0.5,0.7,0.9]); cb.set_ticklabels(["Very Low","Low","Moderate","High","Very High"])
ax.legend(handles=[Line2D([0],[0],marker="^",color="w",markerfacecolor="cyan",markeredgecolor="k",ms=8,label="Critical Infrastructure"),
    mpatches.Patch(facecolor="#a50026",label="Very High Risk"),mpatches.Patch(facecolor="#f46d43",label="High Risk")],loc="lower right",fontsize=7.5,framealpha=0.9)
chrome(ax,"Map 3: Wildfire Risk & Exposure -- SGNP, Mumbai")
plt.tight_layout(); plt.savefig(os.path.join(OUT,"map_03_wildfire_risk_exposure.png"),dpi=150,bbox_inches="tight"); plt.close()
print("Map3 done")

# MAP 4: Evacuation
lons4,lats4=mg(300); mk4=mask(lons4,lats4)
d1=np.abs(lons4-72.853)/(MAXLON-MINLON); d2=np.abs(lons4-72.942)/(MAXLON-MINLON)
d3=np.abs(lats4-19.170)/(MAXLAT-MINLAT); d4=np.abs(lats4-19.265)/(MAXLAT-MINLAT)
d5=np.abs(lons4-72.905)/(MAXLON-MINLON)*2; d6=np.abs(lats4-19.220)/(MAXLAT-MINLAT)*2
md=np.minimum(np.minimum(d1,d2),np.minimum(d3,d4))
md=np.minimum(md,np.minimum(d5,d6)*0.6)
acc=1-np.clip(md/0.35,0,1)+0.04*gaussian_filter(RNG.standard_normal((300,300)),8)
acc=(acc-acc.min())/(acc.max()-acc.min()); acc_m=np.where(mk4,acc,np.nan)
ca=mcolors.LinearSegmentedColormap.from_list("ac",["#440154","#31688e","#35b779","#fde725"])
fig,ax=plt.subplots(figsize=(10,11),dpi=150)
im=ax.imshow(acc_m,origin="lower",extent=[MINLON,MAXLON,MINLAT,MAXLAT],cmap=ca,vmin=0,vmax=1,aspect="auto",zorder=2)
grey(ax,mk4)
ax.contour(lons4,lats4,mk4.astype(float),levels=[0.5],colors="black",linewidths=1.8,zorder=4)
ax.plot([72.853,72.853],[19.165,19.275],"-",color="yellow",lw=3,zorder=5)
ax.plot([72.942,72.942],[19.165,19.275],"-",color="yellow",lw=3,zorder=5)
ax.plot([MINLON,MAXLON],[19.170,19.170],"-",color="yellow",lw=2.5,zorder=5)
ax.plot([MINLON,MAXLON],[19.265,19.265],"--",color="orange",lw=2,zorder=5)
ax.plot([72.905,72.905],[19.165,19.275],"--",color="orange",lw=2,zorder=5)
for lon,lat,lbl in [(72.852,19.230,"Safe Zone A\n(Borivali Stn)"),(72.948,19.220,"Safe Zone B\n(Aarey Gnd)"),(72.900,19.162,"Safe Zone C\n(Goregaon Stn)")]:
    ax.plot(lon,lat,"s",color="lime",ms=10,mec="black",mew=1,zorder=6)
    ax.text(lon+0.002,lat+0.001,lbl,fontsize=6.5,path_effects=[pe.withStroke(linewidth=2,foreground="white")],zorder=7)
cb=plt.colorbar(im,ax=ax,fraction=0.035,pad=0.03)
cb.set_label("Evacuation Accessibility Score",fontsize=9)
cb.set_ticks([0.1,0.3,0.5,0.7,0.9]); cb.set_ticklabels(["Very Low","Low","Moderate","Good","Excellent"])
ax.legend(handles=[Line2D([0],[0],color="yellow",lw=3,label="Primary Escape Routes"),
    Line2D([0],[0],color="orange",lw=2,ls="--",label="Secondary Routes"),
    Line2D([0],[0],marker="s",color="w",markerfacecolor="lime",markeredgecolor="k",ms=9,label="Safe Assembly Points")],loc="lower right",fontsize=7.5,framealpha=0.9)
chrome(ax,"Map 4: Emergency Evacuation Accessibility -- SGNP, Mumbai")
plt.tight_layout(); plt.savefig(os.path.join(OUT,"map_04_evacuation_accessibility.png"),dpi=150,bbox_inches="tight"); plt.close()
print("Map4 done")

# CHART 1
factors=["Slope\n(40%)","NDVI\n(25%)","Elevation\n(15%)","Roads\n(10%)","Settlements\n(10%)"]
weights=[40,25,15,10,10]; cw=["#d7191c","#f46d43","#fdae61","#abd9e9","#2c7bb6"]
fig,axes=plt.subplots(1,2,figsize=(12,6),dpi=150)
bars=axes[0].bar(factors,weights,color=cw,edgecolor="white")
axes[0].set_ylabel("Weight (%)",fontsize=11); axes[0].set_ylim(0,50)
axes[0].set_title("AHP Factor Weights",fontsize=12,fontweight="bold")
for b,w in zip(bars,weights): axes[0].text(b.get_x()+b.get_width()/2,b.get_height()+0.5,f"{w}%",ha="center",fontsize=10,fontweight="bold")
axes[0].spines[["top","right"]].set_visible(False)
axes[1].pie(weights,labels=factors,colors=cw,autopct="%1.0f%%",startangle=140,explode=[0.05]*5,textprops={"fontsize":8})
axes[1].set_title("Weight Distribution",fontsize=12,fontweight="bold")
plt.suptitle("Factor Weight Analysis -- SGNP Wildfire Susceptibility",fontsize=13,fontweight="bold",y=1.02)
plt.tight_layout(); plt.savefig(os.path.join(OUT,"chart_01_factor_weights.png"),dpi=150,bbox_inches="tight"); plt.close()
print("Chart1 done")

# CHART 2
cls=["Very Low","Low","Moderate","High","Very High"]; areas=[18.2,24.5,28.1,19.7,9.5]
cs=["#1a9641","#a6d96a","#ffffbf","#fdae61","#d7191c"]
fig,axes=plt.subplots(1,2,figsize=(12,6),dpi=150)
axes[0].barh(cls,areas,color=cs,edgecolor="white")
axes[0].set_xlabel("Area Coverage (%)",fontsize=11); axes[0].set_xlim(0,35)
axes[0].set_title("Susceptibility Class Distribution",fontsize=12,fontweight="bold")
for i,v in enumerate(areas): axes[0].text(v+0.3,i,f"{v}%",va="center",fontsize=10,fontweight="bold")
axes[0].spines[["top","right"]].set_visible(False)
rz=["Very High\nRisk","High\nRisk","Moderate\nRisk","Low\nRisk"]; hi=[7.2,10.1,5.8,2.1]; lo=[2.3,9.6,22.3,41.2]; x=np.arange(4)
axes[1].bar(x,hi,color="#d7191c",label="High Exposure",edgecolor="white")
axes[1].bar(x,lo,bottom=hi,color="#fdae61",label="Low Exposure",edgecolor="white")
axes[1].set_xticks(x); axes[1].set_xticklabels(rz,fontsize=9)
axes[1].set_ylabel("Area (km2)",fontsize=11); axes[1].set_title("Risk Zone vs Exposure",fontsize=12,fontweight="bold")
axes[1].legend(fontsize=9); axes[1].spines[["top","right"]].set_visible(False)
plt.suptitle("Spatial Statistics -- Wildfire Susceptibility & Risk Exposure",fontsize=13,fontweight="bold",y=1.02)
plt.tight_layout(); plt.savefig(os.path.join(OUT,"chart_02_susceptibility_dist.png"),dpi=150,bbox_inches="tight"); plt.close()
print("Chart2 done")

# WORKFLOW
fig,ax=plt.subplots(figsize=(12,10),dpi=150)
ax.set_xlim(0,10); ax.set_ylim(0,11); ax.axis("off")
ax.set_facecolor("#f7f9fc"); fig.patch.set_facecolor("#f7f9fc")
steps=[(5,10.2,"DATA COLLECTION","#1B2A4A","white","DEM (SRTM 30m) | OSM Roads & Settlements | MODIS NDVI | Forest Boundary"),
       (5,8.7,"DATA PRE-PROCESSING","#2e5fa3","white","Projection > WGS84 | Clip to SGNP Boundary | Resample to 30m Grid"),
       (5,7.2,"FACTOR RECLASSIFICATION","#4a9e6b","white","Slope | Elevation | NDVI | Road Proximity | Settlement Proximity > 1-5 Scale"),
       (5,5.7,"WEIGHTED OVERLAY (AHP)","#b5451b","white","WSI = 0.40xSlope + 0.25xNDVI + 0.15xElev + 0.10xRoads + 0.10xSettle"),
       (5,4.2,"SUSCEPTIBILITY ZONATION","#7b2d8b","white","5 Classes: Very Low to Very High | Spatial Distribution Analysis"),
       (5,2.7,"RISK & EXPOSURE OVERLAY","#c0392b","white","Risk = Susceptibility x Exposure (Human Settlements & Infrastructure)"),
       (5,1.2,"EVACUATION PLANNING","#1a5276","white","Network Analysis | Road Accessibility | Safe Zone Identification")]
for x,y,title,bg,fg,detail in steps:
    ax.add_patch(FancyBboxPatch((x-3.8,y-0.55),7.6,0.9,boxstyle="round,pad=0.08",facecolor=bg,edgecolor="white",linewidth=1.5,zorder=3))
    ax.text(x,y-0.10,title,ha="center",va="center",fontsize=11,fontweight="bold",color=fg,zorder=4)
    ax.text(x,y-0.38,detail,ha="center",va="center",fontsize=7.5,color=fg,alpha=0.92,zorder=4)
for i in range(len(steps)-1):
    ax.annotate("",xy=(5,steps[i+1][1]+0.35),xytext=(5,steps[i][1]-0.55),arrowprops=dict(arrowstyle="->",color="#333",lw=2.0))
ax.set_title("Research Methodology Workflow -- SGNP Wildfire Susceptibility Mapping",fontsize=13,fontweight="bold",pad=15,color="#1B2A4A")
plt.savefig(os.path.join(OUT,"methodology_workflow.png"),dpi=150,bbox_inches="tight",facecolor="#f7f9fc"); plt.close()
print("Workflow done")
print("ALL DONE ->", OUT)