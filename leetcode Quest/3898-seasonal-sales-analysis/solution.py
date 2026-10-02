import pandas as pd

def seasonal_sales_analysis(
    sales: pd.DataFrame,
    products: pd.DataFrame
) -> pd.DataFrame:

    # Merge sales with products
    df = sales.merge(products, on="product_id", how="left")

    # Convert date to datetime
    df["sale_date"] = pd.to_datetime(df["sale_date"])

    # Get month
    month = df["sale_date"].dt.month

    # Assign season
    df["season"] = "Fall"

    df.loc[month.isin([12, 1, 2]), "season"] = "Winter"
    df.loc[month.isin([3, 4, 5]), "season"] = "Spring"
    df.loc[month.isin([6, 7, 8]), "season"] = "Summer"

    # Calculate revenue
    df["revenue"] = df["quantity"] * df["price"]

    # Total quantity and revenue for each season/category
    grouped = (
        df.groupby(["season", "category"], as_index=False)
        .agg(
            total_quantity=("quantity", "sum"),
            total_revenue=("revenue", "sum")
        )
    )

    # Sort according to popularity rules
    grouped = grouped.sort_values(
        ["season", "total_quantity", "total_revenue", "category"],
        ascending=[True, False, False, True]
    )

    # Take the best category from each season
    result = grouped.groupby("season", as_index=False).first()

    # Required season order
    order = ["Fall", "Spring", "Summer", "Winter"]

    result["season"] = pd.Categorical(
        result["season"],
        categories=order,
        ordered=True
    )

    return result.sort_values("season").reset_index(drop=True)
