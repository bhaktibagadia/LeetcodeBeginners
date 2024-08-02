# Write your MySQL query statement below
select r.contest_id , round((count(distinct r.user_id)/count(distinct u.user_id)*100), 2) as percentage
from Users as u join Register as r
group by contest_id
order by percentage desc, r.contest_id;