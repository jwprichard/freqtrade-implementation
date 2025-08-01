# Freqtrade Strategies with Gemini

This project is a laboratory for developing and testing automated cryptocurrency trading strategies using the [Freqtrade](https://www.freqtrade.io/en/stable/) platform. The primary goal of this exercise is to leverage the capabilities of Google's Gemini to create, optimize, and deploy profitable trading strategies.

## Project Overview

[Freqtrade](https://www.freqtrade.io/en/stable/) is a free, open-source crypto trading bot written in Python. It's designed to support all major exchanges and be controlled via Telegram or a web UI. It contains a plethora of features, including backtesting, plotting, and money management tools, in addition to strategy optimization with machine learning.

This project is set up to use Freqtrade with Docker, which simplifies dependency management and deployment.

## The Goal: Profitable Strategies with Gemini

The core objective of this project is to explore the synergy between human guidance and a powerful AI model (Gemini) to achieve the following:

1.  **Strategy Ideation & Creation:** Use Gemini to brainstorm and generate novel trading strategies based on a variety of technical indicators and market conditions.
2.  **Rapid Prototyping:** Quickly translate strategy ideas into functional Freqtrade strategies written in Python.
3.  **Optimization:** Employ Freqtrade's powerful hyperparameter optimization tools to fine-tune strategy parameters for maximum profitability and minimal risk.
4.  **Rigorous Backtesting:** Thoroughly backtest strategies against historical data to evaluate their performance and robustness.
5.  **Deployment:** Deploy promising strategies in a dry-run or live trading environment to validate their performance in real-time market conditions.

By combining the analytical power of Gemini with the robust framework of Freqtrade, we aim to create a streamlined and effective workflow for developing and deploying profitable automated trading strategies.

## Getting Started

### Prerequisites

*   [Google AI Studio](https://aistudio.google.com/) account and API Key.
*   [Gemini CLI](https://github.com/google/generative-ai-docs/blob/main/site/en/tutorials/gemini_cli_tutorial.md) installed and configured with your API key.
*   [Docker](httpss://docs.docker.com/get-docker/) and [Docker Compose](httpss://docs.docker.com/compose/install/)
*   A basic understanding of cryptocurrency trading and technical analysis.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  **Configuration:**
    *   Copy `config.json.example` to `config.json` and customize it with your exchange API keys (if running in live mode), stake settings, and other preferences.
    *   Review the `docker-compose.yml` file to ensure it meets your needs.

### Running the Bot

*   **Dry-run:**
    ```bash
    docker-compose up -d
    ```
*   **Live trading:**
    *   In `config.json`, set `"dry_run": false`.
    *   Run the bot:
        ```bash
        docker-compose up -d
        ```
*   **Web UI:**
    Access the web interface at `http://localhost:8080`.

### Running on Different Architectures (x86 vs. ARM)

This project is configured to run on both standard x86-64 CPUs (most PCs, laptops, and servers) and ARM64 CPUs (like the Raspberry Pi 4). Because Docker images are specific to a CPU architecture, you must tell Docker Compose which one to use.

There are two ways to do this:

#### Method 1: Specify Configuration Files Manually (Recommended for Beginners)

You can specify the correct override file with the `-f` flag for every `docker-compose` command.

**On your x86 PC:**
```bash
# To build and start the container
docker-compose -f docker-compose.yml -f docker-compose.x86.yml up --build -d

# To view logs
docker-compose -f docker-compose.yml -f docker-compose.x86.yml logs -f

# To stop the container
docker-compose -f docker-compose.yml -f docker-compose.x86.yml down
```

**On your Raspberry Pi (ARM):**
```bash
# To build and start the container
docker-compose -f docker-compose.yml -f docker-compose.arm.yml up --build -d

# To view logs
docker-compose -f docker-compose.yml -f docker-compose.arm.yml logs -f

# To stop the container
docker-compose -f docker-compose.yml -f docker-compose.arm.yml down
```

#### Method 2: Use an Environment Variable (More Convenient)

To avoid typing the `-f` flags every time, you can set the `COMPOSE_FILE` environment variable for your shell session.

**On your x86 PC, run this once:**
```bash
export COMPOSE_FILE=docker-compose.yml:docker-compose.x86.yml
```

**On your Raspberry Pi, run this once:**
```bash
export COMPOSE_FILE=docker-compose.yml:docker-compose.arm.yml
```

After running the appropriate `export` command, you can use the standard `docker-compose` commands for the rest of your terminal session:
```bash
# These commands will now work directly
docker-compose up --build -d
docker-compose logs -f
docker-compose down
```
**Note:** To make this setting permanent, add the `export` command to your shell's startup file (e.g., `~/.bashrc` or `~/.zshrc`).

### Development Workflow

1.  **Create a new strategy:**
    *   Use Gemini to help you create a new strategy file in `user_data/strategies/`.
2.  **Backtest the strategy:**
    ```bash
    docker-compose run --rm freqtrade backtesting --config user_data/config.json --strategy <your_strategy_name>
    ```
3.  **Optimize the strategy:**
    ```bash
    docker-compose run --rm freqtrade hyperopt --config user_data/config.json --strategy <your_strategy_name> --epochs 100
    ```
4.  **Deploy the strategy:**
    *   Update the `command` in `docker-compose.yml` to use your new strategy.
    *   Restart the bot:
        ```bash
        docker-compose up -d
        ```

## Disclaimer

Cryptocurrency trading is highly volatile and carries a high level of risk. This project is for educational and experimental purposes only. The strategies and code provided here are not financial advice. You are solely responsible for any financial losses you may incur. Always do your own research and never trade with money you cannot afford to lose.
