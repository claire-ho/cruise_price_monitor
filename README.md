# Cruise Price Monitor

A Python-based crawler using Playwright to monitor room prices for specific Princess Cruises voyages.

## Features
- Crawls dynamic pricing for specific state room types.
- Supports filtering for:
  - Balcony
  - Deluxe Balcony
  - Premium Deluxe Balcony
  - Mini-Suite
- Extracts the most frequent/starting price for each category.
- Composes a `mailto:` link to easily send results via email.

## Requirements
- Python 3.7+
- Playwright

## Setup
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install playwright
   playwright install chromium
   ```

## Usage
Run the crawler:
```bash
python3 crawl_prices.py
```

The script will navigate to the configured URLs, wait for the dynamic content to load, and print the identified prices for the requested room categories.

## Automated Scheduling (Launchd)
A script has been configured to run this crawler automatically 3 times a day (at 8:00 AM, 2:00 PM, and 8:00 PM) via macOS `launchd`.

- **Wrapper Script**: `run_monitor.sh` runs the crawler within the virtual environment and saves the output to `last_run.log`.
- **LaunchAgent Plist**: `com.chinglanho.alaskacruise.plist` defines the schedule.

To set up the scheduled job, copy the plist to your LaunchAgents directory and load it:
```bash
# Copy the file
cp com.chinglanho.alaskacruise.plist ~/Library/LaunchAgents/

# Load and start the schedule
launchctl load ~/Library/LaunchAgents/com.chinglanho.alaskacruise.plist

# Unload and stop the schedule (if needed)
launchctl unload ~/Library/LaunchAgents/com.chinglanho.alaskacruise.plist
```
Output from scheduled runs will be written to `launchd_out.log` and `launchd_err.log` inside the project directory.
