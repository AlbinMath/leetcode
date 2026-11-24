WITH Daily AS (
    SELECT
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
Moving AS (
    SELECT
        visited_on,
        amount,
        SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS total_amount,
        COUNT(*) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS day_count
    FROM Daily
)
SELECT
    visited_on,
    total_amount AS amount,
    CAST(ROUND(1.0 * total_amount / day_count, 2) AS DECIMAL(10, 2)) AS average_amount
FROM Moving
WHERE day_count = 7
ORDER BY visited_on;
