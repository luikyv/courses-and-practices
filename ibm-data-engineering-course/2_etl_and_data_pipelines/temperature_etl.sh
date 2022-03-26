#! /bin/bash
# This is just an example of what a shell script looks like

# Extract reading with get_temp_API
# Append reading to temperature.log
get_temp_api >> temperature.log

# Buffer last hour of readings
tail -60 temperature.log > temperature.log

# Call get_stats.py to aggregate the readings
python3 get_stats.py temperature.log temp_stats.csv

# Load the stats using load_stats_api
load_stats_api temp_stats.csb
