WITH DailyActivity AS (
    SELECT
        user_id,
        action_date,
        MIN(action) AS action
    FROM activity
    GROUP BY user_id, action_date
    HAVING COUNT(*) = 1
),
Grouped AS (
    SELECT
        user_id,
        action,
        action_date,
        DATEADD(
            DAY,
            -ROW_NUMBER() OVER (
                PARTITION BY user_id, action
                ORDER BY action_date
            ),
            action_date
        ) AS grp
    FROM DailyActivity
),
Streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM Grouped
    GROUP BY
        user_id,
        action,
        grp
),
Ranked AS (
    SELECT
        user_id,
        action,
        streak_length,
        start_date,
        end_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY streak_length DESC, start_date ASC
        ) AS rn
    FROM Streaks
    WHERE streak_length >= 5
)
SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM Ranked
WHERE rn = 1
ORDER BY
    streak_length DESC,
    user_id ASC;
