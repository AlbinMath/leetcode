# LeetCode 3554: Find Category Recommendation Pairs

**LeetCode Problem #3554 — Find Category Recommendation Pairs**
Solve LeetCode Find Category Recommendation Pairs using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Category Recommendation Pairs |
| LeetCode | #3554 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `ProductPurchases`

+-------------+------+
| Column Name | Type | 
+-------------+------+
| user_id | int |
| product_id | int |
| quantity | int |
+-------------+------+
(user_id, product_id) is the unique identifier for this table. 
Each row represents a purchase of a product by a user in a specific quantity.

Table: `ProductInfo`

+-------------+---------+
| Column Name | Type | 
+-------------+---------+
| product_id | int |
| category | varchar |
| price | decimal |
+-------------+---------+
product_id is the unique identifier for this table.
Each row assigns a category and price to a product.

Amazon wants to understand shopping patterns across product categories. Write a solution to:

Find all **category pairs** (where `category1` < `category2`) 
 For **each category pair**, determine the number of **unique** **customers** who purchased products from **both** categories

A category pair is considered **reportable** if at least `3` different customers have purchased products from both categories.

Return *the result table of reportable category pairs ordered by **customer_count** in **descending** order, and in case of a tie, by **category1** in **ascending** order lexicographically, and then by **category2** in **ascending** order.*

The result format is in the following example.

## Examples
Consider the standard input for **Find Category Recommendation Pairs**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Category Recommendation Pairs**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Two Pointer Convergence & Scanning** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3521. Find Product Recommendation Pairs](../../3501-4000/3521-find-product-recommendation-pairs/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1835-find-xor-sum-of-all-pairs-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-category-recommendation-pairs/)
