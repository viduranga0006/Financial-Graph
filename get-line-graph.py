#!/usr/bin/env python3

import plotly.graph_objects as go
from datetime import datetime
from subprocess import call
import pandas as pd
import os
import sys


_file1 = "./DataFile.csv"

_image_file = "./Line-Graph.png"

qs1_df = pd.read_csv(_file1)

qs1 = go.Scatter(x = qs1_df['DT'], y = qs1_df['OP'],
                  name='Open'
)

qs2 = go.Scatter(x = qs1_df['DT'], y = qs1_df['HIG'],
                  name='High'
)

qs3 = go.Scatter(x = qs1_df['DT'], y = qs1_df['LOW'],
                  name='Low'
)

qs4 = go.Scatter(x = qs1_df['DT'], y = qs1_df['CLS'],
                  name='Close'
)

data = [qs1, qs2, qs3, qs4]
fig = go.Figure(data=data)
web = go.Figure(data=data)

fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price",
        plot_bgcolor='rgb(213,213,213)',
        autosize=True,
        width=1900,
        height=500,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        #paper_bgcolor="LightSteelBlue",
        paper_bgcolor='rgb(255,255,255)',
        showlegend=True
)

web.update_layout(
        xaxis_title="Date",
        yaxis_title="Price",
        plot_bgcolor='rgb(213,213,213)',
        autosize=True,
        width=1900,
        height=500,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        #paper_bgcolor="LightSteelBlue",
        paper_bgcolor='rgb(255,255,255)',
        showlegend=True
)

web.update_layout(xaxis_rangeslider_visible=True)

fig.to_image(format="png", engine="kaleido")
fig.write_image(_image_file)
web.show()
