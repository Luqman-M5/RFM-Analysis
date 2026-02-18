# RFM Analysis: Customer Segmentation with PostgreSQL and Python
This project performs Recency, Frequency, Monetary (RFM) analysis on transactional data to segment customers and understand their value and behaviour over time. It combines SQL data engineering in PostgreSQL (via DBeaver) with Python‑based visualisation, and is designed as a portfolio‑ready analytics project.

# 1. Project overview
**Objectives**

- Clean messy transactional CSVs and consolidate them into a customer‑level dataset.

- Compute RFM metrics (Recency, Frequency, Monetary) for each customer.

- Assign interpretable customer segments such as Champions, Loyal, At Risk, New, and Others.

- Build simple visualisations that answer clear business questions:
     - Which segments drive the most revenue?
     - Which segments have the highest average spend per customer?
     - How do recency and spend relate across segments?

**Tech stack**

- Database: PostgreSQL (queried via DBeaver)

- Language: Python

- Libraries: pandas, numpy, matplotlib

# 2. Data pipeline
Raw data
The starting point is one or more CSV files with transactional data, for example:
- Multiple rows per customer

- Transaction dates in mixed formats

- Separate columns for invoice/transaction ID, customer ID, and amount

SQL cleaning and RFM preparation (PostgreSQL + DBeaver)

All data cleaning and feature engineering are done in PostgreSQL, executed from DBeaver:

1. Import raw CSVs into staging tables.

2. Clean and standardise:

   - Fix and cast date columns.
   - Remove invalid or duplicate records where needed.
   - Standardise customer identifiers.

3. Aggregate to customer level:

   - Recency: days since last purchase at a chosen reference date.
   - Frequency: number of completed transactions per customer.
   - Monetary: total spend per customer.

4. Segment customers with RFM rules:

   - Use R, F, and M scores or thresholds in a CASE expression to label customers as Champions, Loyal, At Risk, New, Others, etc.

The final step is exporting a single, clean CSV:

- rfmdata.csv – one row per customer with at least:
  - customer_id
  - recency
  - frequency
  - monetary
  - segment

The SQL used for cleaning, aggregation, and segmentation is included in the SQL/ folder as reference. These scripts are written to run directly in PostgreSQL (for example via DBeaver), not from inside Python.

# 3. Repository structure
**Adjust names to match your actual files, but a typical layout is:**

├── SQL/

│   ├── 01_create_tables.sql

│   ├── 02_clean_transform.sql

│   └── 03_rfm_scores.sql

│   └── 04_segments_and_reports.sql

├── Python/

│   ├── 01_at_risk_high_value.py

│   ├── 02_revenue_by_segment.py

│   └── 03_avg_value_per_segment.py

│   └── 04_recency_vs_spend.py

├── Python/rfmdata.csv

├── requirements.txt

└── README.md


