# LeetCode 3521: Find Product Recommendation Pairs

**LeetCode Problem #3521 — Find Product Recommendation Pairs**
Solve LeetCode Find Product Recommendation Pairs using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Product Recommendation Pairs |
| LeetCode | #3521 |
| Difficulty | Medium |
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
(user_id, product_id) is the unique key for this table.
Each row represents a purchase of a product by a user in a specific quantity.

Table: `ProductInfo`

+-------------+---------+
| Column Name | Type | 
+-------------+---------+
| product_id | int |
| category | varchar |
| price | decimal |
+-------------+---------+
product_id is the primary key for this table.
Each row assigns a category and price to a product.

Amazon wants to implement the **Customers who bought this also bought...** feature based on **co-purchase patterns**. Write a solution to :

Identify **distinct** product pairs frequently **purchased together by the same customers** (where `product1_id` < `product2_id`) 
 For **each product pair**, determine how many customers purchased **both** products

**A product pair **is considered for recommendation **if** **at least** `3` **different** customers have purchased **both products**.

Return *the **result table ordered by **customer_count** in **descending** order, and in case of a tie, by *`product1_id`* in **ascending** order, and then by *`product2_id`* in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **Find Product Recommendation Pairs**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Product Recommendation Pairs**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

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
- [3554. Find Category Recommendation Pairs](../../3501-4000/3891-find-category-recommendation-pairs/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1963-find-xor-sum-of-all-pairs-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-product-recommendation-pairs/)
