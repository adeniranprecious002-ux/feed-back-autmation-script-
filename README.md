# Car Feedback Automation Script

An automated Python tool that processes raw customer feedback, converts unstructured text into structured data, and uploads it to a web service via a REST API.

This project was developed as part of the **Google IT Automation with Python Professional Certificate Capstone**, demonstrating real-world skills in file processing, data serialization, and API integration.

---

## Overview

The system is designed to automate the handling of customer feedback by:

1. Reading raw text review files from a local directory.
2. Parsing and structuring the feedback into Python dictionaries.
3. Sending the processed data to a remote web application via HTTP POST requests.

This simulates a backend data pipeline commonly used in production systems for customer insight collection.

---

## Features

* **Directory Traversal:** Uses Python’s `os` module to iterate through multiple feedback files.
* **Text Parsing:** Converts unstructured multi-line customer reviews into structured Python dictionaries.
* **API Integration:** Sends data to a remote Django-based web service using the `requests` library.
* **Automated Data Pipeline:** Fully hands-free workflow from file ingestion to data upload.

---

## Getting Started

### Prerequisites

* Python 3.x
* `requests` library

Install dependencies:

```bash id="k2n9qp"
pip install requests
```

---

## Installation

Clone the repository:

```bash id="a8v3ld"
git clone https://github.com/adeniranprecious002-ux/feed-back-automation.git
cd feed-back-automation
```

---

## Project Structure

```text id="x9q2mp"
.
├── script.py        # Main automation script
└── README.md
```

---

## Usage

Run the script:

```bash id="v4r8ks"
python3 script.py
```

---

## How It Works

1. The script scans a local directory for feedback text files.
2. Each file is read and parsed into structured fields (e.g., name, feedback text).
3. Data is converted into JSON-compatible dictionaries.
4. A POST request is sent to a REST API endpoint.
5. The server receives and stores the feedback for analysis.

---

## Learning Objectives

This project demonstrates:

* File handling in Python
* Data parsing and transformation
* Working with REST APIs
* Using the `requests` library
* Building automated data pipelines
* Real-world backend integration workflows

---

## Future Improvements

* Add retry logic for failed API requests
* Implement authentication (API keys or tokens)
* Add logging and monitoring
* Convert into a scheduled background service
* Extend support for CSV and JSON feedback formats

---

## Author

**Precious Adeniran**

Built as part of the **Google IT Automation with Python Professional Certificate Project**.
