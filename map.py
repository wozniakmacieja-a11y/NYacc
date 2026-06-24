import plotly.express as px

def accident_map(df):
    df_temp = df.copy()

    df_temp['ON STREET NAME'] = df_temp['ON STREET NAME'].astype(str).str.strip().str.upper()

    niechciane_ulice = ['', 'NAN', 'UNSPECIFIED', 'UNKNOWN', 'UnKnOwN', 'OFF STREET', 'OFF-STREET']
    czyste_ulice = df_temp[~df_temp['ON STREET NAME'].isin(niechciane_ulice)]

    top5_nazwy_ulic = czyste_ulice['ON STREET NAME'].value_counts().head(5).index

    df_filtered = czyste_ulice[
        (czyste_ulice['ON STREET NAME'].isin(top5_nazwy_ulic)) &
        (czyste_ulice['LATITUDE'].notna()) &
        (czyste_ulice['LONGITUDE'].notna()) &
        (czyste_ulice['LATITUDE'] != 0)
        ]

    df_filtered = df_filtered.sort_values(by=['ON STREET NAME', 'LONGITUDE'])

    fig = px.line_map(
        df_filtered,
        lat='LATITUDE',
        lon='LONGITUDE',
        color='ON STREET NAME',
        hover_name='ON STREET NAME',
        hover_data={
            'BOROUGH': True,
            'ACCIDENT DATE': True,
            'ACCIDENT TIME': True,
            'CONTRIBUTING FACTOR VEHICLE 1': True,
            'NUMBER OF PERSONS INJURED': True,
            'LATITUDE': False,
            'LONGITUDE': False
        },
        zoom=10,
        center={"lat": 40.7128, "lon": -74.0060},
        map_style="carto-positron",
        height=750,
        title="Mapa "
    )

    fig.update_traces(line=dict(width=3))

    fig.update_layout(
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        title_text="Geometria TOP 5 najniebezpieczniejszych ulic w NYC",
        title_x=0.5,
        legend_title_text="Nazwa ulicy",
        template="plotly_white"
    )

    return fig