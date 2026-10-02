WITH TopLearners AS (
    SELECT
        user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(*) >= 5
       AND AVG(course_rating) >= 4
),

OrderedCourses AS (
    SELECT
        c.user_id,
        c.course_name,
        LEAD(c.course_name) OVER (
            PARTITION BY c.user_id
            ORDER BY c.completion_date, c.course_id
        ) AS second_course
    FROM course_completions c
    JOIN TopLearners t
        ON c.user_id = t.user_id
),

CoursePairs AS (
    SELECT
        course_name AS first_course,
        second_course
    FROM OrderedCourses
    WHERE second_course IS NOT NULL
)

SELECT
    first_course,
    second_course,
    COUNT(*) AS transition_count
FROM CoursePairs
GROUP BY
    first_course,
    second_course
ORDER BY
    transition_count DESC,
    first_course ASC,
    second_course ASC;
