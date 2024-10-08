from __future__ import division
import numpy as np
from scipy import stats


def get_net2net_matrix(conn_mtx, network_names, net_list=None, meas='mean'):
    if net_list==None:
        net_list = sorted(list(set(network_names)))
    net_num = len(net_list)
    net_mtx = np.zeros((net_num, net_num))
    for inet,net0 in enumerate(net_list):
        for jnet,net1 in enumerate(net_list):
            idx0 = [i for i, n in enumerate(network_names) if n == net0]
            idx1 = [i for i, n in enumerate(network_names) if n == net1]
            nd = conn_mtx[idx0][:,idx1]
            if meas == 'mean':
                net_mtx[inet,jnet] = np.nanmean(nd)
            elif meas == 'sum':
                net_mtx[inet,jnet] = np.nansum(nd)
    return net_mtx, net_list
