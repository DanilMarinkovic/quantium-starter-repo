from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df=pd.read_csv("output.csv")
df["sales"] = df["sales"].str.replace(r'\$', '', regex=True).astype(float)
df["date"] = pd.to_datetime(df["date"])

fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div(children=[
    html.H1(children='Sales of Pink Morsel Over Time'),

    html.Div(children='''
        This graph shows the sales of "pink morsel" over time across all regions. As seen, after the price increase on the 15th of January 2021, all regions had an increase in sales.
    '''),

    dcc.Graph(
        id='Sales Graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
