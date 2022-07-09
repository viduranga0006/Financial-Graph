#!/usr/bin/env python3

import plotly.graph_objects as go
from datetime import datetime
from subprocess import call
import pandas as pd
import os
import sys

_file1 = "./DataFile.csv"

_image_file = "./OHLC-Graph.png"

qs1_df = pd.read_csv(_file1)

fig = go.Figure(data=go.Ohlc(x=qs1_df['DT'],
                open=qs1_df['OP'],
                high=qs1_df['HIG'],
                low=qs1_df['LOW'],
                close=qs1_df['CLS']))

web = go.Figure(data=go.Ohlc(x=qs1_df['DT'],
                open=qs1_df['OP'],
                high=qs1_df['HIG'],
                low=qs1_df['LOW'],
                close=qs1_df['CLS']))

fig.update(layout_xaxis_rangeslider_visible=False)

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
        height=600,
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

fig.to_image(format="png", engine="kaleido")
fig.write_image(_image_file)
web.show()
