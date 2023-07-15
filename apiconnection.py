import yfinance as yf

ticker = input("Enter a ticker symbol: ")

## Making ticker object
stock = yf.Ticker(ticker)

## Contain dataframes for historical price data for weeks and months
df_week = stock.history(period="1wk")
df_month = stock.history(period="1mo")

## Closing prices returned as pandas dataframes by yfinance
close_prices_week = df_week["Close"]
close_prices_month = df_month["Close"]

## Loop in selection to prevent error
while True:
    selection = input("View data for week or month? ")

    if selection.lower() == "week":
        print("Historical data for the prior week:")
        print(close_prices_week)
        break
    elif selection.lower() == "month":
        print("Historical data for the prior month:")
        print(close_prices_month)
        break
    else:
        print("Invalid")
