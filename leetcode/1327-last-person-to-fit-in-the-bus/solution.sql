SELECT person_name
FROM (
    SELECT
        person_name,
        total_weight,
        ROW_NUMBER() OVER (ORDER BY total_weight DESC) AS rn
    FROM (
        SELECT
            person_name,
            SUM(weight) OVER (ORDER BY turn) AS total_weight
        FROM Queue
    )
    WHERE total_weight <= 1000
)
WHERE rn = 1;
