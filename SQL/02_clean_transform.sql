-- Add a new column 'revenue' to the transactions table
-- Calculate the revenue for each transaction by multiplying quantity and unit_price
ALTER TABLE transactions
ADD COLUMN IF NOT EXISTS revenue decimal(10,2);

UPDATE transactions
SET revenue = quantity * unit_price;

