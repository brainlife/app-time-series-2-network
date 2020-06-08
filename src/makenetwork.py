#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Oct 23 15:46:26 2018

@author: jfaskowi

copied/adapted from original code here: https://github.com/fliem/sea_zrh_rs

"""

import os
import argparse
import numpy as np
from nilearn import input_data, connectome
import pandas as pd
import h5py


def get_con_df(raw_mat, roi_names):
    """
    takes a symmetrical connectivity matrix (e.g., numpy array) and a list of roi_names (strings)
    returns data frame with roi_names as index and column names
    e.g.
         r1   r2   r3   r4
    r1  0.0  0.3  0.7  0.2
    r2  0.3  0.0  0.6  0.5
    r3  0.7  0.6  0.0  0.9
    r4  0.2  0.5  0.9  0.0
    """
    # sanity check if matrix is symmetrical
    assert np.allclose(raw_mat, raw_mat.T, atol=1e-03, equal_nan=True), "matrix not symmetrical"

    np.fill_diagonal(raw_mat, 0)
    con_df = pd.DataFrame(raw_mat, index=roi_names, columns=roi_names)
    return con_df


def extract_net(in_timeseries, discard_frames=0, conntype='correlation'):

    hf = h5py.File(in_timeseries,'r')

    reglabs = np.array(hf.get('regionids')).astype(np.str)

    ts = np.array(hf.get('timeseries'))
    print('shape of input data: {}'.format(ts.shape))
    # possibly trim
    if discard_frames>0:
        ts = ts[discard_frames:,:]
        print('new shape of input data: {}'.format(ts.shape))

    if conntype == 'partialcorrelation':
        conntype = 'partial correlation'

    connobj = connectome.ConnectivityMeasure(kind=conntype)
    connmat = connobj.fit_transform([ts])[0]
    conndf = get_con_df(connmat, reglabs)

    hf.close()

    return conndf


def main():

    parser = argparse.ArgumentParser(description='fmri -> adjacency matrix')
    parser.add_argument('timeseries', type=str, help='input fmri to be denoised')
    parser.add_argument('-type', type=str, help='type of connectivity',
                        choices=['correlation', 'partialcorrelation', 'covariance'],
                        default='correlation')
    parser.add_argument('-discardframes',type=int, 
                        help='number of frames at start of time series to discard')
    parser.add_argument('-out', type=str, help='output base name',
                        default='output')

    # parse
    args = parser.parse_args()

    # print the args
    print("\nARGS: ")
    for arg in vars(args):
        print("{} {}".format(str(arg), str(getattr(args, arg))))
    print("END ARGS\n")

    conndf = extract_net(args.timeseries, 
                         conntype=args.type, discard_frames=args.discardframes)

    conndf.to_csv(''.join([args.out, '_' , ''.join(args.type.split()), '_connMatdf.csv']), float_format='%.3g')


if __name__ == '__main__':
    main()
