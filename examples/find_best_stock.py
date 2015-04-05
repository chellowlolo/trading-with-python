''' find the best stock from choices on which you should apply the strategy 
    base on historic data
'''
#!pip install mlboost
from util import strategy 
reload(strategy)

charts = False
verbose = True
months=12

stocks = ["TSLA", "GS", "SCTY", "AMZN", "CSCO", 
          'UTX','JCI',"GOOGL",'AAPL','BP','MSFT']

# try current strategy on different stock
strategy.eval_best(stocks, field='open', months=months, 
                  initialCash=10000, min_stocks=50, 
                  charts=charts, verbose=verbose);
  