import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html

df = pd.read_csv('merged_marriage_statistics_uganda.csv')

df['Divorce Rate'] = df['Divorce Rate'] * 100

# Create the Dash app
app = Dash(__name__)

# Line chart for Total Marriages over the Years
line_fig = px.line(df, x='Year', y='Total Marriages', title='Total Marriages Over the Years')

# Bar chart for Children Born to Married Couples
bar_fig = px.bar(df, x='Year', y='Children Born to Married Couples', title='Children Born to Married Couples Over the Years')

# Heat map for correlation between variables
heatmap_fig = go.Figure(data=go.Heatmap(
    z=df.corr(),
    x=df.columns,
    y=df.columns,
    colorscale='Viridis'))
heatmap_fig.update_layout(title='Correlation Heatmap')

# Layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='Uganda Marriage Statistics Dashboard'),

    html.Div(children='''
        Interactive visualizations of Uganda marriage statistics.
    '''),

    dcc.Graph(
        id='line-chart',
        figure=line_fig
    ),

    dcc.Graph(
        id='bar-chart',
        figure=bar_fig
    ),

    dcc.Graph(
        id='heatmap',
        figure=heatmap_fig
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
