# Write your MySQL query statement below
select d1.name as Department,e1.name as Employee ,e1.salary as Salary
from Department d1,Employee e1
where e1.DepartmentId=d1.Id
and 3>(select count(distinct e2.salary) FROM Employee e2
       WHERE e1.DepartmentId=e2.DepartmentId AND e1.salary<e2.salary)
       ORDER BY d1.Name,e1.salary DESC;
