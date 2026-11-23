# LeetCode 3564: Seasonal Sales Analysis

**LeetCode Problem #3564 — Seasonal Sales Analysis**
Solve LeetCode Seasonal Sales Analysis using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Seasonal Sales Analysis |
| LeetCode | #3564 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `sales`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| sale_id | int |
| product_id | int |
| sale_date | date |
| quantity | int |
| price | decimal |
+---------------+---------+
sale_id is the unique identifier for this table.
Each row contains information about a product sale including the product_id, date of sale, quantity sold, and price per unit.

Table: `products`

+---------------+---------+
| Column Name | Type |
+---------------+---------+
| product_id | int |
| product_name | varchar |
| category | varchar |
+---------------+---------+
product_id is the unique identifier for this table.
Each row contains information about a product including its name and category.

Write a solution to find the most popular product category for each season. The seasons are defined as:

**Winter**: December, January, February 
 **Spring**: March, April, May 
 **Summer**: June, July, August 
 **Fall**: September, October, November

The **popularity** of a **category** is determined by the **total quantity sold** in that **season**. If there is a **tie**, select the category with the highest **total revenue** (`quantity &times; price`). If there is still a tie, return the lexicographically smaller category.

Return *the result table ordered by season in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Seasonal Sales Analysis**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Seasonal Sales Analysis**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **In-Place Array Traversal & Index Mapping** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1068. Product Sales Analysis I](../../1001-1500/1153-product-sales-analysis-i/)
- [1070. Product Sales Analysis III](../../1001-1500/1155-product-sales-analysis-iii/)
- [1084. Sales Analysis III](../../1001-1500/1174-sales-analysis-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/seasonal-sales-analysis/)
