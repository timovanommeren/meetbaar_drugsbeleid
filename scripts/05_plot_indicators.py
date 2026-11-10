"""Small-multiple time-series plots, one figure per harm dimension.

Usage: python scripts/05_plot_indicators.py cocaine|cannabis|mdma|amphetamine|heroin
Reads data/processed/<drug>_harm_long.csv; writes output/figures/<drug>_*_indicators.png.
Panels per drug are defined in scripts/_config.py.
"""
import csv, sys, matplotlib
from _paths import PROCESSED, FIGURES, TABLES
from _config import PANELS, TEXT
DRUG = sys.argv[1] if len(sys.argv) > 1 else "cocaine"
NAME = {"mdma": "MDMA"}.get(DRUG, DRUG)
T = TEXT[DRUG]
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator
L=list(csv.DictReader(open(PROCESSED / f'{DRUG}_harm_long.csv', encoding='utf-8')))
def s(col):
    r=sorted([(int(x['year']),float(x['value']),x['flag']) for x in L if x['column']==col and int(x['year'])>=T['first']])
    return r
SURF="#fcfcfb"; T1="#0b0b0b"; T2="#52514e"; T3="#8a8984"; GRID="#e6e5e1"
SER=["#2a78d6","#eb6834","#1baf7a"]
fmt=FuncFormatter(lambda v,p: f"{v:,.0f}" if abs(v)>=10 or v==0 else f"{v:g}")
def fig(panels,title,sub,out,dim):
    D=dim[0].upper(); n=len(panels); nc=4; nr=-(-n//nc)
    f,axs=plt.subplots(nr,nc,figsize=(17,3.35*nr+1.3),facecolor=SURF,sharex=True)
    for i,(ax,(t,ser,unit)) in enumerate(zip(axs.flat,panels),1):
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
        ax.set_title(f"{D}{i}  {t}",loc="left",fontsize=10.5,color=T1,fontweight="bold",pad=30 if multi else 16)
        ax.text(0,1.11 if multi else 1.02,unit,transform=ax.transAxes,fontsize=8.5,color=T2,va="bottom")
        ax.set_ylim(0,ymax*1.12); ax.yaxis.set_major_formatter(fmt); ax.yaxis.set_major_locator(MaxNLocator(4))
        ax.grid(axis="y",color=GRID,lw=0.8); ax.set_axisbelow(True)
        for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
        ax.spines["bottom"].set_color(T3); ax.tick_params(colors=T2,labelsize=8.5,length=0)
        ax.set_xlim(T['first'],2026.5); ax.set_xticks([y for y in (2000,2005,2010,2015,2020,2025) if y>=T['first']])
        if multi:
            ax.legend([plt.Line2D([],[],color=SER[k],lw=2.5) for k in range(len(ser))],[f"{"abc"[k]}  {l}" for k,(_,l) in enumerate(ser)],fontsize=8,frameon=False,loc="lower left",bbox_to_anchor=(0,1.0),ncol=len(ser),labelcolor=T2,handlelength=1.2,columnspacing=1.0,borderaxespad=0.1,handletextpad=0.4)
        ax.xaxis.set_tick_params(labelbottom=True)
    for ax in list(axs.flat)[n:]: ax.set_visible(False)
    Hh=f.get_figheight()
    f.text(0.012,1-0.15/Hh,title,ha="left",va="top",fontsize=16,fontweight="bold",color=T1)
    f.text(0.012,1-0.48/Hh,sub,ha="left",va="top",fontsize=10,color=T2)
    f.tight_layout(rect=(0,0.45/Hh,1,1-0.8/Hh),h_pad=2.2,w_pad=2.5)
    f.text(0.012,0.004,f"Filled dot: exact value. Open dot: approximate, derived, lower-bound, uncertain or partial-year value{T['note']}. Dashed line: years missing in between. Panel IDs (C1, U3b, ...) match the correlation matrices.\nEach panel has its own y-axis starting at zero. Source: {DRUG}_harm_long.csv ({T['sources']}).",fontsize=8.5,color=T2)
    FIGURES.mkdir(parents=True, exist_ok=True); TABLES.mkdir(parents=True, exist_ok=True)
    f.savefig(out,dpi=150,facecolor=SURF); print(out)
fig(PANELS[DRUG]["crime"],f"Crime harm indicators, {NAME}, Netherlands",T["crime_sub"],FIGURES / f"{DRUG}_crime_indicators.png","crime")
fig(PANELS[DRUG]["use"],f"Use and dependency harm indicators, {NAME}, Netherlands",T["use_sub"],FIGURES / f"{DRUG}_use_indicators.png","use")
