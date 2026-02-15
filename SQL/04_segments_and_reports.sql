-- Create a table to store the segment values based on RFM scores.
-- The segments are defined as follows:
-- Champions: Customers with the highest recency, frequency, and monetary scores (R=1, F=1, M=1).
-- Loyal: Customers with high recency and frequency scores but moderate monetary scores (R<=2, F<=2, M<=3).
-- New: Customers with high recency scores but low frequency and monetary scores (R<=2, F>=4, M>=4).
-- At Risk: Customers with low recency scores but high monetary scores (R>=4, M<=2).
-- Others: Customers who do not fit into the above segments.
Drop table if exists segment_values;
Create table segment_values as
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
rfm_score as (
select customer_id,
recency_date,
frequency,
monetary,
ntile(5) over (order by recency_date asc ) as r_score,
ntile(5) over (order by frequency desc  ) as f_score,
ntile(5) over (order by monetary desc ) as m_score
from customer_metric
),
segments as(
select customer_id,
r_score,
f_score,
m_score,
recency_date,
frequency,
monetary,
case
	when r_score = 1 and f_score =1 and m_score =1 then 'Champions'
	when r_score <=2 and f_score <= 2 and m_score <=3 then 'Loyal'
	when r_score <=2 and f_score >=4 and m_score >=4 then 'New'
	when r_score >= 4 and m_score <= 2 then 'At Risk'
	else 'others'
end as segment

from rfm_score)
select *
from segments

--2 query to view the 'At Risk' customers with high monetary value, ordered by recency score.
select * from segment_values
where segment = 'At Risk' and monetary > 3000
order by r_score asc; 