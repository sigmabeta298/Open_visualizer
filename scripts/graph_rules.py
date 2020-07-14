# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:09:04 2020

@author: Syamanthaka
"""
import pandas as pd

#Graph rules algorithm

# bar_graph {
#      simple_bar{
#          x = str/date & y = int { bar == vertical}
#          x = int & y = str { bar == horizontal}
#          str == unique
#      }
#      split_bar{
#          str != unique
#      }
# }
# pie_graph{
#     x = str & y = int { convert y to %}
# }
# scatter{
#     x = str & y = str
# }
# line{
#      x = str/date y = int
# }
# A simply graph recommender system based on rules implemented in python

int_types = ['int64', 'float64']
str_types = ['object', 'str']
def graph_type(df, x, y):
    boolean_x = df[x].duplicated().any()
    # boolean_y = df[y].duplicated().any()
    x_dtype = df[x].dtype
    y_dtype = df[y].dtype
    
    grf_others = []
    if x_dtype in str_types:
        if boolean_x == False: #all are unique values
            if y_dtype in int_types:
                grf_typ = 'simple_bar_vertical'
                grf_others = ['pie', 'line']
            elif y_dtype in str_types:
                grf_typ = 'scatter'
        else:
            grf_typ = 'split_bar'
    elif x_dtype in int_types:
        if y_dtype in str_types:
            grf_typ = 'simple_bar_horizontal'
        elif y_dtype in int_types:
            grf_typ = 'scatter'
    elif x_dtype == 'date':
        if y_dtype in int_types:
            grf_typ = 'line'
        else :
            grf_typ = 'scatter'
        
    if grf_typ == 'simple_bar_horizontal' or grf_typ == 'simple_bar_vertical' or grf_typ == 'split_bar':
        grf_name = 'bar'
    else:
        grf_name = grf_typ
            
    return grf_typ, grf_others, grf_name
        
