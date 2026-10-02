SELECT
    customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING
    -- At least 3 purchases
    SUM(
        CASE
            WHEN transaction_type = 'purchase' THEN 1
            ELSE 0
        END
    ) >= 3

    -- Active for at least 30 days
    AND DATEDIFF(
        day,
        MIN(transaction_date),
        MAX(transaction_date)
    ) >= 30

    -- Refund rate < 20%
    AND
    CAST(
        SUM(
            CASE
                WHEN transaction_type = 'refund' THEN 1
                ELSE 0
            END
        ) AS DECIMAL(10, 4)
    )
    / COUNT(*) < 0.20

ORDER BY
    customer_id ASC;
