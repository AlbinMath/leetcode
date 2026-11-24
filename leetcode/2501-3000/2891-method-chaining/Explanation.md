# LeetCode 2891: Method Chaining

**LeetCode Problem #2891 — Method Chaining**
Solve LeetCode Method Chaining using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Method Chaining |
| LeetCode | #2891 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
DataFrame `animals`
+-------------+--------+
| Column Name | Type |
+-------------+--------+
| name | object |
| species | object |
| age | int |
| weight | int |
+-------------+--------+

Write a solution to list the names of animals that weigh **strictly more than** `100` kilograms.

Return the animals sorted by weight in **descending order**.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `DataFrame animals:
+----------+---------+-----+--------+
| name | species | age | weight |
+----------+---------+-----+--------+
| Tatiana | Snake | 98 | 464 |
| Khaled | Giraffe | 50 | 41 |
| Alex | Leopard | 6 | 328 |
| Jonathan | Monkey | 45 | 463 |
| Stefan | Bear | 100 | 50 |
| Tommy | Panda | 26 | 349 |
+----------+---------+-----+--------+`
- **Output:** `+----------+
| name |
+----------+
| Tatiana |
| Jonathan |
| Tommy |
| Alex |
+----------+`
- **Explanation:** All animals weighing more than 100 should be included in the results table.
Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
The results should be sorted in descending order of weight. 

 
 In Pandas,

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Method Chaining**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `DataFrame animals:
+----------+---------+-----+--------+
| name | species | age | weight |
+----------+---------+-----+--------+
| Tatiana | Snake | 98 | 464 |
| Khaled | Giraffe | 50 | 41 |
| Alex | Leopard | 6 | 328 |
| Jonathan | Monkey | 45 | 463 |
| Stefan | Bear | 100 | 50 |
| Tommy | Panda | 26 | 349 |
+----------+---------+-----+--------+`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+----------+
| name |
+----------+
| Tatiana |
| Jonathan |
| Tommy |
| Alex |
+----------+`.
4. **Verification:** All animals weighing more than 100 should be included in the results table.
Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
The results should be sorted in descending order of weight. 

 
 In Pandas,

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values("weight", ascending=False)[["name"]]
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2726. Calculator with Method Chaining](../../2501-3000/2726-calculator-with-method-chaining/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [49. Group Anagrams](../../0001-0500/0049-group-anagrams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/method-chaining/)
