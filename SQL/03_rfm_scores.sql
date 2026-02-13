-- RFM (Recency, Frequency, Monetary) analysis is a marketing technique used to segment customers based on their purchasing behavior.
-- Recency: How recently a customer made a purchase.
-- Frequency: How often a customer makes a purchase.
-- Monetary: How much money a customer spends on purchases.
-- This SQL script calculates RFM scores for customers based on their transaction history and creates a new table to store these scores.

DROP TABLE IF EXISTS rfm_score;

with customer_summary as(
select customer_id,
max(invoice_date) as recent_date,
count(distinct invoice_no ) as frequency,
sum(revenue) as monetary
from transactions
WHERE customer_id IS NOT NULL
AND TRIM(customer_id) <> ''
group by customer_id
),
customer_metric as (
select customer_id,
recent_date,
date '2011-12-10' - date(recent_date) as recency_date,
frequency,
monetary 
from customer_summary
),
rfm_scores as (
select customer_id,
recency_date,
frequency,
monetary,
ntile(5) over (order by recency_date asc ) as r_score,
ntile(5) over (order by frequency desc  ) as f_score,
ntile(5) over (order by monetary desc ) as m_score
from customer_metric
)

CREATE TABLE rfm_score AS
SELECT *
FROM rfm_scores;

SELECT *
FROM rfm_score
ORDER BY r_score, f_score, m_score DESC
LIMIT 20;