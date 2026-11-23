WITH ordered AS (
    SELECT
        ss.*,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY session_date, session_id
        ) AS rn,
        LAG(session_date) OVER (
            PARTITION BY student_id
            ORDER BY session_date, session_id
        ) AS prev_date
    FROM study_sessions ss
),

grouped AS (
    SELECT
        *,
        SUM(
            CASE
                WHEN prev_date IS NULL
                     OR DATEDIFF(day, prev_date, session_date) > 2
                THEN 1
                ELSE 0
            END
        ) OVER (
            PARTITION BY student_id
            ORDER BY rn
            ROWS UNBOUNDED PRECEDING
        ) AS grp
    FROM ordered
),

sequence_info AS (
    SELECT
        student_id,
        grp,
        COUNT(*) AS session_count,
        COUNT(DISTINCT subject) AS subject_count,
        SUM(hours_studied) AS total_hours
    FROM grouped
    GROUP BY student_id, grp
    HAVING COUNT(*) >= 6
       AND COUNT(DISTINCT subject) >= 3
),

numbers AS (
    SELECT 3 AS n
    UNION ALL SELECT 4
    UNION ALL SELECT 5
    UNION ALL SELECT 6
    UNION ALL SELECT 7
    UNION ALL SELECT 8
    UNION ALL SELECT 9
    UNION ALL SELECT 10
    UNION ALL SELECT 11
    UNION ALL SELECT 12
    UNION ALL SELECT 13
    UNION ALL SELECT 14
    UNION ALL SELECT 15
    UNION ALL SELECT 16
    UNION ALL SELECT 17
    UNION ALL SELECT 18
    UNION ALL SELECT 19
    UNION ALL SELECT 20
),

candidates AS (
    SELECT
        si.student_id,
        si.grp,
        si.session_count,
        si.total_hours,
        n.n AS cycle_length
    FROM sequence_info si
    JOIN numbers n
        ON n.n >= 3
       AND n.n <= si.session_count / 2
       AND si.session_count % n.n = 0
),

pattern_validation AS (
    SELECT
        c.student_id,
        c.grp,
        c.cycle_length,
        c.total_hours,

        COUNT(DISTINCT
            CASE
                WHEN g.rn <= c.cycle_length
                THEN g.subject
            END
        ) AS first_cycle_subjects,

        COUNT(*) AS total_sessions,

        COUNT(DISTINCT
            CONCAT(
                (g.rn - 1) % c.cycle_length,
                '|',
                g.subject
            )
        ) AS unique_positions

    FROM candidates c
    JOIN grouped g
        ON g.student_id = c.student_id
       AND g.grp = c.grp

    GROUP BY
        c.student_id,
        c.grp,
        c.cycle_length,
        c.total_hours
),

valid_patterns AS (
    SELECT
        student_id,
        grp,
        cycle_length,
        total_hours
    FROM pattern_validation
    WHERE first_cycle_subjects = cycle_length
      AND unique_positions = cycle_length
)

SELECT
    s.student_id,
    s.student_name,
    s.major,
    vp.cycle_length,
    vp.total_hours AS total_study_hours
FROM valid_patterns vp
JOIN students s
    ON s.student_id = vp.student_id
ORDER BY
    vp.cycle_length DESC,
    vp.total_hours DESC;
