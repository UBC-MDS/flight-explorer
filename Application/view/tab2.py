import dash_core_components as dcc
import dash_html_components as html
import view.chart1 as chart1
import sys
sys.path.append("..")


tab2_result = html.Div([
            #Insert code for tab2 plot here
            dcc.Dropdown(
        id='dd-chart1',
        options=[
        {'label': 'Incidents', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Fatal incidents', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Fatalities', 'value': '##### Lise, you can pick your value here'},
        {'label': 'Lethality', 'value': '##### Lise, you can pick your value here'},

        ],
        value='##### Lise, this is the default value for drop dowm',
        style=dict(width='45%',
                verticalAlign="middle")
                ),

        html.Iframe(
                sandbox='allow-scripts',
                id='plot1',
                height='1000',
                width='1500',
                style={'border-width': '0'},
                
                srcDoc = chart1.plot1.to_html()
                
                ),

        ])