# Write your MySQL query statement below
SELECT u.unique_id,n.name
From Employees n
LEFT JOIN EmployeeUNI u
ON n.id=u.id;
