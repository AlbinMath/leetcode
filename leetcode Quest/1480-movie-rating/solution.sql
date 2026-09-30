SELECT name AS results
FROM (
    SELECT TOP 1
        u.name
    FROM Users u
    JOIN MovieRating mr
        ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name ASC
) AS UserResult

UNION ALL

SELECT title AS results
FROM (
    SELECT TOP 1
        m.title
    FROM Movies m
    JOIN MovieRating mr
        ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01'
      AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(CAST(mr.rating AS FLOAT)) DESC, m.title ASC
) AS MovieResult;
