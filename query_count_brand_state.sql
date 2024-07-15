select
c.brand,
c.state,
count(*) total
from cars c
where "year" > 2000
group by brand, c.state
having count(*) > 2
order by 3 desc