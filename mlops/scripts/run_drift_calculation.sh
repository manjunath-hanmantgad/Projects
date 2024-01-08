#!/bin/bash

# Navigate to the project directory
cd "D:\development\Projects\mlops"

# Run the drift calculation script and redirect logs to a central location
path/to/python D:\development\Projects\mlops\scripts\drift_calculation.py >> /path/to/central/logs/drift_calculation.log 2>&1
