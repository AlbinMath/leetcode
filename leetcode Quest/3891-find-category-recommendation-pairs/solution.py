import pandas as pd

def find_category_recommendation_pairs(
    product_purchases: pd.DataFrame,
    product_info: pd.DataFrame
) -> pd.DataFrame:

    # Add category to each purchase
    purchases = product_purchases.merge(
        product_info[["product_id", "category"]],
        on="product_id",
        how="left"
    )

    # Keep only unique user-category combinations
    user_categories = purchases[["user_id", "category"]].drop_duplicates()

    # Join the table with itself for users who bought both categories
    pairs = user_categories.merge(
        user_categories,
        on="user_id"
    )

    # Keep each category pair only once
    pairs = pairs[
        pairs["category_x"] < pairs["category_y"]
    ]

    # Count unique customers for each category pair
    result = (
        pairs.groupby(
            ["category_x", "category_y"]
        )["user_id"]
        .nunique()
        .reset_index(name="customer_count")
    )

    # At least 3 customers
    result = result[result["customer_count"] >= 3]

    # Rename columns
    result = result.rename(columns={
        "category_x": "category1",
        "category_y": "category2"
    })

    # Sort as required
    return result.sort_values(
        ["customer_count", "category1", "category2"],
        ascending=[False, True, True]
    ).reset_index(drop=True)
    
