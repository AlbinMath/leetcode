WITH ranked_inventory AS (
    SELECT
        i.*,
        COUNT(*) OVER (
            PARTITION BY i.store_id
        ) AS product_count,

        ROW_NUMBER() OVER (
            PARTITION BY i.store_id
            ORDER BY i.price DESC, i.inventory_id
        ) AS expensive_rank,

        ROW_NUMBER() OVER (
            PARTITION BY i.store_id
            ORDER BY i.price ASC, i.inventory_id
        ) AS cheap_rank
    FROM inventory i
),

store_data AS (
    SELECT
        store_id,

        MAX(CASE
            WHEN expensive_rank = 1
            THEN product_name
        END) AS most_exp_product,

        MAX(CASE
            WHEN expensive_rank = 1
            THEN quantity
        END) AS expensive_quantity,

        MAX(CASE
            WHEN cheap_rank = 1
            THEN product_name
        END) AS cheapest_product,

        MAX(CASE
            WHEN cheap_rank = 1
            THEN quantity
        END) AS cheapest_quantity,

        MAX(product_count) AS product_count
    FROM ranked_inventory
    GROUP BY store_id
)

SELECT
    s.store_id,
    s.store_name,
    s.location,
    sd.most_exp_product,
    sd.cheapest_product,
    ROUND(
        CAST(sd.cheapest_quantity AS DECIMAL(10, 2))
        / sd.expensive_quantity,
        2
    ) AS imbalance_ratio
FROM store_data sd
JOIN stores s
    ON s.store_id = sd.store_id
WHERE sd.product_count >= 3
  AND sd.expensive_quantity < sd.cheapest_quantity
ORDER BY
    imbalance_ratio DESC,
    s.store_name ASC;
