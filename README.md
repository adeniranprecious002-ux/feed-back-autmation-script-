# Car Feedback Automation Script

An automated Python tool designed to process raw text customer reviews, serialize them into structured data, and upload them to a corporate web service via a REST API. 

This project was built as part of the Google IT Automation Capstone.

## Features
- Iterates through local directories using the Python `os` module.
- Parses unstructured, multi-line text files into Python dictionaries.
- Transmits data payloads asynchronously to a Django web application using standard `POST` requests via the `requests` library.

## Getting Started

### Prerequisites
- Python 3.x
- `requests` library

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adeniranprecious002-ux/feed-back-automation.git
