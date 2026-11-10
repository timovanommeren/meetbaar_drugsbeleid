"""Small-multiple time-series plots, one figure per harm dimension.

Reads data/processed/cocaine_harm_long.csv; writes output/figures/cocaine_*_indicators.png.
"""
import csv, matplotlib
from _paths import PROCESSED, FIGURES, TABLES
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator
L=list(csv.DictReader(open(PROCESSED / 'cocaine_harm_long.csv', encoding='utf-8')))
def s(col):
    r=sorted([(int(x['year']),float(x['value']),x['flag']) for x in L if x['column']==col and int(x['year'])>=2003])
    return r
SURF="#fcfcfb"; T1="#0b0b0b"; T2="#52514e"; T3="#8a8984"; GRID="#e6e5e1"
SER=["#2a78d6","#eb6834","#1baf7a"]
crime=[("Hard-drug offences registered",[("c09_harddrug_offences_registered",None)],"offences"),
("Hard-drug suspect registrations",[("c09_harddrug_suspect_registrations",None)],"registrations"),
("Murder victims",[("c07_murder_victims_total","total"),("c07_murder_victims_firearm","by firearm")],"victims"),
("Criminal-milieu murders and liquidations",[("c05_murders_criminal_milieu","criminal milieu"),("c06_liquidations","liquidations")],"cases"),
("Attacks with explosives",[("c08_explosive_attacks",None)],"attacks"),
("Uithalers apprehended",[("c03_uithalers_apprehended",None)],"persons"),
("Cocaine seized",[("c01_seized_douane_total_kg","Douane total"),("c01_seized_douane_maritime_kg","Douane maritime"),("c01_seized_harc_rotterdam_kg","HARC Rotterdam")],"kg"),
("Douane seizures, number (all)",[("c01_seizures_douane_total_n",None)],"seizures"),
("Douane seizures, number (maritime)",[("c01_seizures_douane_maritime_n",None)],"seizures"),
("OM investigations, organised drug crime",[("c10_investigations_org_drug_crime","all drugs"),("c10_investigations_cocaine_heroin","cocaine & heroin")],"investigations"),
("Retail price",[("c18_retail_price_eur_g",None)],"€ per gram"),
("Perceived drug nuisance in neighbourhood",[("c16_nuisance_drug_dealing_pct","dealing"),("c16_nuisance_drug_use_pct","use")],"% of residents"),
("Cocaine seized at Schiphol",[("c01_seized_schiphol_kg",None)],"kg"),
("Cocaine labs dismantled",[("c20_cocaine_labs_dismantled",None)],"sites"),
("Payment-code fraud at terminals",[("c19_paymentcode_fraud",None)],"cases"),
("Organized Crime Index, cocaine trade",[("c14_ocindex_cocaine_trade",None)],"score (1–10)")]
use=[("Last-year use",[("h01_lastyear_use_pct","CBS, all ages"),("h01b_lastyear_use_18plus_ndm_pct","NDM, 18+")],"% of population"),
("Last-month use (CBS)",[("h01_lastmonth_use_pct",None)],"% of population"),
("Lifetime use (CBS)",[("h01_lifetime_use_pct",None)],"% of population"),
("Lifetime use, pupils 12–16",[("h03_lifetime_use_pupils_pct",None)],"% of pupils"),
("Treatment, cocaine primary problem",[("h05_treatment_all_institutions","all institutions"),("h05_treatment_constant_institutions","constant institutions")],"clients"),
("Treatment, cocaine secondary problem",[("h05_treatment_secondary_all","all institutions"),("h05_treatment_secondary_constant","constant institutions")],"clients"),
("Deaths involving cocaine",[("h08_deaths_cocaine","NDM definition"),("h08_deaths_f14_underlying","F14 underlying cause")],"deaths"),
("Hospital admissions, cocaine main diagnosis",[("h09_hospital_main_dx",None)],"admissions"),
("Hospital admissions, cocaine secondary diagnosis",[("h09_hospital_secondary_dx",None)],"admissions"),
("Cocaine share of drug incidents",[("h06_mdi_share_mdi_hospitals_pct","MDI hospitals"),("h06_mdi_incidents_share_pct","all services"),("h06_mdi_share_ambulance_pct","ambulance")],"% of incidents"),
("Cocaine in wastewater",[("h11_wastewater_amsterdam","Amsterdam"),("h11_wastewater_eindhoven","Eindhoven"),("h11_wastewater_utrecht","Utrecht")],"mg/1,000 inh./day"),
("Purity",[("h12_purity_dims_pct","DIMS samples"),("h17_purity_nfi_pct","NFI police seizures")],"% cocaine"),
("Adulterated samples (DIMS)",[("h12_adulterated_share_pct","any cutting agent"),("h12_levamisole_share_pct","levamisole")],"% of samples"),
("Last-year use, nightlife-goers",[("h04_lastyear_use_nightlife_pct",None)],"% of nightlife-goers"),
("Treatment per 100,000 inhabitants",[("h05_treatment_per100k_constant",None)],"clients (constant inst.)")]
fmt=FuncFormatter(lambda v,p: f"{v:,.0f}" if abs(v)>=10 or v==0 else f"{v:g}")
def fig(panels,title,sub,out):
    n=len(panels); nc=4; nr=-(-n//nc)
    f,axs=plt.subplots(nr,nc,figsize=(17,3.35*nr+1.3),facecolor=SURF,sharex=True)
    for ax,(t,ser,unit) in zip(axs.flat,panels):
        ax.set_facecolor(SURF)
        multi=len(ser)>1; ymax=0
        for k,(col,lab) in enumerate(ser):
            d=s(col); 
            if not d: continue
            c=SER[k]
            main=[(x,y,fl) for x,y,fl in d if "different institution base" not in fl]
            for (x0,y0,_),(x1,y1,_) in zip(main,main[1:]):
                gap=x1-x0>1
                ax.plot([x0,x1],[y0,y1],color=c,lw=1.2 if gap else 2,ls=(0,(2,2)) if gap else "-",solid_capstyle="round",zorder=3)
            for x,y,fl in d:
                exact=fl.startswith("exact") and "different institution base" not in fl
                ax.plot(x,y,"o",ms=5 if exact else 6,mfc=c if exact else SURF,mec=c,mew=1.6,zorder=4)
            ymax=max(ymax,max(y for _,y,_ in d))
        ax.set_title(t,loc="left",fontsize=10.5,color=T1,fontweight="bold",pad=30 if multi else 16)
        ax.text(0,1.11 if multi else 1.02,unit,transform=ax.transAxes,fontsize=8.5,color=T2,va="bottom")
        ax.set_ylim(0,ymax*1.12); ax.yaxis.set_major_formatter(fmt); ax.yaxis.set_major_locator(MaxNLocator(4))
        ax.grid(axis="y",color=GRID,lw=0.8); ax.set_axisbelow(True)
        for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
        ax.spines["bottom"].set_color(T3); ax.tick_params(colors=T2,labelsize=8.5,length=0)
        ax.set_xlim(2003,2026.5); ax.set_xticks([2005,2010,2015,2020,2025])
        if multi:
            ax.legend([plt.Line2D([],[],color=SER[k],lw=2.5) for k in range(len(ser))],[l for _,l in ser],fontsize=8,frameon=False,loc="lower left",bbox_to_anchor=(0,1.0),ncol=len(ser),labelcolor=T2,handlelength=1.2,columnspacing=1.0,borderaxespad=0.1,handletextpad=0.4)
        ax.xaxis.set_tick_params(labelbottom=True)
    for ax in list(axs.flat)[n:]: ax.set_visible(False)
    f.text(0.012,0.992,title,ha="left",va="top",fontsize=16,fontweight="bold",color=T1)
    f.text(0.012,0.972,sub,ha="left",va="top",fontsize=10,color=T2)
    f.tight_layout(rect=(0,0.03,1,0.96),h_pad=2.2,w_pad=2.5)
    f.text(0.012,0.004,"Filled dot: exact value. Open dot: approximate, derived, uncertain or partial-year value, or (treatment 2006, 2015) an older report with a different institution base. Dashed line: years missing in between.\nEach panel has its own y-axis starting at zero. Source: cocaine_harm_long.csv (CBS, Nationale Drug Monitor, Politie, OM, GI-TOC).",fontsize=8.5,color=T2)
    FIGURES.mkdir(parents=True, exist_ok=True); TABLES.mkdir(parents=True, exist_ok=True)
    f.savefig(out,dpi=150,facecolor=SURF); print(out)
fig(crime,"Crime harm indicators, cocaine, Netherlands","Enforcement, violence, recruitment, trade and market indicators, 2003–2025",FIGURES / "cocaine_crime_indicators.png")
fig(use,"Use and dependency harm indicators, cocaine, Netherlands","Prevalence, treatment, acute harm, mortality, consumption and product risk, 2003–2025",FIGURES / "cocaine_use_indicators.png")
