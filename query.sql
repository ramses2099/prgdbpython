
-- price,brand,model,year,title_status,mileage,color,vin,lot,state,country,condition

drop table cars;

create table if not exists cars(
id SERIAL primary key,
price 	INT, 
brand 	VARCHAR(150),
model 	VARCHAR(150),
"year" 	INT,
title_status 	VARCHAR(250),
mileage 	FLOAT,
color 	VARCHAR(150),
vin 	VARCHAR(150),
lot 	INT,
state  VARCHAR(250),
country 	VARCHAR(250),
"condition" VARCHAR(150)
);


select * from cars;


select
c.brand,
c.state,
count(*) total
from cars c
where "year" > 2000
group by brand, c.state
having count(*) > 2
order by 3 desc
