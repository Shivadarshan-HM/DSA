# Write your MySQL query statement below
SELECT p.product_name, y.year, y.price
From Sales y
INNER JOIN Product p
ON y.product_id=p.product_id

