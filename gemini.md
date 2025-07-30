This project is a Freqtrade cryptocurrency trading bot. Freqtrade is a free, open-source Python-based bot for developing, backtesting, and optimizing trading strategies. It can be controlled via Telegram or a web UI and supports major exchanges like Binance and Kraken.

## Gemini's Role

My role in this project is to assist with the following:

*   **Configuration:** Help with setting up and modifying the `config.json` file, including trading parameters, exchange settings, and other bot configurations.
*   **Strategy Customization:** Assist in the development and customization of trading strategies. This includes:
    *   Adding and modifying indicators.
    *   Defining entry and exit signals.
    *   Implementing stop-loss and ROI settings.
    *   Using informative pairs for more advanced strategies.

## Session Summaries

At the end of a session, I can create a summary document in the `Gemini Session Summaries` folder. These summaries serve as a record of our work. They are:

*   **Dated and Titled:** For easy chronological ordering and identification.
*   **A Log of Work:** They provide a detailed account of the key activities, debugging steps, and outcomes of the session.
*   **A Quick Reference:** They allow you to quickly recall the context and progress of our work together.

## Key Files

*   `docker-compose.yml`: Defines the services for running Freqtrade.
*   `user_data/config.json`: Main configuration for the bot (stake, exchange, pairs, etc.).
*   `user_data/strategies/`: Location for your custom trading strategy Python files.
*   `user_data/hyperopts/`: Location for custom hyperopt loss functions.

## Common Commands

*   **Running in dry-run/live:** `docker-compose run --rm freqtrade trade --config user_data/config.json --strategy sample_strategy`
*   **Backtesting:** `docker-compose run --rm freqtrade backtesting --config user_data/config.json --strategy sample_strategy`
*   **Hyperoptimization:** `docker-compose run --rm freqtrade hyperopt --config user_data/config.json --strategy sample_strategy --hyperopt-loss sample_hyperopt_loss --epochs 100`
*   **Download Data:** `docker-compose run --rm freqtrade download-data --config user_data/config.json --timerange 20230101-`

## Development Workflow

1.  Modify the strategy file in `user_data/strategies/`.
2.  Run backtesting to evaluate performance.
3.  Run hyperoptimization to find optimal parameters.
4.  Deploy the strategy for dry-run or live trading.

## Coding Language and Best Practices

*   **Language:** The primary coding language for this project is Python. Strategies are written as Python classes that inherit from Freqtrade's `IStrategy` class.
*   **Libraries:** Strategies heavily utilize libraries like `pandas` for data manipulation and technical analysis libraries such as `technical` and `pandas-ta`.
*   **Best Practices:**
    *   **Avoid Lookahead Bias:** Never use future data to calculate signals. Freqtrade provides tools to help detect this.
    *   **Vectorized Operations:** Use vectorized operations with `pandas` and `numpy` instead of loops for better performance.
    *   **Thorough Backtesting:** Test strategies against a variety of historical market conditions.
    *   **Forward Testing:** Use the dry-run mode to validate backtesting results on live data before deploying with real funds.
    *   **Risk Management:** Always implement a stop-loss and consider using the minimal ROI table for taking profits.

## Data Management

*   **Downloading Data:** Use the `download-data` command to get historical data for backtesting. The data is stored in `user_data/data/`.
*   **Example:** `docker-compose run --rm freqtrade download-data --config user_data/config.json --timerange 20230101-`

## Logging and Debugging

*   **Log File:** The main log file is located at `user_data/logs/freqtrade.log`. This file is essential for troubleshooting both the bot and strategy execution.
*   **Increasing Verbosity:** Use the `-v` or `--verbose` flag with `freqtrade` commands to get more detailed log output.

## Telegram Integration

*   **Configuration:** Enable and configure Telegram integration in `config.json` by setting `telegram.enabled` to `true` and providing your bot token and chat ID.
*   **Benefits:** Receive real-time notifications of trades, status updates, and control the bot remotely with commands like `/status`, `/profit`, and `/stop`.

## External Resources

*   **Official Documentation:** [https://www.freqtrade.io/en/stable/](https://www.freqtrade.io/en/stable/)
*   **Strategy Repository:** [https://github.com/freqtrade/freqtrade-strategies](https://github.com/freqtrade/freqtrade-strategies)
*   **Community Discord:** [https://discord.gg/freqtrade](https://discord.gg/freqtrade)
