# New Trading Strategy: "Momentum Crossover"

This document outlines the requirements for a new trading strategy called "Momentum Crossover". The goal is to create a strategy that is more sophisticated and profitable than the default `SampleStrategy`.

## Strategy Overview

The "Momentum Crossover" strategy is a trend-following strategy that aims to identify strong market trends and capitalize on them. It uses a combination of momentum and moving average indicators to generate entry and exit signals.

## Indicators

The strategy will use the following indicators:

*   **Exponential Moving Average (EMA):** A 50-period EMA will be used to identify the overall trend direction.
*   **Relative Strength Index (RSI):** A 14-period RSI will be used to measure the momentum of the market.
*   **Moving Average Convergence Divergence (MACD):** The MACD will be used to confirm trend changes and generate entry/exit signals.

## Entry Signal (Buy)

A buy signal is generated when all of the following conditions are met:

1.  The closing price is above the 50-period EMA.
2.  The RSI is above 50.
3.  The MACD line crosses above the MACD signal line.

## Exit Signal (Sell)

A sell signal is generated when any of the following conditions are met:

1.  The MACD line crosses below the MACD signal line.
2.  The RSI drops below 30.

## Risk Management

*   **Stop-Loss:** A hard stop-loss will be set at 10% below the entry price.
*   **Minimal ROI:** The following minimal ROI table will be used:
    *   `60 minutes`: 1%
    *   `30 minutes`: 2%
    *   `0 minutes`: 4%

## Best Practices

The implementation of this strategy will adhere to the best practices outlined in the `gemini.md` file, including:

*   **No Lookahead Bias:** The strategy will only use historical data to make decisions.
*   **Vectorized Operations:** The strategy will use `pandas` and `numpy` for efficient calculations.
*   **Thorough Backtesting:** The strategy will be backtested against a variety of market conditions.
*   **Risk Management:** The strategy will include a stop-loss and a minimal ROI table.
