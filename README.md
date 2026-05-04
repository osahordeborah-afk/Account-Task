# Accountant Automation System

A Python-based automation tool for handling basic accounting operations, including petty cash tracking, invoice reconciliation, budget variance analysis, and year-end financial reporting.

## Features

- Track petty cash requests
- Calculate cash request turnaround time
- Reconcile invoices with purchase orders
- Detect invoice exceptions
- Perform budget variance analysis
- Generate year-end financial summaries
- Export accounting reports as CSV files

## Role Context

This project automates key accounting responsibilities such as:

- IRS-sponsored VITA tax support documentation
- Petty cash administration
- GAAP-aligned financial tracking
- Invoice and purchase order reconciliation
- Budget analysis
- Audit documentation support
- Year-end financial reporting

## Technologies Used

- Python
- Pandas
- CSV file handling
- Datetime processing

## Project Structure

```text
graduate-accountant-automation/
│
├── main.py
├── petty_cash.csv
├── invoices.csv
├── purchase_orders.csv
├── budget.csv
│
├── petty_cash_summary.csv
├── invoice_reconciliation_report.csv
├── invoice_exceptions.csv
├── budget_variance_report.csv
├── year_end_financial_summary.csv
│
└── README.md
