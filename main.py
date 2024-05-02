
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Load the dataset that has been downloaded using 'get_data.py'
data_path = 'LoyersMoyen2023.xlsx'  # Make sure this path is where 'get_data.py' saves the file
data = pd.read_excel(data_path)

# Create a Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='type-dropdown',
                options=[{'label': i, 'value': i} for i in data['type'].unique()],
                value='ensemble',
                clearable=False
            ),
            dcc.Graph(id='loyer-histogram')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='geo-map')
        ], width=6)
    ])
])

@app.callback(
    Output('loyer-histogram', 'figure'),
    Input('type-dropdown', 'value')
)
def update_histogram(selected_type):
    filtered_data = data[data['type'] == selected_type]
    fig = px.histogram(filtered_data, x='Loyer', nbins=30, title="Distribution des Loyers")
    return fig

@app.callback(
    Output('geo-map', 'figure'),
    Input('type-dropdown', 'value')
)
def update_map(selected_type):
    filtered_data = data[data['type'] == selected_type]
    # Dummy lat and lon for the example; replace with real data if available
    fig = px.scatter_geo(filtered_data, lat=pd.Series([48.8566]*len(filtered_data)), lon=pd.Series([2.3522]*len(filtered_data)),
                         title="Carte des Loyers")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
