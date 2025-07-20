import yfinance as yf

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    
    if data.empty:
        print("Invalid stock symbol or data unavailable.")
        return

    current_price = stock.info['currentPrice']
    open_price = stock.info['open']
    day_high = stock.info['dayHigh']
    day_low = stock.info['dayLow']
    previous_close = stock.info['previousClose']
    
    change = current_price - previous_close
    percent_change = (change / previous_close) * 100

    print(f"\n📊 Stock: {symbol.upper()}")
    print(f"Current Price: ₹{current_price}")
    print(f"Open: ₹{open_price}")
    print(f"Day High: ₹{day_high}")
    print(f"Day Low: ₹{day_low}")
    print(f"Change: ₹{change:.2f} ({percent_change:.2f}%)\n")

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., INFY, RELIANCE.NS): ")
    get_stock_data(symbol)
