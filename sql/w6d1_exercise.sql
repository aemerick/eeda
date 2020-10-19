-- Question 1 : ranking

-- this might work on sql server
SELECT id, score
       RANK() OVER(PARTITION BY id ORDER BY score ASC) Rank
FROM table
ORDER BY Rank;

-- from stack overflow

--
SELECT Scores.score, COUNT(t.score) AS rnk FROM
   (SELECT DISTINCT score from Scores) AS t, Scores
   WHERE Scores.score <= t.score
   GROUP BY Scores.Id, Scores.score
   ORDER BY Scores.score DESC;


-- Question 2:

-- events created per day for the last 30 days?
SELECT DATE_TRUNC('day',dates) as day,
       COUNT(event_id)
  FROM events_creation
  WHERE day < DATE_TRUNC('day',GETDATE())
  GROUP BY day

-- drop off rate (% of events started )
SELECT (x.val / y.val)
FROM
(
  SELECT COUNT(action) FROM events_creation
    WHERE action = 'cancel_event'
) AS x
JOIN
(
  SELECT COUNT(action) FROM events_creation
  WHERE action = 'start_creation_event'
) AS y
ON 1 = 1;

-- avergae time in days from event creation
-- to cancellation

SELECT AVG((x.val - y.val) / (24*3600))
FROM
(
  SELECT timestamp, event_id FROM events_creation
    WHERE action = 'start_creation_event'
) AS x
JOIN
(
  SELECT timestamp, event_id FROM events_creation
  WHERE action = 'cancel_event'
) AS y
ON x.event_id = y.event_id;

SELECT (y.amount - x.amount)
FROM
( SELECT SUM(AMOUNT), sender FROM transactions
   GROUP BY sender ) AS x
JOIN
( SELECT SUM(AMOUNT), receiver FROM transactions
   GROUP BY receiver) AS y
ON x.sender = y.receiver;


-------------------------- Question 3 --------------------------

SELECT (y.amount - x.amount)
FROM
( SELECT SUM(AMOUNT), sender FROM transactions
   GROUP BY day, sender ) AS x
JOIN
( SELECT SUM(AMOUNT), receiver FROM transactions
   GROUP BY day, receiver) AS y
ON x.sender = y.receiver;

-- level up?
SELECT (y.amount - x.amount)
FROM
( SELECT DATE_TRUNC('day',date) as day, SUM(AMOUNT), sender FROM transactions
   GROUP BY day, sender ) AS x
JOIN
( SELECT DATE_TRUNC('day',date) as day, SUM(AMOUNT), receiver FROM transactions
   GROUP BY day, receiver) AS y
ON x.sender = y.receiver;
