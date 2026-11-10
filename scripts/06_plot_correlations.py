"""Correlation matrices (Pearson r, pairwise complete years, min. 5 shared years), one per dimension.

Usage: python scripts/06_plot_correlations.py cocaine|cannabis|mdma
Reads data/processed/<drug>_harm_long.csv; writes output/figures/<drug>_*_correlations.png and output/tables/<drug>_*_correlations.csv.
Indicators per drug are defined in scripts/_config.py.
"""
import csv, math, sys, matplotlib
from _paths import PROCESSED, FIGURES, TABLES
from _config import CORR
DRUG = sys.argv[1] if len(sys.argv) > 1 else "cocaine"
NAME = {"mdma": "MDMA"}.get(DRUG, DRUG)
MINN = 5
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
L=list(csv.DictReader(open(PROCESSED / f'{DRUG}_harm_long.csv', encoding='utf-8')))
V={}
for x in L:
    if "different institution base" in x['flag']: continue
    V.setdefault(x['column'],{})[int(x['year'])]=float(x['value'])
SURF="#fcfcfb"; T1="#0b0b0b"; T2="#52514e"; MISS="#ffffff"
cmap=LinearSegmentedColormap.from_list("div",["#e34948","#f0efec","#2a78d6"])
MINN=5
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
fig(CORR[DRUG]["crime"],f"Correlations between crime harm indicators, {NAME}, Netherlands",FIGURES / f"{DRUG}_crime_correlations.png",TABLES / f"{DRUG}_crime_correlations.csv")
fig(CORR[DRUG]["use"],f"Correlations between use and dependency harm indicators, {NAME}, Netherlands",FIGURES / f"{DRUG}_use_correlations.png",TABLES / f"{DRUG}_use_correlations.csv")
