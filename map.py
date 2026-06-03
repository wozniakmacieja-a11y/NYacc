import plotly.express as px

def accident_map(df_filtered):

    fig = px.scatter_map(
        df_filtered,
        lat='LATITUDE',
        lon='LONGITUDE',
        zoom=10,
        center={"lat": 40.7128, "lon": -74.0060},
        hover_name='BOROUGH',
        hover_data={
            'ACCIDENT DATE': True,
            'ACCIDENT TIME': True,
            'CONTRIBUTING FACTOR VEHICLE 1': True,
            'NUMBER OF PERSONS INJURED': True,
            'LATITUDE': False,
            'LONGITUDE': False
        },
        map_style="carto-positron",
        height=750,
        title="Mapa wypadków w Nowym Jorku"
    )

    fig.update_traces(cluster=dict(enabled=True, color="yellow", size=10))
    fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})

    return fig