import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.graph_objects as go

# Prepare data
data = {
    "Year": [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Top10_NextYearReturn(%)": [0.2482, 0.2427, 0.1673, -0.4348, 0.1461, 0.3971, -0.0057, 0.2347, 0.6808, 0.0511, 0.1941, 0.2372,
                             0.2240, 0.0920, 0.3696, 0.4496, 0.3278, -0.1600, 0.0775],
    "Bottom10_NextYearReturn(%)": [0.0855, 0.3052, 0.1381, -0.3389, 1.1789, 0.1406, 0.0059, 0.2928, 0.3348, 0.1239, 0.3209, 0.2347,
                                0.2942, 0.0277, 0.4078, -0.0066, 0.2840, -0.0843, 1.0650],
    "Winner_Portofolio": [12481.7281, 15510.5008, 18105.2384, 10233.6833, 11729.3103, 16387.1974, 16294.2260, 20118.9932,
                          33816.2452, 35543.2645, 42442.3586, 52510.2861, 64274.5980, 70190.4887, 96133.3883,
                          139350.3220, 185033.2458, 155420.0926, 167467.0182],
    "Loser_Portofolio": [10855.3909, 14168.9258, 16125.8541, 10661.4730, 23230.1228, 26497.3002, 26653.5532, 34459.9375,
                         45995.9051, 51692.8045, 68278.5976, 84305.9382, 109108.8300, 112133.4515, 157864.8712,
                         156818.8712, 201360.7204, 184390.2240, 380760.1397]
}

df = pd.DataFrame(data)
df["Top10_NextYearReturn(%)"] = (df["Top10_NextYearReturn(%)"] * 100).round(2)
df["Bottom10_NextYearReturn(%)"] = (df["Bottom10_NextYearReturn(%)"] * 100).round(2)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Portfolio Table"

# Layout
app.layout = html.Div([
    html.H1("📊 Portfolio Performance Table", style={"textAlign": "center"}),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center'},
        style_header={
            'backgroundColor': 'lightblue',
            'fontWeight': 'bold'
        },
    )
])

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
