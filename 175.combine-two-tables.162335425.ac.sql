# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName,Address.City,Address.State
FROM Person
LEFT JOIN Address On Person.PersonId=Address.PersonId;
