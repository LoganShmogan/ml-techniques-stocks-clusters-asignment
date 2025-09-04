## -- Quick start guide -- 
import yfinance as yf
dat = yf.Ticker("MSFT")

## -- One ticker symbol -- 
dat = yf.Ticker("MSFT")
dat.info
dat.calendar
dat.analyst_price_targets
dat.quarterly_income_stmt
dat.history(period='1mo')
dat.option_chain(dat.options[0]).calls

## -- Multiple ticker symbol -- 
tickers = yf.Tickers('MSFT AAPL GOOG')
tickers.tickers['MSFT'].info
yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo') 

## -- Funds -- 
spy = yf.Ticker('SPY').funds_data
spy.description
spy.top_holdings