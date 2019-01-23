SELECT A.name AS "Actors that were in at least 2 movies"
FROM Actors A
INNER JOIN ActorsMovies AM ON A.actor_id = AM.actor_id
INNER JOIN Movies M ON M.movie_id = AM.movie_id
GROUP BY A.name HAVING COUNT(*)>1

SELECT G.name AS "Genre that have more than one movie"
FROM Genres G
INNER JOIN GenresMovies GM ON G.genre_id = GM.genre_id
INNER JOIN Movies M ON M.movie_id = GM.movie_id
GROUP BY G.name HAVING COUNT(*)>1

SELECT D.name AS "Directors that have more than one movie"
FROM Directors D
INNER JOIN DirectorsMovies DM ON D.director_id = DM.director_id
INNER JOIN Movies M ON M.movie_id = DM.movie_id
GROUP BY D.name HAVING COUNT(*)>1

SELECT M.title AS "Movies that are newer than 2015"
FROM Movies M
WHERE M.year > 2015

SELECT M.title AS "Movies that are older than 2015"
FROM Movies M
WHERE M.year < 2015

SELECT M.title AS "Movies that are from 2015"
FROM Movies M
WHERE M.year = 2015

SELECT DISTINCT(M.title) AS "Which movies are rented"
FROM Movies M
INNER JOIN DVDMovie DM ON DM.movie_id = M.movie_id
INNER JOIN Rents R on R.dvd_id = DM.dvd_id

SELECT DISTINCT(M.title) AS "Which DVD are available"
FROM Movies M
INNER JOIN DVDMovie DM ON DM.movie_id = M.movie_id
INNER JOIN Rents R on R.dvd_id != DM.dvd_id

SELECT DISTINCT(G.name) AS "Genre",  D.name AS "Director"
FROM Directors D
INNER JOIN DirectorsMovies DM on DM.director_id = D.director_id
INNER JOIN Movies M on M.movie_id = DM.movie_id
INNER JOIN GenresMovies GM on M.movie_id = GM.movie_id
INNER JOIN Genres G on G.genre_id = GM.genre_id
ORDER BY (D.name)

SELECT DISTINCT(G.name) AS "Genre",  A.name AS "Actors"
FROM Actors A
INNER JOIN ActorsMovies AM on AM.actor_id = A.actor_id
INNER JOIN Movies M on M.movie_id = AM.movie_id
INNER JOIN GenresMovies GM on M.movie_id = GM.movie_id
INNER JOIN Genres G on G.genre_id = GM.genre_id
ORDER BY (A.name)
 
SELECT E.name AS "Employee Girls"
FROM Employees E
WHERE E.cnp > 2000000000000

SELECT E.name AS "Employee Man"
FROM Employees E
WHERE E.cnp < 2000000000000
