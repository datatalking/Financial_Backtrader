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
        
    def __init__(self, data):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataopen = self.datas[0].open
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low
        self.dataclose = self.datas[0].close
        self.datavolume = self.datas[0].volume