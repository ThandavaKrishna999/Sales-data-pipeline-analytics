# TOTAL REVENUE

SELECT ROUND(SUM(sales),2) as total_revenue from sales;

# SALES by category
select p.category, round(sum(s.sales),2) as total_sales from sales s
join products p on 
s.product_id = p.product_id
group by p.category;

# sales by region

select c.region, round(sum(s.sales),2) as total_sales from sales s
join orders o 
on s.order_id = o.order_id
join customers c
on o.customer_id = c.customer_id
group by c.region;

# Monthly trend

select 
DATE_FORMAT(o.order_date, '%Y-%m') as month,
round(sum(s.sales),2) as revenue
from sales s 
join orders o 
on s.order_id = o.order_id
group by DATE_FORMAT(o.order_date, '%Y-%m')
order by DATE_FORMAT(o.order_date, '%Y-%m');

# Profit by category
SELECT 
    p.category,
    ROUND(SUM(s.profit), 2) AS total_profit
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category;
# Create VIEW

CREATE OR REPLACE VIEW sales_summary AS
SELECT 
    o.order_date,
    DATE_FORMAT(o.order_date, '%Y-%m') AS order_month,
    c.region,
    p.category,
    p.sub_category,
    s.sales,
    s.quantity,
    s.discount,
    s.profit
FROM sales s
JOIN orders o ON s.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id;