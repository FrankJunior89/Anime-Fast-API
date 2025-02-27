import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import random

# Charger le fichier CSV
df = pd.read_csv('data/animes.csv')

# Sélectionner aléatoirement 12 images de la colonne 'image_url'
sample_df = df.sample(n=12)

selected_images = sample_df['image_url'].to_list()
selected_ids = sample_df['anime_id'].to_list()

# Créer une application Dash
app = dash.Dash(__name__)

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
        ], style={'width': '25%', 'display': 'inline-block', 'text-align': 'center', 'margin-bottom': '20px'}) for i, row in zip(selected_ids,selected_images)
    ], style={'display': 'flex', 'flex-wrap': 'wrap'}),
    html.Div(id='output')
])

# Ajouter des callbacks pour détecter les clics sur les boutons
@app.callback(
    Output('output', 'children'),
    [Input(f'start-{i}', 'n_clicks') for i in selected_ids] +
    [Input(f'rate-{i}', 'n_clicks') for i in selected_ids] +
    [Input(f'finish-{i}', 'n_clicks') for i in selected_ids] +
    [Input(f'schedule-{i}', 'n_clicks') for i in selected_ids]
)
def update_output(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        return 'Aucun bouton cliqué'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if 'rate' in button_id:
            return html.Div([
                html.H3('Formulaire de notation'),
                dcc.Input(id='input-2', type='number', placeholder='Votre note'),
                html.Button('Soumettre', id='submit-button')
            ])
        return f'Le bouton {button_id} a été cliqué'

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)