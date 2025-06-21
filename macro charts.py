import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.xlsx'
sheets = ['GDP growth', 'Inflation', 'Exchange rate']

def plot_macro_trend(sheet_name, title, ylabel, filename):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df.set_index('Country', inplace=True)
    df = df.transpose()
    df = df.apply(pd.to_numeric, errors='coerce')  # Convert strings to NaN
    df.dropna(inplace=True)  

    plt.figure(figsize=(10, 6))
    for country in df.columns:
        plt.plot(df.index, df[country], marker='o', label=country)

    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

plot_macro_trend(
    sheet_name='GDP growth',
    title='Annual GDP Growth (%)',
    ylabel='GDP Growth (%)',
    filename='gdp_growth.png'
)

plot_macro_trend(
    sheet_name='Inflation',
    title='Annual Inflation Rate (YoY %)',
    ylabel='Inflation (%)',
    filename='inflation_trend.png'
)

plot_macro_trend(
    sheet_name='Exchange rate',
    title='Exchange Rate vs USD (Local Currency)',
    ylabel='Local Currency per USD',
    filename='exchange_rate.png'
)
