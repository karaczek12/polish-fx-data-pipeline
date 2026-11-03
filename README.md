# Polish FX Data Pipeline

A Python-based data engineering project that retrieves foreign exchange rates from the National Bank of Poland (NBP).

The long-term goal is to build an ETL pipeline that collects historical exchange rates, stores them in PostgreSQL, and supports financial reporting for a fictional Polish company.

**Project status:** In development — Milestone 1

## Business Problem

A company operating in Poland may receive invoices in foreign currencies such as EUR, USD and GBP.

To produce consistent financial reports in PLN, the company needs reliable historical exchange-rate information.

This project explores how to automate the collection, validation, storage and transformation of exchange-rate data.

## Technologies

- **Python** — API communication and data processing
- **Requests** — HTTP requests to the NBP API
- **Pytest** — automated testing
- **Git and GitHub** — source control and documentation

Planned additions include PostgreSQL, Docker and SQL-based reporting.

## Data Source

Exchange rates are obtained from the official [National Bank of Poland API](https://api.nbp.pl/en.html).

The project initially uses NBP Table A, which provides published average exchange rates for supported currencies.

## Getting Started

### Prerequisites

- Python 3.11 or newer
- Git

### Installation (Windows PowerShell)

Clone the repository:

```powershell
git clone https://github.com/YOUR_USERNAME/polish-fx-data-pipeline.git
cd polish-fx-data-pipeline
```

Create a Python virtual environment:

```powershell
py -3 -m venv .venv
```

Install the project and development dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

### Run the application

```powershell
.\.venv\Scripts\python.exe -m fx_pipeline
```

Once the NBP client is working, this command will retrieve and print the latest published EUR/PLN exchange rate.

## Testing

Run the tests using:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

The initial tests focus on extracting exchange-rate data from an API response and rejecting unsupported currencies.

## Project Roadmap

- [ ] Milestone 1 — Python foundation, API client and unit tests
- [ ] Milestone 2 — Historical exchange-rate ingestion and validation
- [ ] Milestone 3 — PostgreSQL integration and database design
- [ ] Milestone 4 — Invoice conversion and SQL analytics
- [ ] Milestone 5 — Automated checks, documentation and final portfolio presentation

## Current Limitations

This project is under development. It does not yet provide persistent storage, automatic scheduling or a complete reporting pipeline.

## What I Am Learning

Through this project, I am developing practical skills in:

- Python functions, modules, packages and type hints
- REST APIs, HTTP and JSON
- Automated testing and error handling
- ETL architecture and data modelling
- SQL and relational databases

The project builds on my commercial Java and Spring Boot development experience as I transition into data engineering.
