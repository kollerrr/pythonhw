import pandas as pd
import plotly
import plotly.express as px
import dash
import psutil 
import matplotlib 
import dash_bootstrap_components as dbc


from dash import Dash, html, dcc, callback, Input, Output

df = pd.read_csv('world2015.csv')

cpu_df = pd.DataFrame()

for i in range(psutil.cpu_count()):

    cpu_df[f"cpu{i+1}"] = [pd.NA] * 100

app = Dash('this is the title', external_stylesheets=[dbc.themes.CYBORG])

items = [

    dbc.DropdownMenuItem('Life_expectancy'),
    dbc.DropdownMenuItem('GDP_per_capita'),
    dbc.DropdownMenuItem('Population'),

]

app.layout = html.Div([

        html.H1("GDP per capita and life expectancy from csv table", 
                style={"text-align": "center", 'color':'white', 'font-size':'4em'}),

        dcc.Tabs(id='tabs', value='tab-1', children=[
                 dcc.Tab(label='World 2015', value='tab-1'),
                 dcc.Tab(label='CPU', value='tab-2')
        ]),

        html.Div(id='tab_component')

    ])


# # @callback(Output("graph", "figure"), Input("x_drop", "value"), 
# #           Input("y_drop", "value"))
# # def update(x, y):
# #     return px.scatter(
# #         df,
# #         x=x,
# #         y=y,
# #         color="Continent",
# #         hover_name="Country",
# #         size="Population",
# #         size_max=50,
# #     )


@callback(Output('tab_content', 'children'), Input('tabs', 'value'))

def render(tab):

    if tab == 'tab-1':

        return html.Div([

            dcc.Dropdown(
                ["Life_expectancy", "GDP_per_capita", "Population"],
                "GDP_per_capita",
                id="x_drop",
            ),
            dcc.Dropdown(
                ["Life_expectancy", "GDP_per_capita", "Population"],
                "Life_expectancy",
                id="y_drop",
            ),
            dcc.Graph(figure={}, id="graph", style={"height": "700px"}),

            ])
    
    if tab == 'tab-2':

        return html.Div([

            dcc.Graph(figure={}, id='cpu_graph'), 
            dcc.Interval(id='timer', interval=250)
        ])


@callback(Output('cpu_graph', 'figure'), Input('timer', 'n_intervals'))

def cpu_update(n):

    cpu_df.iloc[:-1, :] = cpu_df.iloc[1:, :]
    cpu_df.iloc[-1,:] = psutil.cpu_percent(percpu=True)  # core workload

    return px.line(cpu_df, line_shape='spline', range_y=(0,100), template='plotly_dark')


if __name__ == "__main__":
    app.run(debug=True)