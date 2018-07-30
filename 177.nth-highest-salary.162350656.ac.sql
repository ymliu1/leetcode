CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select DISTINCT Salary
      from Employee
      order by Salary desc limit 1 offset N
  );
END

