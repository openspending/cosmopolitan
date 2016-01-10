# name of country and count of it's postal codes
# for Europe
select cities_country.name, count(cities_postalcode.id) as cnt
from cities_postalcode, cities_country
where cities_postalcode.country_id=cities_country.id
  and country_id in (select id from cities_country where continent = 'EU')
group by country_id, cities_country.name
order by cities_country.name;

# EU countries without postal codes
select cities_country.name
from cities_country
where id not in
(select distinct(cities_postalcode.country_id) from cities_postalcode)
and id in (select id from cities_country where continent = 'EU')
order by cities_country.name;
