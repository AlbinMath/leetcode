WITH ReactionCounts AS (
    SELECT
        user_id,
        reaction,
        COUNT(*) AS reaction_count
    FROM reactions
    GROUP BY user_id, reaction
),
UserStats AS (
    SELECT
        user_id,
        SUM(reaction_count) AS total_reactions,
        MAX(reaction_count) AS max_reaction_count
    FROM ReactionCounts
    GROUP BY user_id
),
DominantReaction AS (
    SELECT
        rc.user_id,
        rc.reaction,
        rc.reaction_count,
        ROW_NUMBER() OVER (
            PARTITION BY rc.user_id
            ORDER BY rc.reaction_count DESC, rc.reaction ASC
        ) AS rn
    FROM ReactionCounts rc
)
SELECT
    d.user_id,
    d.reaction AS dominant_reaction,
    ROUND(
        d.reaction_count / u.total_reactions,
        2
    ) AS reaction_ratio
FROM DominantReaction d
JOIN UserStats u
    ON d.user_id = u.user_id
WHERE d.rn = 1
  AND u.total_reactions >= 5
  AND d.reaction_count / u.total_reactions >= 0.60
ORDER BY
    reaction_ratio DESC,
    d.user_id ASC;
