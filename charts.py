import plotly.express as px

def acc_group_borough(df):
    df_temp = df.copy()
    df_temp['BOROUGH'] = df_temp['BOROUGH'].fillna("NIEZNANA (NaN)")

    dane_wykres = df_temp.groupby("BOROUGH").size().reset_index(name="Liczba rekordów")
    dane_wykres = dane_wykres.sort_values(by="Liczba rekordów", ascending=False)

    fig = px.bar(
        dane_wykres,
        x="BOROUGH",
        y="Liczba rekordów",
        text="Liczba rekordów",
        color="Liczba rekordów",
        color_continuous_scale="Viridis",
        title="Liczba kolizji w podziale na dzielnice NYC",
        labels={"BOROUGH": "Dzielnica (Borough)", "Liczba rekordów": "Liczba rekordów"}
    )

    fig.update_layout(
        title_font_size=16,
        title_x=0.5,
        xaxis_tickangle=45,
        coloraxis_showscale=False,
        template="plotly_white"
    )

    fig.update_traces(textposition="outside")

    fig.show()