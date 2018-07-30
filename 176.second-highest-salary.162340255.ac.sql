# Write your MySQL query statement below
select (select DISTINCT Salary
from Employee
order by Salary desc limit 1 offset 1) as SecondHighestSalary;
