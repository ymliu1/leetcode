# Write your MySQL query statement below

select distinct Request_at as Day , ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
from Trips
left join Users on Trips.Client_Id=Users.Users_Id
where Users.Banned='NO' and Request_at between '2013-10-01' and '2013-10-03'
group by Request_at;
