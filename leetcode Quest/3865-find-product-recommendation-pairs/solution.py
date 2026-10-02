import pandas as pd

def find_product_recommendation_pairs(
    product_purchases: pd.DataFrame,
    product_info: pd.DataFrame
) -> pd.DataFrame:

    # Join purchases with itself for the same user
    pairs = product_purchases.merge(
        product_purchases,
        on="user_id"
    )

    # Keep each pair only once
    pairs = pairs[
        pairs["product_id_x"] < pairs["product_id_y"]
    ]

    # Count customers for each product pair
    result = (
        pairs.groupby(
            ["product_id_x", "product_id_y"]
        )
        .size()
        .reset_index(name="customer_count")
    )

    # Keep pairs purchased by at least 3 customers
    result = result[result["customer_count"] >= 3]

    # Add product categories
    result = result.merge(
        product_info[["product_id", "category"]],
        left_on="product_id_x",
        right_on="product_id"
    ).rename(columns={
        "product_id_x": "product1_id",
        "category": "product1_category"
    }).drop(columns=["product_id"])

    result = result.merge(
        product_info[["product_id", "category"]],
        left_on="product_id_y",
        right_on="product_id"
    ).rename(columns={
        "product_id_y": "product2_id",
        "category": "product2_category"
    }).drop(columns=["product_id"])

    # Sort as required
    return result[
        [
            "product1_id",
            "product2_id",
            "product1_category",
            "product2_category",
            "customer_count"
        ]
    ].sort_values(
        ["customer_count", "product1_id", "product2_id"],
        ascending=[False, True, True]
    ).reset_index(drop=True)
