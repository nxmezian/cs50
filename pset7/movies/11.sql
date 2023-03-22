SELECT *
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN ratings ON ratings.movie_id = movies.id
JOIN people ON stars.person_id = people.id
WHERE people.name="Helena Bonham Carter"
OR people.name="Johnny Depp"
ORDER BY rating DESC;