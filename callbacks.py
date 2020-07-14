# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:11:45 2020

@author: Syamanthaka
"""

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app
# import layouts as lyt
import data_n_graphs as grf

@app.callback([Output('output-data-upload', 'children'),
               Output('x-dropdown', 'options'),
               Output('y-dropdown', 'options'),
               Output('data_df', 'children')],
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
def update_output(contents, filename):
    if contents is not None:
        contents_df, cols, the_df = grf.parse_contents(contents, filename)
        return contents_df, cols, cols, the_df

@app.callback([Output('selected_cols', 'children'),
               Output('output_grf', 'children'),
               Output('main_title', 'placeholder'),
               Output('xtitle', 'placeholder'),
               Output('ytitle', 'placeholder'),
               Output('dd_val', 'value')
               ],
              [Input('data_df', 'children'),
               Input('x-dropdown', 'value'),
               Input('y-dropdown', 'value'),
               Input('grf_typ', 'value'),
               Input('my-color-picker', 'value'),
               Input('main_title', 'value'),
               Input('xtitle', 'value'),
               Input('ytitle', 'value')
              ],
              [State('x-dropdown', 'value'),
               State('y-dropdown', 'value')
              ])
def update_dds(df, x, y, gtyp, sel_color, mtitle_val, xtitle_val, ytitle_val, x_state, y_state):
    if not (x_state and y_state):
        raise PreventUpdate

    main_title = mtitle_val if mtitle_val != '' else x + ' vs ' + y
    xtitle = xtitle_val if xtitle_val != '' else x
    ytitle = ytitle_val if ytitle_val != '' else y
    
    grf_obj, grf_typ_new =  grf.plot_grf(df, x, y, gtyp, sel_color, main_title, xtitle, ytitle)
    sel_txt = 'You have selected ' + x + ' and ' + y
    
    return sel_txt, grf_obj, main_title, xtitle, ytitle, grf_typ_new
 
@app.callback(Output('grf_typ', 'value'),
              [Input('dd_val', 'value')])
def update_bar_type(hidden_val):
    return hidden_val
              