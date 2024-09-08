# Local Email Automation Tool

This project automates the process of sending greeting emails templates to your subscribers. It retrieves subscriber data from a CSV file stored locally and sends emails using your Outlook account through the `smtplib` library.

## Features

- Reads subscriber information (name and email) from a CSV file.
- Processes and stores data locally.
- Connects to Outlook using Python's `smtplib` to send emails.
- Automatically loops through the subscriber list and sends a greeting email.
