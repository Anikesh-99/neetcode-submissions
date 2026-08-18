-- Write your query below
select DISTINCT c.name from customers c
except
select Distinct c.name from customers c join orders o ON c.id = o.customer_id
