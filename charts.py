import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def acc_group_borough(df):

    dane_wykres = df.groupby("BOROUGH", dropna=False).size()
    dane_wykres.index = dane_wykres.index.fillna("NIEZNANA (NaN)")
    dane_wykres = dane_wykres.sort_values(ascending=False)
    dzielnice = dane_wykres.index.tolist()
    wartosci = dane_wykres.values.tolist()

    fig, ax = plt.subplots(figsize=(10, 6))

    kolory = [cm.viridis(i / len(dzielnice)) for i in range(len(dzielnice))]

    bars = ax.bar(dzielnice, wartosci, color=kolory, edgecolor="black", linewidth=0.7)

    ax.set_title(
        "Liczba kolizji w podziale na dzielnice NYC", fontsize=14, pad=15
    )
    ax.set_xlabel("Dzielnica (Borough)", fontsize=12, labelpad=10)
    ax.set_ylabel("Liczba rekordów", fontsize=12, labelpad=10)

    ax.set_xticks(range(len(dzielnice)))
    ax.set_xticklabels(dzielnice, rotation=45, ha="right")
    ax.get_yaxis().set_major_formatter(
        ticker.FuncFormatter(lambda x, p: format(int(x), ",d").replace(",", " "))
    )

    ax.grid(axis="y", linestyle="--", alpha=0.7, zorder=0)
    ax.set_axisbelow(True)

    for bar in bars:
        yval = bar.get_height()
        sformatowana_liczba = format(int(yval), ",d").replace(",", " ")
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval + (max(wartosci) * 0.01),
            sformatowana_liczba,
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.tight_layout()

    plt.show()