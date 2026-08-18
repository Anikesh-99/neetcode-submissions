-- Write your query below
select c.customer_id, c.customer_name
from customers c 
where 'C' not in (Select product_name from orders where customer_id = c.customer_id) and 'B' in (Select product_name from orders where customer_id = c.customer_id) and 'A' in (Select product_name from orders where customer_id = c.customer_id) 
order by c.customer_name