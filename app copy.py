import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import requests

# Charger le fichier CSV
df = pd.read_csv('data/animes.csv')

# Sélectionner aléatoirement 12 images de la colonne 'image_url'
sample_df = df.sample(n=12)

selected_images = sample_df['image_url'].to_list()
selected_ids = sample_df['anime_id'].to_list()

# Créer une application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Ajouter le lien vers Font Awesome et inclure les éléments requis
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Dash</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        {%metas%}
        {%favicon%}
        {%css%}
    </head>
    <body>
        <div id="react-entry-point">
            {%app_entry%}
        </div>
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Définir la disposition de l'application
app.layout = html.Div([
    html.H1('Images d\'anime aléatoires'),
    html.Div([
        html.Div([
            html.Img(src=row, style={'width': '100%'}),
            html.Div([
                html.Button(html.I(className='fas fa-play'), id=f'start-{i}', style={'width': '24%'}),
                html.Button(html.I(className='fas fa-star'), id=f'rate-{i}', style={'width': '24%'}),
                html.Button(html.I(className='fas fa-check'), id=f'finish-{i}', style={'width': '24%'}),
                html.Button(html.I(className='fas fa-calendar-alt'), id=f'schedule-{i}', style={'width': '24%'})
            ], style={'display': 'flex', 'justify-content': 'space-between', 'margin-top': '10px'})
        ], style={'width': '25%', 'display': 'inline-block', 'text-align': 'center', 'margin-bottom': '20px'}) for i, row in zip(selected_ids, selected_images)
    ], style={'display': 'flex', 'flex-wrap': 'wrap'}),
    html.Div(id='output'),
    dcc.Store(id='form-data'),
    dbc.Modal(
        [
            dbc.ModalHeader("Formulaire de notation"),
            dbc.ModalBody([
                dcc.Input(id='input-1', type='text', placeholder='Votre nom', style={'margin-bottom': '10px'}),
                dcc.Input(id='input-2', type='number', placeholder='Votre note', style={'margin-bottom': '10px'}),
            ]),
            dbc.ModalFooter(
                dbc.Button("Soumettre", id='submit-button', className='ml-auto')
            ),
        ],
        id='modal',
        is_open=False,
    )
])

# Ajouter des callbacks pour détecter les clics sur les boutons
@app.callback(
    Output('modal', 'is_open'),
    [Input(f'rate-{i}', 'n_clicks') for i in selected_ids],
    [State('modal', 'is_open')]
)
def toggle_modal(*args, is_open):
    ctx = dash.callback_context

    if not ctx.triggered:
        return is_open
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if 'rate' in button_id:
            return not is_open
        return is_open

@app.callback(
    Output('form-data', 'data'),
    Input('submit-button', 'n_clicks'),
    State('input-1', 'value'),
    State('input-2', 'value')
)
def submit_form(n_clicks, name, rating):
    if n_clicks:
        data = {'name': name, 'rating': rating}
        response = requests.post('https://votre-api.com/endpoint', json=data)
        return f'Formulaire soumis avec succès : {response.status_code}'
    return None

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)