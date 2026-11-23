SELECT
    session_id,
    MAX(user_id) AS user_id,
    DATEDIFF(
        MINUTE,
        MIN(event_timestamp),
        MAX(event_timestamp)
    ) AS session_duration_minutes,
    SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scroll_count
FROM app_events
GROUP BY session_id
HAVING
    -- Duration more than 30 minutes
    DATEDIFF(
        MINUTE,
        MIN(event_timestamp),
        MAX(event_timestamp)
    ) > 30

    -- At least 5 scroll events
    AND SUM(
        CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END
    ) >= 5

    -- Click-to-scroll ratio < 0.20
    AND CAST(
        SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END)
        AS DECIMAL(10, 4)
    )
    /
    SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END)
    < 0.20

    -- No purchases
    AND SUM(
        CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END
    ) = 0

ORDER BY
    scroll_count DESC,
    session_id ASC;
