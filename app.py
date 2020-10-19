# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 08:56:56 2020

@author: Jonathan
"""

import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

df = pd.read_excel('data.xlsx')
rands = np.random.normal(0, 0.1, size=(df.shape[0], 3))
num_cols = ['Data Source', 'Target Variable', 'Prediction Type']
df[num_cols] = df[num_cols]+rands

fig = px.scatter_3d(df, x='Data Source', y='Target Variable', z='Prediction Type',
              color='Family', width=1000, height=700, title='Machine Learning Exploration', 
              hover_data={'Family': True, 'Technique': True, 'Data Source': False, 'Target Variable': False, 'Prediction Type': False, 'Description': False},
              range_x=[-.15, 1.15], range_y=[-.15, 1.15], range_z=[-1.15, 1.15])

fig.update_layout(scene={'xaxis': {'ticktext': ['Unstructured', 'Structured'], 
                                   'tickvals': [0, 1],
                                   'showbackground': False},
                         'yaxis': {'ticktext': ['Unsupervised', 'Supervised'],
                                   'tickvals': [0, 1]}, 
                         'zaxis': {'ticktext': ['Classification', 'Regression', 'Grouping'],
                                   'tickvals': [0, 1, -1]},
                         'xaxis_showspikes': False,
                         'yaxis_showspikes': False,
                         'zaxis_showspikes': False})

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)