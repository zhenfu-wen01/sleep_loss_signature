import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_paired_measures(df, use_colors):
    jitter = 0.025
    np.random.seed(0)
    df_x_jitter = pd.DataFrame(np.random.normal(loc=0, scale=jitter, size=df.values.shape), columns=df.columns)
    df_x_jitter += np.arange(len(df.columns))
    
    fig, ax = plt.subplots(figsize=(6,6))
    # sns.violinplot(x=-2.5, y=df['C1'].to_numpy(), split=True, width=0.1, ax=ax, fill=False)
    # use_colors = ['b', 'r']
    for ic,col in enumerate(df):
        ax.plot(df_x_jitter[col], df[col], 'o', alpha=.90, zorder=1, ms=5, mew=0, color=use_colors[ic])
    ax.set_xticks(range(len(df.columns)))
    ax.set_xticklabels(df.columns)
    # ax.set_xlim(-0.5,len(df.columns)-0.5)
    
    for idx in df.index:
        cflg = df.loc[idx,['C1']].to_numpy() - df.loc[idx,['C2']].to_numpy()
        if cflg>0:
            clr = use_colors[0]
        else:
            clr = use_colors[1]
        ax.plot(df_x_jitter.loc[idx,['C1','C2']], 
                df.loc[idx,['C1','C2']], 
                color=clr, 
                linewidth=1., 
                linestyle='-', 
                zorder=-1,
                alpha=0.3)
    
    v1 = ax.violinplot(df['C1'].to_numpy(), points=100, positions=[0], widths=0.3,
                       showmeans=False, showextrema=False, showmedians=False)
    
    v2 = ax.violinplot(df['C2'].to_numpy(), points=100, positions=[1], widths=0.3,
                       showmeans=False, showextrema=False, showmedians=False)
    
    for b in v1['bodies']:
        # get the center
        m = np.mean(b.get_paths()[0].vertices[:, 0])
        # modify the paths to not go further right than the center
        b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
        b.set_color(use_colors[0])
        b.set_alpha(0.5)
    for b in v2['bodies']:
        # get the center
        m = np.mean(b.get_paths()[0].vertices[:, 0])
        # modify the paths to not go further left than the center
        b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
        b.set_color(use_colors[1])
        b.set_alpha(0.5)

    return fig, ax