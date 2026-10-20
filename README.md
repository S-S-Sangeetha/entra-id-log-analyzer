# Entra ID Sign-in Log Analyzer (Python)

## The Problem
IAM analysts manually review hundreds of Microsoft Entra ID sign-in logs to find suspicious activity (like failed logins or high-risk sign-ins from foreign countries). This is slow and prone to human error.

## The Solution
A Python script that parses Entra ID CSV log exports, applies detection logic (failed status, high risk level), and outputs automated alerts for the security team.

## How It Works
- Uses Python's built-in `csv` module to read the logs.
- Iterates through each row and checks for specific IAM risk indicators.
- Prints an alert and counts the total suspicious events.

## What I Learned
- How to parse enterprise log files using Python.
- How to translate IAM security concepts (Risk Levels, Failed Logins) into Python logic.
- How to automate the daily triage of identity alerts.

- ## Screenshot
- <img width="932" height="336" alt="image" src="https://github.com/user-attachments/assets/a3310a6d-abc7-476b-a032-d33b19a325c7" />
