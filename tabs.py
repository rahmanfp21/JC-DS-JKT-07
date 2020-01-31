import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import dash_table


def generate_table(dataframe, page_size=10):
    return dash_table.DataTable(
        id='dataTable',
        columns=[{
            "name": i,
            "id": i
        } for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action="native",
        page_current=0,
        page_size=page_size,
    )


tips = sns.load_dataset('tips')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.H1('Dash Plotly Dashboard'),
        html.Div(children='''
        Created by: Cornellius
    '''),
        dcc.Tabs(
            children=[
                dcc.Tab(
                    value='Tab1',
                    label='Graph Example',
                    children=[
                        html.Div([
                            dcc.Graph(id='example-graph',
                                      figure={
                                          'data': [{
                                              'x': tips['smoker'],
                                              'y': tips['tip'],
                                              'type': 'bar',
                                              'name': 'smoker'
                                          }, {
                                              'x': tips['sex'],
                                              'y': tips['tip'],
                                              'type': 'violin',
                                              'name': 'sex'
                                          }],
                                          'layout': {
                                              'title':
                                              'Tips Dash Data Visualization'
                                          }
                                      })
                        ])
                    ]),
                dcc.Tab(
                    value='Tab2',
                    label='Scatter chart',
                    children=[
                        html.Div(children=dcc.Graph(
                            id='graph-scatter',
                            figure={
                                'data': [
                                    go.Scatter(x=tips[tips['day'] == i]['tip'],
                                               y=tips[tips['day'] == i]
                                               ['total_bill'],
                                               mode='markers',
                                               name='Day {}'.format(i))
                                    for i in tips['day'].unique()
                                ],
                                'layout':
                                go.Layout(
                                    xaxis={'title': 'Tip'},
                                    yaxis={'title': ' Total Bill'},
                                    title='Tips Dash Scatter Visualization',
                                    hovermode='closest')
                            }))
                    ]),
                dcc.Tab(value='Tab3',
                        label='Data Frame Tips',
                        children=[
                            html.Div(children=[
                                html.Div([
                                    html.P('Smoker'),
                                    dcc.Dropdown(value='',
                                                 id='filter-smoker',
                                                 options=[{'label': 'No','value': 'No'}, 
                                                 {'label': 'Yes','value': 'Yes'}])
                                ],
                                         className='col-3'),
                                
                                html.Div([
                                    html.P('Sex'),
                                    dcc.Dropdown(value='',
                                                 id='filter-sex',
                                                 options=[{'label': 'Female','value': 'Female'}, 
                                                 {'label': 'Male','value': 'Male'}])
                                ],
                                         className='col-3'),
                                
                                html.Div([
                                    html.P('Day'),
                                    dcc.Dropdown(value='',
                                                 id='filter-day',
                                                 options=[{'label': i,'value': i} for i in tips['day'].unique()])
                                ],
                                         className='col-3'),
                                html.Div([
                                    html.P('Time'),
                                    dcc.Dropdown(value='',
                                                 id='filter-time',
                                                 options=[{'label': i,'value': i} for i in tips['time'].unique()])
                                ],
                                         className='col-3')

                            ],
                                     className='row'),
                            html.Br(),
                            html.Div([
                                html.P('Max Rows:'),
                                dcc.Input(id ='filter-row',
                                          type = 'number', 
                                          value = 10)
                            ], className = 'row col-3'),

                            html.Div(children =[
                                    html.Button('search',id = 'filter')
                             ],className = 'row col-4'),
                             
                            html.Div(id='div-table',
                                     children=[generate_table(tips)])
                        ])
            ],
            ## Tabs Content Style
            content_style={
                'fontFamily': 'Arial',
                'borderBottom': '1px solid #d6d6d6',
                'borderLeft': '1px solid #d6d6d6',
                'borderRight': '1px solid #d6d6d6',
                'padding': '44px'
            })
    ],
    #Div Paling luar Style
    style={
        'maxWidth': '1200px',
        'margin': '0 auto'
    })

if __name__ == '__main__':
    app.run_server(debug=True)