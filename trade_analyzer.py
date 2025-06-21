import numpy as np
import pandas as pd
import plotly.express as px

symbols = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
quantities = np.random.randint(10, 200, 10)
prices = np.random.uniform(100, 500, 10)
fees = np.random.uniform(1, 10, 10)
symbols_random = np.random.choice(symbols, 10)


df = pd.DataFrame({
    'Symbol': symbols_random,
    'Quantity': quantities,
    'Price': prices.round(2),
    'Fees': fees.round(2)
})


df['TotalCost'] = (df['Quantity'] * df['Price'] + df['Fees']).round(2)


print("\nTrade Data:\n", df)


# fig = px.bar(df, x='Symbol', y='TotalCost',
#              color='Symbol',
#              title='Trade Costs by Stock',
#              text='TotalCost')

# fig = px.scatter(df, x='Symbol', y='TotalCost',
#              color='Symbol',
#              title='Trade Costs by Stock',
#              text='TotalCost')

fig = px.line(df, x='Symbol', y='TotalCost',
             color='Symbol',
             title='Trade Costs by Stock',
             text='TotalCost')

#fig.show()

fig.write_html("trade_analyzer_line.html")