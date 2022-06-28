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