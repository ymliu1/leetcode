# Write your MySQL query statement below
select Department.name as Department,e1.name as Employee,e1.salary as Salary
from Employee e1
right join (select max(e2.salary) as salary,e2.DepartmentId
          from Employee e2
          group by e2.DepartmentId) n
on e1.salary=n.salary and e1.DepartmentId=n.DepartmentId
join Department on e1.DepartmentId=Department.Id;


