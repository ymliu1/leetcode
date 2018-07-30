# Write your MySQL query statement below
select distinct P1.Email
from Person P1
inner join Person P2 on P1.email= P2.email
where P1.Id != P2.Id;
