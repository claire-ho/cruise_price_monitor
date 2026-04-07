#!/bin/bash

# Change to the project directory
cd /Users/chinglanho/work/ml/llm/AlaskaCruise

# Activate the virtual environment
source venv/bin/activate

# Optional: Run the python crawler and save output
python3 crawl_prices.py > last_run.log 2>&1

# If you also want to send the AppleScript email after crawling:
# osascript send_prices.scpt
