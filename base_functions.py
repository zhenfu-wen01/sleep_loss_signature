from __future__ import division
import math 
import pandas as pd
import numpy as np
from scipy import stats
# from bct.algorithms import get_components


def get_subject_info(DF, subjects, var_name):
    df_subjects = DF['Subjects'].to_list()

    subj_idx = []
    df_idx = []
    for isubj, subj in enumerate(subjects):
        if subj in df_subjects:
            idx = df_subjects.index(subj)
            subj_idx.append(isubj)
            df_idx.append(idx)
    care_DF = DF.iloc[df_idx].reset_index(drop=True)
    info_data = np.nan*np.zeros((len(subjects), len(var_name)))
    info_data[subj_idx] = care_DF[var_name].to_numpy()
    info_data = np.squeeze(info_data)
    return info_data

def plot_line_std(meas, ax):
    snum, tnum = meas.shape
    mp = np.nanmean(meas, axis=0)
    sp = np.nanstd(meas, axis=0) / np.sqrt(snum)
    ax.errorbar(np.arange(1,tnum+1), mp, yerr=sp);
    return ax


def weight_transform(X, coef_vals, Nbricks = 100):
    # For small feature number:
    # patterns = np.cov(pca_X.T)@coef_vals.T/np.cov(coef_vals@pca_X.T)
    
    data = X.copy()
    weights = coef_vals.T
    n_samples, n_dim = data.shape
    
    scale_param = np.cov(np.matmul(weights.T, data.T))
    pattern_unscaled = np.zeros((n_dim,1));

    data = data - np.mean(data, axis=0, keepdims=True)

    Nbricks = min(Nbricks,n_dim);
    brick_n = np.floor(n_dim / Nbricks);


    #Randomly assign TRs into one of Nfolds
    for n in range(Nbricks):
#         print(n)
        #Select id group
        if n<Nbricks-1:
            ids = np.arange(n*brick_n, (n+1)*brick_n)
        elif n==Nbricks-1:
            ids = np.arange(n*brick_n, n_dim)
        ids = ids.astype(int)
        #Generate unscaled forward models values
        val = data[:,ids]
        data_cov = np.matmul(val.T, data) / (n_samples-1)
        t = np.matmul(data_cov, weights)
        pattern_unscaled[ids] = t

    pattern = pattern_unscaled / scale_param; # like cov(X)*W * inv(W'*X')
    return pattern
