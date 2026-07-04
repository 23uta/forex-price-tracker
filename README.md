
# Real-Time Forex Price Tracker

A lightweight, real-time financial market monitoring utility written in Python. This script establishes a continuous polling pipeline with the Yahoo Finance API to track live price fluctuations of Gold futures (`GC=F`) at 1-minute intervals. It utilizes specialized terminal control characters to output a dynamic, single-line streaming ticker directly in the console.

This script serves as the **Real-Time Streaming Layer** for automated trading systems or alerting dashboards.

## 🚀 Features

- **Live Market Polling:** Continuously fetches the latest market closing price for Gold using high-frequency polling logic.
- **Dynamic Terminal UI:** Leverages carriage return (`\r`) mechanics to overwrite the terminal line in place, creating a clean, professional live-updating ticker display instead of flooding the console history.
- **Adjustable Frequency:** Built-in sleep interval management to control API polling rates and optimize system resource consumption.

## 🛠️ Tech Stack & Requirements

- **yfinance** - For live financial data streaming and retrieval.
- **time (Standard Library)** - For polling interval and thread throttling.

## 📦 Quick Start & Setup

1. **Create the Repository Files:**
   Create a new file in your GitHub repository named `README.md` and paste this content inside it.

2. **Install Dependencies:**
   Ensure you have the streaming library installed:
   ```bash
   pip install yfinance

3. **Deployment:**
    Save the Python script (e.g., `main.py`) in your project root directory.

## 📈 Execution

Launch the real-time stream from your console:

```bash
python main.py 

```

### Expected Output:

The console will initialize the pipeline and maintain a single-line streaming update of the asset value:

```text
tracking << XAUUSD >> started ...
 current price: $2345.85

```

*(The price line above will update dynamically every 10 seconds without generating new lines)*

## ⚙️ Customization

You can easily adjust the live tracking update frequency by changing the `time.sleep()` value at the bottom of the script:

```python
# Change 10 to 5 for faster updates, or to 60 for minute-by-minute tracking
time.sleep(10)

```
