# Report Generation and Tracking Script
## Overview
This Python script automates the process of generating and modifying reports based on a template Excel file. It tracks and calculates various metrics related to applications received or processed over time, such as counts of applications processed in the current and previous quarters, updating processed counts, and calculating service standards compliance.

## Features
1. Date Handling:
- Automatically determines the current date, previous quarter, and handles quarter-specific data.

2. Sheet Duplication:
- Duplicates the reference sheet for the previous quarter and updates it with the latest data for the current quarter.

3. Count and Process Tracking:
- Counts the number of applications processed or received in the relevant time period.
- Updates these counts in the new report.

4. Service Standards:
- Calculates and updates whether the service standards were met for applications processed in the current and previous quarter.
- Computes percentages based on defined thresholds (e.g., time taken to process applications).

5. Excel Operations:
- Uses the openpyxl library to read, write, and manipulate Excel files.

6. Statistics Calculations:
- Calculates the mean and median for time taken to process applications, with data aggregation based on monthly time frames.

Note: Some of the details are intentionally omitted or generalized for privacy and security reasons.
