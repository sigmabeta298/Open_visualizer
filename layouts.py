# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:37:40 2020

@author: Syamanthaka
"""

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_daq as daq
import data_n_graphs as grf

title = html.Div([
    dbc.Row(dbc.Col(html.Div("Open Visualizer", className="navbar")))
])

#######################################################################
#*********************************************************************
leftside_col = dbc.Col([
    html.Div("Select X axis column", className='labels'),
    dcc.Dropdown(
        id='x-dropdown',
        options=[],
        placeholder='Options ',
        disabled=False
    ),
    html.Hr(),
    html.Div("Select Y axis column", className='labels'),
    dcc.Dropdown(
        id='y-dropdown',
        options=[],
        placeholder='Options',
        disabled=False
    ),
    html.Br(),
], width=3, className='column_left')
#*********************************************************************

center_col = dbc.Col([
    html.Div('Upload file to visualize (currently accepting only .csv)'),
    dcc.Upload(
        id='upload-data',
        children=
        html.Div([
            'Drag and Drop or Click to Select File'
        ], className='upload_box'),
        multiple=False
    ),
    
    html.Div(id='data_df', style={'display': 'none'}), #Hidden div to store uploaded data
    html.Div(id='selected_cols', className='info_user'),
    html.Div(id='output_grf'),
    html.Div(id='output-data-upload'), #Data display, can be removed later
], width=7, className='column_right')

rightside_col = dbc.Col([
    html.Div("Select Graph Type", className='labels'),
    dcc.Dropdown(
        id='grf_typ',
        options=[
              {'label': 'Bar', 'value': 'bar'},
              {'label': 'Scatter', 'value': 'scatter'},
              {'label': 'Line', 'value': 'line'},
              {'label': 'Pie', 'value': 'pie'}
          ],
        value='bar',
        disabled=False
    ),
   
    html.Div(id='dd_val'),
    daq.ColorPicker(
        id='my-color-picker',
        label='Color Picker',
        value=dict(hex='#2a20aa')
    ),
    dcc.Input(id='main_title', type='text', value='', placeholder='Main Title'),
    dcc.Input(id='xtitle', type='text', value='', placeholder='X axis'),
    dcc.Input(id='ytitle', type='text', value='', placeholder='Y axis'),

], width=2)

#*********************************************************************
#Layout1
layout1 = html.Div([
    dbc.Container([
    dbc.Row([
        leftside_col,
        center_col,
        rightside_col    
    ]),
    ],fluid=True)
 ])

#*********************************************************************
