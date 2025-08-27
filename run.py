import yfinance as yf

apple = yf.Ticker("aapl")

# pandas dataFrame containing dividends and splits
corpAction = apple.actions

# pandas dataFrame containing historical accounting data
financials = apple.financials
financialsTimestamps = financials.columns.values.tolist()

print(financialsTimestamps)
