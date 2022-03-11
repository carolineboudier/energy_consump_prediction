import plotly.express as px
import dataiku
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Uncomment the following to read your own dataset
dataset = dataiku.Dataset("full_data_enriched")
df = dataset.get_dataframe()

fig = px.histogram(df, x="State_Factor", y="site_eui", color="building_class",histfunc="avg",barmode="group",title="Average Site EUI")

app.layout = html.Div(children=[
    html.H1(children='A simple Dash application'),


    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
