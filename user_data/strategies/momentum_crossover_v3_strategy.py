# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy, IntParameter, DecimalParameter
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib

class momentum_crossover_v3_strategy(IStrategy):
    """
    This is the Momentum Crossover strategy, version 3, with hyperoptable parameters.
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

    # Hyperoptable parameters
    buy_ema_period = IntParameter(20, 100, default=50, space="buy")
    buy_rsi_level = IntParameter(30, 70, default=50, space="buy")
    buy_adx_level = IntParameter(20, 50, default=25, space="buy")
    sell_rsi_level = IntParameter(30, 70, default=50, space="sell")

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Adds several different TA indicators to the given DataFrame
        """
        # EMA
        dataframe['ema'] = ta.EMA(dataframe, timeperiod=self.buy_ema_period.value)

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
                (dataframe['close'] > dataframe['ema']) &
                (dataframe['rsi'] > self.buy_rsi_level.value) &
                (qtpylib.crossed_above(dataframe['macd'], dataframe['macdsignal'])) &
                (dataframe['adx'] > self.buy_adx_level.value)
            ),
            'buy'] = 1

        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        """
        dataframe.loc[
            (
                (qtpylib.crossed_below(dataframe['macd'], dataframe['macdsignal'])) &
                (dataframe['rsi'] > self.sell_rsi_level.value)
            ),
            'sell'] = 1
        return dataframe
