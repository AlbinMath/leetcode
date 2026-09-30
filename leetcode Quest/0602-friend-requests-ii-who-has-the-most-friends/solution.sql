WITH Friends AS (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
),
FriendCount AS (
    SELECT 
        id,
        COUNT(*) AS num
    FROM Friends
    GROUP BY id
)
SELECT TOP 1
    id,
    num
FROM FriendCount
ORDER BY num DESC;
