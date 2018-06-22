#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:24:37 2018

@author: niels
"""

import numpy as np
import itertools
import dash_html_components as html



def model_value (data_valg_values, model_valg_values):
    
    if sum(data_valg_values) > 13:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.01)
        elif model_valg_values == 45:
            y=(model_valg_values*2.2)
        elif model_valg_values == 40:
            y=(model_valg_values*2.3)
    elif sum(data_valg_values) == 13 or sum(data_valg_values) == 12.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.01)
        elif model_valg_values == 45:
            y=(model_valg_values*2.2)
        elif model_valg_values == 40:
            y=(model_valg_values*2.3)
    elif sum(data_valg_values) == 12 or sum(data_valg_values) == 11.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 11 or sum(data_valg_values) == 10.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 10 or sum(data_valg_values) == 9.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 9 or sum(data_valg_values) == 8.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 8 or sum(data_valg_values) == 7.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 7 or sum(data_valg_values) == 6.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 6 or sum(data_valg_values) == 5.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 5 or sum(data_valg_values) == 4.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 4 or sum(data_valg_values) == 3.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 3 or sum(data_valg_values) == 2.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 2 or sum(data_valg_values) == 1.5:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 1:
        if model_valg_values == 49.5:
            y=(model_valg_values*2.)
        elif model_valg_values == 45:
            y=(model_valg_values*2.1)
        elif model_valg_values == 40:
            y=(model_valg_values*2.2)
    elif sum(data_valg_values) == 0.5:
        if model_valg_values == 49.5:
            y=0
        elif model_valg_values == 45:
            y=0
        elif model_valg_values == 40:
            y=0
    else:
        y = data_valg_values
    return y







def x_values(data_valg_values, model_valg_value):
    summen= sum(data_valg_values)+model_valg_value
    if summen == 1:
        nul =np.arange(1,82)
        et = np.arange(1,82)
        total=itertools.chain(nul,et)
    elif summen == 1.5:
        nul =np.arange(1,82)
        et = np.arange(6,87)
        total =itertools.chain(nul,et)
    elif summen == 2:
        nul =np.arange(1,82)
        et = np.arange(11,92)
        total =itertools.chain(nul,et) 
    elif summen == 2.5:
        nul =np.arange(1,82)
        et = np.arange(16,97)
        total =itertools.chain(nul,et) 
    elif summen == 3:
        nul =np.arange(1,82)
        et = np.arange(16,97)
        total =itertools.chain(nul,et) 
    elif summen == 3.5:
        nul =np.arange(1,82)
        et = np.arange(21,102)
        total =itertools.chain(nul,et)
    elif summen == 4:
        nul =np.arange(1,82)
        et = np.arange(21,102)
        total =itertools.chain(nul,et)
    elif summen == 4.5:
        nul =np.arange(1,82)
        et = np.arange(26,107)
        total =itertools.chain(nul,et) 
    elif summen == 5:
        nul =np.arange(1,82)
        et = np.arange(26,107)
        total =itertools.chain(nul,et) 
    elif summen == 5.5:
        nul =np.arange(1,82)
        et = np.arange(31,112)
        total =itertools.chain(nul,et)
    elif summen == 6:
        nul =np.arange(1,82)
        et = np.arange(31,112)
        total =itertools.chain(nul,et)
    elif summen == 6.5:
        nul =np.arange(1,82)
        et = np.arange(36,117)
        total =itertools.chain(nul,et)
    elif summen == 7:
        nul =np.arange(1,82)
        et = np.arange(36,117)
        total =itertools.chain(nul,et)
    elif summen == 7.5:
        nul =np.arange(1,82)
        et = np.arange(41,122)
        total =itertools.chain(nul,et)
    elif summen == 8:
        nul =np.arange(1,82)
        et = np.arange(41,122)
        total =itertools.chain(nul,et) 
    elif summen == 8.5:
        nul =np.arange(1,82)
        et = np.arange(46,127)
        total =itertools.chain(nul,et)
    elif summen == 9:
        nul =np.arange(1,82)
        et = np.arange(46,127)
        total =itertools.chain(nul,et)
    elif summen == 9.5:
        nul =np.arange(1,82)
        et = np.arange(51,132)
        total =itertools.chain(nul,et)
    elif summen == 10:
        nul =np.arange(1,82)
        et = np.arange(51,132)
        total =itertools.chain(nul,et)
    elif summen == 10.5:
        nul =np.arange(1,82)
        et = np.arange(56,137)
        total =itertools.chain(nul,et)
    elif summen == 11:
        nul =np.arange(1,82)
        et = np.arange(56,137)
        total =itertools.chain(nul,et)
    elif summen == 11.5:
        nul =np.arange(1,82)
        et = np.arange(61,142)
        total =itertools.chain(nul,et)
    elif summen == 12:
        nul =np.arange(1,82)
        et = np.arange(61,142)
        total =itertools.chain(nul,et)
    elif summen == 12.5:
        nul =np.arange(1,82)
        et = np.arange(66,147)
        total =itertools.chain(nul,et)
    elif summen == 13:
        nul =np.arange(1,82)
        et = np.arange(66,147)
        total =itertools.chain(nul,et)
    elif summen == 13.5:
        nul =np.arange(1,82)
        et = np.arange(71,152)
        total =itertools.chain(nul,et)
    elif summen == 14:
        nul =np.arange(1,82)
        et = np.arange(71,152)
        total = itertools.chain(nul,et)
    elif summen == 14.5:
        nul =np.arange(1,82)
        et = np.arange(75,156)
        total = itertools.chain(nul,et)
    elif summen == 15:
        nul =np.arange(1,82)
        et = np.arange(75,156)
        total = itertools.chain(nul,et)
    elif summen == 15.5:
        nul =np.arange(1,82)
        et = np.arange(82,163)
        total = itertools.chain(nul,et)
    return total




def string(value):
    if 'FP' in value:
        style={'background':'red', 'opacity':'0.7', 'fontSize':'15','color':'white',
               'margin':'auto', 'border':'solid', 'width':'15%',
               'text-align':'center', 'font-family':'Arial'}
    elif 'FN' in value:
        style={'background':'red', 'opacity':'0.7', 'fontSize':'15','color':'white',
               'margin':'auto', 'border':'solid', 'width':'15%',
               'text-align':'center', 'font-family':'Arial'}
    
    else:
        style={'background':'green', 'opacity':'0.7', 'fontSize':'15','color':'white',
               'margin':'auto', 'border':'solid', 'width':'15%',
               'text-align':'center', 'font-family':'Arial'}
    return style



def Table(dataframe):
    rows = []
    
    for i in range(len(dataframe)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            cell = html.Td(style=string(value), children=value)
            row.append(cell)
        rows.append(html.Tr(row))
    return html.Table(style={'width':'100%'},children=
        # Header
        #[html.Tr([html.Th(col) for col in dataframe.columns])] +

        rows
    )


