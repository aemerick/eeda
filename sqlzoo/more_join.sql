

-- 1
-- List the films where yr is 1962 [id, title]
SELECT id, title
 FROM movie
 WHERE yr=1962;

 -- 2
 -- Give year of 'Citizen Kane'.
 SELECT yr FROM movie
     WHERE movie.title = 'Citizen Kane';

-- 3
-- List all of the Star Trek movies, include the id, title and yr
--  (all of these movies include the words Star Trek in the title).
--   Order results by year.
SELECT id, title, yr FROM movie
    WHERE title LIKE '%Star Trek%'
    ORDER BY yr ASC;

-- 4
-- What id number does the actor 'Glenn Close' have?
SELECT actor.id FROM actor
    WHERE actor.name = 'Glenn Close';

-- 5
-- WHat is the id of the film 'Casablanca'?
SELECT id FROM movie
    WHERE movie.title = 'Casablanca';

-- 6
-- Obtain the cast list for 'Casablanca'.
-- what is a cast list?
--   The cast list is the names of the actors who were in the movie.
-- Use movieid=11768, (or whatever value you got from the previous question)
SELECT actor.name FROM actor
    JOIN casting ON actor.id = casting.actorid
    WHERE casting.movieid =
        (SELECT id FROM movie
            WHERE movie.title = 'Casablanca')l


-- 7
-- Obtain the cast list for the film 'Alien'
SELECT actor.name FROM actor
    JOIN casting ON actor.id = casting.actorid
    WHERE casting.movieid = ( SELECT movie.id
                              FROM movie
                              WHERE movie.title = 'Alien');

-- 8
-- List the films where Harrison Ford appeared
SELECT movie.title FROM movie
    JOIN casting ON casting.movieid = movie.id
    WHERE casting.actorid =
          (SELECT actor.id FROM actor WHERE actor.name = 'Harrison Ford');

-- 9
-- List the films where 'Harrison Ford' has appeared - but not in the starring
--  role. [Note: the ord field of casting gives the position of the actor.
--  If ord=1 then this actor is in the starring role]
SELECT movie.title FROM movie
    JOIN casting ON casting.movieid = movie.id
    WHERE casting.actorid = (SELECT actor.id FROM actor
                                WHERE actor.name = 'Harrison Ford')
        AND casting.ord > 1;

-- 10
-- List the films together with the leading astart for all 1962 films.
SELECT movie.title, actor.name FROM casting
    JOIN movie ON movie.id = casting.movieid
    JOIN actor ON actor.id = casting.actorid
    WHERE movie.yr = 1962
          AND casting.ord = 1;

-- 11
-- Which were the busiest years for 'Rock Hudson', show the year and the number
--  of movies he made each year for any year in which he made more than 2 movies.
SELECT movie.yr, COUNT(movie.yr) AS cnt FROM casting
  JOIN actor ON actor.id = casting.actorid
  JOIN movie ON movie.id = casting.movieid
  WHERE actor.name = 'Rock Hudson'
  GROUP BY movie.yr
  HAVING cnt > 2;

-- 12
-- List the film title and the leading actor for all of the films 'Julie Andrews'
-- played in. Did you get "Little Miss Marker twice"?
SELECT x.title, actor.name FROM casting
JOIN
    ( SELECT casting.movieid as mid, movie.title as title FROM casting
         JOIN actor ON casting.actorid = actor.id
         JOIN movie ON casting.movieid = movie.id
         WHERE actor.name = 'Julie Andrews') AS x
   ON casting.movieid = x.mid
JOIN actor ON casting.actorid = actor.id
   WHERE casting.ord = 1;

-- 13
-- Obtain a list, in alphabetical order, of actors who've had at least 15 starring roles.
SELECT actor.name FROM actor
JOIN ( SELECT casting.actorid as actorid,
         COUNT(*) as cnt FROM casting
      WHERE casting.ord = 1
      GROUP BY casting.actorid
      HAVING cnt >= 15) as x
      ON x.actorid = actor.id
      ORDER BY actor.name;

-- 14
-- List the films released in the year 1978 ordered by the number of
-- actors in the cast, then by title.
SELECT movie.title, COUNT(casting.actorid) as cnt FROM casting
    JOIN movie on casting.movieid = movie.id
    WHERE movie.yr = 1978
    GROUP BY movie.title
    ORDER BY cnt DESC, movie.title;

-- 15
-- List all the people who have worked with 'Art Garfunkel'.
--  AE NOTE: This does give the right answer but didn't make the usual
--           smiley face... not sure whats going on...
SELECT DISTINCT(actor.name) FROM casting
JOIN actor ON casting.actorid = actor.id
JOIN movie ON casting.movieid = movie.id
WHERE movie.id IN (SELECT casting.movieid as mid FROM casting
                   JOIN actor on casting.actorid = actor.id
                   JOIN movie ON casting.movieid = movie.id
                   WHERE actor.name = 'Art Garfunkel');
