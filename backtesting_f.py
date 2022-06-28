# SOURCE Medium Backtest-stock-trading-strategies

import backtrader as bt
import pyfolio as pf


def backtesting_engine(symbol, strategy, fromdate, todate, args=None):
	"""
		Primary function for backtesting, not entirely parameterized
	"""
	
	# Backtesting Engine
	cerebro = bt.Cerebro()
	
	# Add a Strategy if no Data Required for the model
	if args is None:
		cerebro.addstrategy(strategy)
	# If the Strategy requires a Model and therefore data
	elif args is not None:
		cerebro.addstrategy(strategy, args)
	
	# Retrieve Data from YahooFinance
	data = bt.feeds.YahooFinanceData(
		dataname=symbol,
		fromdate=fromdate,  # datetime.date(2015, 1, 1)
		todate=todate,  # datetime.datetime(2016, 1, 1)
		reverse=False
	)
	
	# Add Data to Backtesting Engine
	cerebro.adddata(data)
	
	# Set Initial Portfolio Value
	cerebro.broker.setcash(100000.0)