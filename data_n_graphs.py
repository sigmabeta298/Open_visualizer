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
from scripts import graph_rules as grules

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

    the_col_names = [{'label': i + ' (' + str(df[i].dtypes) + ')', 'value': i} for i in col_names]
    the_df = df.to_json(date_format='iso', orient='split')
    
    
    table = html.Div([
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),
    ])
    
    return table, the_col_names, the_df

def plot_grf(df_json, x_col, y_col, grf_typ_ud, sel_color, mtitle, xtitle, ytitle):
    df = pd.read_json(df_json, orient='split')
    
    # Get a graph type from the graph rules
    grf_type, grf_others, grf_name = grules.graph_type(df, x_col, y_col)
    
    #See if user selection is a viable option to plot
    if grf_typ_ud != grf_name: #User selection is not recommended
        
        #check if grf_type present in grf_others
        if grf_typ_ud in grf_others:
            grf_type = grf_typ_ud #Set graph type for plotting
            grf_name = grf_typ_ud #Set graph name for changing dropdown
        else:
            grf_comp = html.Div(children=
                "Sorry this cannot be plotted. We recommend " + grf_name,
                className='error_txt'
            )
            return grf_comp, grf_typ_ud
            
    
    
    fig = go.Figure()
    
    if grf_type == 'scatter':
        fig.add_trace(go.Scatter(x=df[x_col], y=df[y_col], 
                                        mode='markers', 
                                        marker_color= sel_color['hex']))
    elif grf_type == 'line':
        fig.add_trace(go.Scatter(x=df[x_col], y=df[y_col], 
                                        line=dict(color=sel_color['hex'])))
    elif grf_type == 'pie':
        fig.add_trace(go.Pie(labels=df[x_col], values=df[y_col]))
    elif grf_type == 'simple_bar_horizontal':
        fig.add_trace(go.Bar(x=df[x_col], y=df[y_col],
                                marker_color=sel_color['hex'], 
                                orientation='h'))
    else:
        fig.add_trace(go.Bar(x=df[x_col], y=df[y_col],
                                marker_color=sel_color['hex']))
        
    fig.update_layout(
        title = mtitle,
        xaxis_title = xtitle,
        yaxis_title = ytitle
    )
    

    grf_comp = dcc.Graph(
            id='main_grf',
            figure=fig
        )
    return grf_comp, grf_name
