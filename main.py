import yfinance as yf
import time

print("tracking << XAUUSD >> started ...")

while True:
    #tickers = pair(currency) symbol , interval = timeframe
    data = yf.download(tickers="GC=F", period="1d", interval="1m", progress=False)
    
    if not data.empty:
        current_price = data['Close'].iloc[-1]
        print(f"\r current price: ${current_price}", end="")
    #update time (could be changed)    
    time.sleep(10)