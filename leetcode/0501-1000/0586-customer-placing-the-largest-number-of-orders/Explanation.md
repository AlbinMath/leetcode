# LeetCode 586: Customer Placing the Largest Number of Orders

**LeetCode Problem #586 — Customer Placing the Largest Number of Orders**
Solve LeetCode Customer Placing the Largest Number of Orders using SQL and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Window Function in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Customer Placing the Largest Number of Orders |
| LeetCode | #586 |
| Difficulty | Easy |
| Language | SQL |
| Algorithm | SQL Query / Relational Join & Window Function |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Orders`

+-----------------+----------+
| Column Name | Type |
+-----------------+----------+
| order_number | int |
| customer_number | int |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.

Write a solution to find the `customer_number` for the customer who has placed **the largest number of orders**.

The test cases are generated so that **exactly one customer** will have placed more orders than any other customer.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 3 |
+--------------+-----------------+`
- **Output:** `+-----------------+
| customer_number |
+-----------------+
| 3 |
+-----------------+`
- **Explanation:** The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We solve **Customer Placing the Largest Number of Orders** by formulating an SQL query that applies relational algebra and SQL aggregation clauses. We group records using `GROUP BY` and compute metrics with aggregate functions. We order the final result set using `ORDER BY`.

## Algorithm
1. Group records and calculate aggregated summary metrics.
2. Sort the projected result.
3. Project and return the requested output columns.

## Example Walkthrough
1. **Input State:** We begin with `Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 3 |
+--------------+-----------------+`.
2. **Processing Steps:** We apply **SQL Query / Relational Join & Window Function** using our **Relational Table**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+-----------------+
| customer_number |
+-----------------+
| 3 |
+-----------------+`.
4. **Verification:** The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Relational Table.

## Pattern
**Database / SQL**

## Topics
- Database
- SQL
- Data Aggregation

## Language
SQL

## Source Code
- [solution.sql](./solution.sql)


```sql
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```

## Why This Works
By utilizing **Database / SQL**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1801. Number of Orders in the Backlog](../../1501-2000/1928-number-of-orders-in-the-backlog/)
- [179. Largest Number](../../0001-0500/0179-largest-number/)
- [747. Largest Number At Least Twice of Others](../../0501-1000/0748-largest-number-at-least-twice-of-others/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/)
