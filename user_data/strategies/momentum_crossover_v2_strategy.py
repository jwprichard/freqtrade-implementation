# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib

class MomentumCrossoverV2Strategy(IStrategy):
    """
    This is the Momentum Crossover strategy, version 2.
    """
    # Strategy interface version - attribute needed by Freqtrade
    INTERFACE_VERSION = 2

    # Minimal ROI designed for the strategy
    minimal_roi = {
        "60": 0.01,
        "30": 0.02,
        "0": 0.04
    }

    # Stoploss:
    stoploss = -0.10

    # Trailing stop:
    trailing_stop = False

    # Optimal timeframe for the strategy
    timeframe = '5m'

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Adds several different TA indicators to the given DataFrame
        """
        # EMA
        dataframe['ema50'] = ta.EMA(dataframe, timeperiod=50)

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)

        # MACD
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']

        # ADX
        dataframe['adx'] = ta.ADX(dataframe, timeperiod=14)

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        """
        dataframe.loc[
            (
                (dataframe['close'] > dataframe['ema50']) &
                (dataframe['rsi'] > 50) &
                (qtpylib.crossed_above(dataframe['macd'], dataframe['macdsignal'])) &
                (dataframe['adx'] > 25)
            ),
            'buy'] = 1

        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        """
        dataframe.loc[
            (
                (qtpylib.crossed_below(dataframe['macd'], dataframe['macdsignal']))
            ),
            'sell'] = 1
        return dataframe
