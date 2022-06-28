# SOURCE Medium Backtest-stock-trading-strategies

from models.isolation_model import IsolationModel
import backtrader as bt
import pandas as pd
import numpy as np


class MainStrategy(bt.Strategy):
	"""
		Explanation: MainStrategy houses the actions to take as a stream of data flows in a linear fa
	"""
	
	def log(self, txt, dt=None):
	    ''' Logging function fot this strategy'''
	    dt = dt or self.datas[0].datetime.date(0)
	    print('%s, %s' % (dt.isoformat(), txt))
	    
	def __init__(self):
	    self.dataclose = self.datas[0].close
	    self.mean = bt.indicators.SMA(period=20)
	    self.std = bt.indicators.StandardDeviation()
	    self.orderPosition = 0
	    self.z_score = 0
	    
	def next(self):
	    self.log(self.dataclose[0])
	    z_score = (self.dataclose[0] - self.mean[0])/self.std[0]
	    if (z_score >= 2) & (self.orderPosition > 0):
	        self.sell(size=1)
	    if z_score <= -2:
	        self.log('BUY CREATE, %.2f' % self.dataclose[0])
	        self.buy(size=1)
	        self.orderPosition += 1