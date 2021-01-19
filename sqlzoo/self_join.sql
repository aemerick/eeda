SELECT count(*) FROM stops;

SELECT id FROM stops where name LIKE 'Craiglockhart';

SELECT id, name FROM stops
    JOIN route ON stops.id = route.stop
    WHERE route.num LIKE '4' AND route.company LIKE 'LRT';

SELECT company, num, COUNT(*) AS x
FROM route WHERE stop=149 OR stop=53
GROUP BY company, num
HAVING x = 2;


SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop = (SELECT stops.id FROM stops WHERE
                stops.name = 'Craiglockhart') AND
      b.stop = (SELECT stops.id FROM stops WHERE
                stops.name = 'London Road');


SELECT a.company, a.num, stopa.name, stopb.name
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart'
   AND stopb.name='London Road';

SELECT DISTINCT a.company, a.num
FROM route AS a JOIN route AS b
    ON (a.num = b.num AND a.company=b.company)
    WHERE a.stop = (SELECT id from stops WHERE name LIKE 'Haymarket')
    AND   b.stop = (SELECT id from stops WHERE name LIKE 'Leith');

/* 8
*/
SELECT a.company, a.num
    FROM route AS a JOIN route AS b
    ON (a.num = b.num AND a.company = b.company)
    WHERE a.stop = (SELECT id FROM stops WHERE name LIKE 'Craiglockhart')
    AND b.stop = (SELECT id from stops WHERE name LIKE 'Tollcross');

/* 9
Give a distinct list of the stops which may be reached from 'Craiglockhart' by taking one bus, including 'Craiglockhart' itself, offered by the LRT company. Include the company and bus no. of the relevant services.
*/
SELECT DISTINCT stopb.name, b.company, b.num
FROM route a
  JOIN route b ON (a.num=b.num AND a.company=b.company)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
  WHERE a.company LIKE 'LRT' AND
      stopa.name = 'Craiglockhart';

/* 10 */
