"""Correlation matrices (Pearson r, pairwise complete years, min. 5 shared years), one per dimension.

Reads data/processed/cocaine_harm_long.csv; writes output/figures/cocaine_*_correlations.png and output/tables/cocaine_*_correlations.csv.
"""
import csv, math, matplotlib
from _paths import PROCESSED, FIGURES, TABLES
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
L=list(csv.DictReader(open(PROCESSED / 'cocaine_harm_long.csv', encoding='utf-8')))
V={}
for x in L:
    if "different institution base" in x['flag']: continue
    V.setdefault(x['column'],{})[int(x['year'])]=float(x['value'])
SURF="#fcfcfb"; T1="#0b0b0b"; T2="#52514e"; MISS="#ffffff"
cmap=LinearSegmentedColormap.from_list("div",["#e34948","#f0efec","#2a78d6"])
MINN=5
crime=[("c09_harddrug_offences_registered","Hard-drug offences"),("c09_harddrug_suspect_registrations","Hard-drug suspects"),
("c07_murder_victims_total","Murder victims, total"),("c07_murder_victims_firearm","Murder victims, firearm"),
("c05_murders_criminal_milieu","Criminal-milieu murders"),("c06_liquidations","Liquidations"),("c08_explosive_attacks","Explosive attacks"),
("c03_uithalers_apprehended","Uithalers"),("c01_seized_douane_total_kg","Seized, Douane total kg"),("c01_seized_douane_maritime_kg","Seized, Douane maritime kg"),
("c01_seized_harc_rotterdam_kg","Seized, HARC Rotterdam kg"),("c01_seizures_douane_total_n","Seizures, Douane total n"),("c01_seizures_douane_maritime_n","Seizures, Douane maritime n"),
("c10_investigations_org_drug_crime","OM investigations, all drugs"),("c10_investigations_cocaine_heroin","OM investigations, coc./her."),("c18_retail_price_eur_g","Retail price")]
use=[("h01_lastyear_use_pct","Last-year use (CBS)"),("h01b_lastyear_use_18plus_ndm_pct","Last-year use 18+ (NDM)"),("h01_lastmonth_use_pct","Last-month use (CBS)"),("h01_lifetime_use_pct","Lifetime use (CBS)"),
("h05_treatment_all_institutions","Treatment, all inst."),("h05_treatment_constant_institutions","Treatment, constant inst."),("h05_treatment_secondary_all","Treatment secondary, all"),("h05_treatment_secondary_constant","Treatment secondary, constant"),
("h08_deaths_cocaine","Deaths (NDM)"),("h08_deaths_f14_underlying","Deaths (F14 underlying)"),("h09_hospital_main_dx","Hospital, main dx"),("h09_hospital_secondary_dx","Hospital, secondary dx"),
("h06_mdi_incidents_share_pct","Incident share, all services"),("h06_mdi_share_mdi_hospitals_pct","Incident share, MDI hospitals"),("h06_mdi_share_ambulance_pct","Incident share, ambulance"),
("h11_wastewater_amsterdam","Wastewater, Amsterdam"),("h11_wastewater_eindhoven","Wastewater, Eindhoven"),("h11_wastewater_utrecht","Wastewater, Utrecht"),
("h12_purity_dims_pct","Purity (DIMS)"),("h12_adulterated_share_pct","Adulterated share"),("h12_levamisole_share_pct","Levamisole share")]
def pr(a,b):
    ys=sorted(set(V[a])&set(V[b])); n=len(ys)
    if n<3: return None,n
    x=[V[a][y] for y in ys]; z=[V[b][y] for y in ys]
    mx,mz=sum(x)/n,sum(z)/n
    sx=math.sqrt(sum((i-mx)**2 for i in x)); sz=math.sqrt(sum((i-mz)**2 for i in z))
    if sx==0 or sz==0: return None,n
    return sum((i-mx)*(j-mz) for i,j in zip(x,z))/(sx*sz),n
def fig(items,title,out,csvout):
    k=len(items); cols=[c for c,_ in items]; labs=[l for _,l in items]
    f,ax=plt.subplots(figsize=(0.62*k+4.2,0.55*k+2.6),facecolor=SURF); ax.set_facecolor(SURF)
    rows=[]
    for i in range(k):
        for j in range(k):
            r,n=pr(cols[i],cols[j]); rows.append([cols[i],cols[j],"" if r is None else round(r,3),n])
            if j>=i: continue
            if r is None or n<MINN:
                ax.add_patch(plt.Rectangle((j-.5+.03,i-.5+.03),.94,.94,fc=MISS,ec="#e6e5e1",lw=.8))
                ax.text(j,i,f"n={n}",ha="center",va="center",fontsize=6.5,color="#8a8984"); continue
            ax.add_patch(plt.Rectangle((j-.5+.03,i-.5+.03),.94,.94,fc=cmap((r+1)/2),ec=SURF,lw=0))
            ink="#ffffff" if abs(r)>0.6 else T1
            ax.text(j,i-.08,f"{r:.2f}".replace("0.",".").replace("-.","−."),ha="center",va="center",fontsize=8,color=ink,fontweight="bold")
            ax.text(j,i+.24,f"n={n}",ha="center",va="center",fontsize=5.8,color=ink)
    ax.set_xlim(-.5,k-1.5); ax.set_ylim(k-.5,.5)
    ax.set_yticks(range(1,k)); ax.set_yticklabels(labs[1:],fontsize=9,color=T1)
    ax.set_xticks(range(k-1)); ax.set_xticklabels(labs[:-1],fontsize=9,color=T1,rotation=50,ha="right",rotation_mode="anchor")
    ax.tick_params(length=0); [s.set_visible(False) for s in ax.spines.values()]
    f.text(0.01,0.985,title,ha="left",va="top",fontsize=15,fontweight="bold",color=T1)
    f.text(0.01,0.955,f"Pearson r between yearly values, pairwise complete years (n shown). Cells with fewer than {MINN} shared years are left blank.",ha="left",va="top",fontsize=9.5,color=T2)
    sm=plt.cm.ScalarMappable(cmap=cmap,norm=plt.Normalize(-1,1))
    cax=f.add_axes([0.70,0.80,0.22,0.018]); cb=f.colorbar(sm,cax=cax,orientation="horizontal",ticks=[-1,-.5,0,.5,1])
    cb.outline.set_visible(False); cb.ax.tick_params(labelsize=8,colors=T2,length=0); cb.set_label("r",fontsize=8.5,color=T2,labelpad=2)
    f.text(0.01,0.008,"Correlations between trending series partly reflect shared time trends; |r| needed for p < .05 (two-sided): .88 at n = 5, .63 at n = 10, .43 at n = 21. No correction for multiple comparisons.",fontsize=8.5,color=T2)
    f.subplots_adjust(left=0.20,right=0.98,top=0.93,bottom=0.17)
    FIGURES.mkdir(parents=True, exist_ok=True); TABLES.mkdir(parents=True, exist_ok=True)
    f.savefig(out,dpi=150,facecolor=SURF)
    with open(csvout,"w",newline="") as fh: w=csv.writer(fh); w.writerow(["var1","var2","r","n"]); w.writerows(rows)
    print(out)
fig(crime,"Correlations between crime harm indicators, cocaine, Netherlands",FIGURES / "cocaine_crime_correlations.png",TABLES / "cocaine_crime_correlations.csv")
fig(use,"Correlations between use and dependency harm indicators, cocaine, Netherlands",FIGURES / "cocaine_use_correlations.png",TABLES / "cocaine_use_correlations.csv")
