# Web Scraper Backend

This is the backend for a web scraping application built with Flask.

## Table of Contents

- [Web Scraper Backend](#web-scraper-backend)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Configuration](#configuration)

## Introduction

This backend serves as the API for a web scraping application. It uses Flask to handle HTTP requests, and it includes endpoints for initiating web scraping and fetching the scraped data.

## Prerequisites

- Python 3.8+
- Pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:cbrit0/sons-back.git
   cd sons-back
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. The backend will be accessible at [http://localhost:5000](http://localhost:5000).

## API Endpoints

## Configuration

- Update the `pyproject.toml` file for Black code formatting configurations.
- Configure Flask-CORS in `app.py` for handling Cross-Origin Resource Sharing.
