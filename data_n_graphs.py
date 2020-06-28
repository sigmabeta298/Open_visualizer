# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:11:45 2020

@author: Syamanthaka B
"""
import pandas as pd
import plotly.graph_objects as go
import base64
import io
import dash_html_components as html
import dash_core_components as dcc

import dash_table

def parse_contents(contents, filename): 
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
         if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
         else:
            raise Exception('Not csv file')
    except Exception as e:
        print(e)
        return html.Div([
            'Please upload csv file'
        ])

    col_names = df.columns
    the_col_names = [{'label': i, 'value': i} for i in col_names]
    the_df = df.to_json(date_format='iso', orient='split')
    
    
    table = html.Div([
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),
    ])
    
    return table, the_col_names, the_df

def plot_grf(df_json, x_col, y_col, grf_typ):
    df = pd.read_json(df_json, orient='split')
    
    if grf_typ == 'scatter':
        fig = go.Figure(data=go.Scatter(x=df[x_col], y=df[y_col], mode='markers'))
    elif grf_typ == 'line':
        fig = go.Figure(data=go.Scatter(x=df[x_col], y=df[y_col]))
    else:
        fig = go.Figure([go.Bar(x=df[x_col], y=df[y_col])])
    
    grf_comp = dcc.Graph(
            id='main_grf',
            figure=fig
        )
    return grf_comp
