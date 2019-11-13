import plotly.graph_objects as go
import pandas as pd

# opening the file provided using pandas.
df = pd.read_csv('World_Map.csv')

# Plotting Choropleth map
fig = go.Figure(data=go.Choropleth(
    locations = df['CODE'],
    z = df['TEMP'],
    text = df['COUNTRY'],
    colorscale = 'Reds',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = 'degree C - ',
    colorbar_title = ' ',
))

fig.update_layout(
    title_text=' ',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
        showarrow = False
    )]
)

fig.show()
