# SOURCE Medium Backtest-stock-trading-strategies

from datetime import datetime
from strategies.reversion_strategy import LongOnlyReversion
from tools.backtesting_tools import backtesting_engine

"""
    Script for backtesting strategies
"""

if __name__ == '__main__':
	# Run backtesting engine
	
	backtesting_engine(
		symbol='AAPL', strategy=LongOnlyReversion,
		fromdate=datetime(2018, 1, 1), todate=datetime(2019, 1, 1)
	)