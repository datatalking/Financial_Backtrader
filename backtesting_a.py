# SOURCE Medium Backtest-stock-trading-strategies

import backtrader as bt


def backtesting_engine(symbol, strategy, fromdate, todate, args=None):
	"""
		Primary function for backtesting, not entirely parameterized
	"""
	# Backtesting Engine
	cerebro = bt.Cerebro()