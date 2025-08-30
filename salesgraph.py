from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()
df=pd.read_csv("output.csv")
df["sales"] = df["sales"].str.replace(r"\$", "", regex=True).astype(float)
df["date"] = pd.to_datetime(df["date"])

fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div(
    style={
        "backgroundColor": "#FFFFFF",
        "color": "#2335FA",
    },
    children=[
    html.H1(children="Sales of Pink Morsel Over Time", style={"textAlign": "center"}),

    html.Div(children="This graph shows the sales of pink morsel over time across different regions. As seen, after the price increase on the 15th of January 2021, all regions had an increase in sales."),

    dcc.Graph(
        id="Sales Graph",
        figure=fig,
        style={"backgroundColor": "#000000"}
    ),
    dcc.RadioItems(
        options=[
            {"label":"North", "value":"north"}, 
            {"label":"South", "value":"south"}, 
            {"label":"East", "value":"east"}, 
            {"label":"West", "value":"west"}, 
            {"label":"All Regions", "value":"all"}
        ],
        value="all",
        id="region-selector",
        style={"textAlign": "center"},
        labelStyle={"display": "inline-block"}

    )
])

@app.callback(
    Output("Sales Graph", "figure"),
    Input("region-selector", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
    
    fig = px.line(filtered_df, x="date", y="sales", color="region")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
