from datetime import datetime
from pandas import DataFrame
from freqtrade.constants import Config
from freqtrade.optimize.hyperopt import IHyperOptLoss
import numpy as np

class profit_drawdown_loss(IHyperOptLoss):
    """
    A custom hyperopt loss function that prioritizes profit while penalizing for high drawdown.
    """

    @staticmethod
    def calculate_max_drawdown(results: DataFrame) -> float:
        """
        Calculates the maximum drawdown from a series of trades.
        """
        cumulative_profit = results["profit_ratio"].cumsum()
        peak = cumulative_profit.cummax()
        drawdown = (peak - cumulative_profit) / (peak + 1e-9)  # Add epsilon to avoid division by zero
        return drawdown.max()

    @staticmethod
    def hyperopt_loss_function(
        results: DataFrame,
        trade_count: int,
        min_date: datetime,
        max_date: datetime,
        config: Config,
        processed: dict[str, DataFrame],
        *args,
        **kwargs,
    ) -> float:
        """
        Objective function, returns smaller number for better results.
        """
        total_profit = results["profit_ratio"].sum()
        drawdown = profit_drawdown_loss.calculate_max_drawdown(results)

        # Penalize strategies with high drawdown
        drawdown_penalty = drawdown * 2

        # The loss is the negative of the total profit, adjusted by the drawdown penalty.
        # We want to maximize profit, so we minimize the negative profit.
        loss = -total_profit + drawdown_penalty

        # Add a penalty if there are too few trades
        if trade_count < 10:
            loss += (10 - trade_count) * 0.1

        return loss
