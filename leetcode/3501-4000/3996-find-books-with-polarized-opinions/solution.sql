WITH book_stats AS (
    SELECT
        rs.book_id,
        COUNT(*) AS total_sessions,
        MAX(rs.session_rating) AS highest_rating,
        MIN(rs.session_rating) AS lowest_rating,

        SUM(
            CASE
                WHEN rs.session_rating >= 4
                  OR rs.session_rating <= 2
                THEN 1
                ELSE 0
            END
        ) AS extreme_ratings,

        SUM(
            CASE
                WHEN rs.session_rating >= 4
                THEN 1
                ELSE 0
            END
        ) AS high_ratings,

        SUM(
            CASE
                WHEN rs.session_rating <= 2
                THEN 1
                ELSE 0
            END
        ) AS low_ratings

    FROM reading_sessions rs
    GROUP BY rs.book_id
)

SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages,

    bs.highest_rating - bs.lowest_rating AS rating_spread,

    ROUND(
        CAST(bs.extreme_ratings AS DECIMAL(10, 2))
        / bs.total_sessions,
        2
    ) AS polarization_score

FROM books b
JOIN book_stats bs
    ON b.book_id = bs.book_id

WHERE bs.total_sessions >= 5
  AND bs.high_ratings >= 1
  AND bs.low_ratings >= 1
  AND (
        CAST(bs.extreme_ratings AS DECIMAL(10, 2))
        / bs.total_sessions
      ) >= 0.6

ORDER BY
    polarization_score DESC,
    b.title DESC;
