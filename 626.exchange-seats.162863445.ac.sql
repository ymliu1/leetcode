# Write your MySQL query statement below
select id,
       case 
       when id=(select count(*) from seat) and id%2=1 then student
       when id%2=1 then (select s1.student from seat s1 where s1.id=s.id+1)
       when id%2=0 then (select s1.student from seat s1 where s1.id=s.id-1)
       end as student
from seat as s;

