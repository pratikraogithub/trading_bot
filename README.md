### 3. Install dependencies
### 4. Create .env file
### 5. Binance Testnet Setup
# Trading Bot — Binance Futures Testnet (Python)

## Overview

This is a simplified Python trading bot that interacts with the Binance Futures Testnet (USDT-M). It provides a small CLI to place Market and Limit orders with input validation and logging.

## Features

- Market and Limit orders
- BUY / SELL side support
- CLI-based input handling and validation
- Structured, modular code under the `bot/` package
- Logging of requests, responses, and errors
- Order status retrieval

## Project Structure

```
trading_bot/
├── bot/
│   ├── client.py           # Binance API client
│   ├── orders.py           # Order placement & retrieval logic
│   ├── validators.py       # Input validation
│   └── logging_config.py   # Logging setup
├── logs/
│   └── trading.log         # Log file (generated)
├── cli.py                  # CLI entry point
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository and change directory:

```bash
git clone <repo-url>
cd trading_bot
```

2. Create a virtual environment and activate it (Windows):

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your testnet credentials:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret
```

5. Binance Futures Testnet base URL (example):

```
https://testnet.binancefuture.com
```

## How to run

Place a market order:

```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

Place a limit order:

```bash
python cli.py BTCUSDT BUY LIMIT 0.001 --price 70000
```

## Sample output

```
Binance Futures Order
--------------------------------
Field         : Value
--------------------------------
Order ID      : 13681543827
Status        : NEW
Executed Qty  : 0.0000
Avg Price     : 0.00
```

## Logging

All logs are written to `logs/trading.log` and include API requests, responses, and errors.

---

If you'd like, I can also reformat or lint the Python files under `bot/` to ensure consistent style.