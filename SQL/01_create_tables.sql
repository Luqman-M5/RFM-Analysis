--Create the transactions table to store sales data 
-- data downloaded from kaggle: https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset
CREATE TABLE transactions (
    invoice_no   VARCHAR(20),
    stock_code   VARCHAR(20),
    description  TEXT,
    quantity     INT,
    invoice_date TIMESTAMP,
    unit_price   NUMERIC(10,2),
    customer_id  VARCHAR(20),
    country      VARCHAR(50),
    revenue      NUMERIC(10,2)
);

CREATE INDEX idx_transactions_customer ON transactions(customer_id);
CREATE INDEX idx_transactions_date ON transactions(invoice_date);
