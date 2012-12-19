from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma
from pyalgotrade.technical import rsi

class MyStrategy(strategy.Strategy):
    def __init__(self, feed):
        strategy.Strategy.__init__(self, feed)
        self.__rsi = rsi.RSI(feed["orcl"].getCloseDataSeries(), 14)
        self.__sma = ma.SMA(self.__rsi, 15)

    def onBars(self, bars):
        bar = bars["orcl"]
        print "%s: %s %s %s" % (bar.getDateTime(), bar.getClose(), self.__rsi[-1], self.__sma[-1])

# Load the yahoo feed from the CSV file
feed = yahoofeed.Feed()
feed.addBarsFromCSV("orcl", "orcl-2000.csv")

# Evaluate the strategy with the feed's bars.
myStrategy = MyStrategy(feed)
myStrategy.run()

