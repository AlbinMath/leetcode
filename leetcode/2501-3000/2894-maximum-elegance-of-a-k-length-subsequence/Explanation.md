# LeetCode 2813: Maximum Elegance of a K-Length Subsequence

**LeetCode Problem #2813 — Maximum Elegance of a K-Length Subsequence**
Solve LeetCode Maximum Elegance of a K-Length Subsequence using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Elegance of a K-Length Subsequence |
| LeetCode | #2813 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** 2D integer array `items` of length `n` and an integer `k`.

`items[i] = [profit_i, category_i]`, where `profit_i` and `category_i` denote the profit and category of the `i^th` item respectively.

Let's define the **elegance** of a **subsequence** of `items` as `total_profit + distinct_categories^2`, where `total_profit` is the sum of all profits in the subsequence, and `distinct_categories` is the number of **distinct** categories from all the categories in the selected subsequence.

Your task is to find the **maximum elegance** from all subsequences of size `k` in `items`.

Return *an integer denoting the maximum elegance of a subsequence of *`items`* with size exactly *`k`.

**Note:** A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.

## Constraints
- `1 <= items.length == n <= 10^5`
- `items[i].length == 2`
- `items[i][0] == profit_i`
- `items[i][1] == category_i`
- `1 <= profit_i <= 10^9`
- `1 <= category_i <= n `
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `items = [[3,2],[5,1],[10,1]], k = 2`
- **Output:** `17`
- **Explanation:** In this example, we have to select a subsequence of size 2.
We can select items[0] = [3,2] and items[2] = [10,1].
The total profit in this subsequence is 3 + 10 = 13, and the subsequence contains 2 distinct categories [2,1].
Hence, the elegance is 13 + 2^2 = 17, and we can show that it is the maximum achievable elegance.

### Example 2
- **Input:** `items = [[3,1],[3,1],[2,2],[5,3]], k = 3`
- **Output:** `19`
- **Explanation:** In this example, we have to select a subsequence of size 3. 
We can select items[0] = [3,1], items[2] = [2,2], and items[3] = [5,3]. 
The total profit in this subsequence is 3 + 2 + 5 = 10, and the subsequence contains 3 distinct categories [1,2,3]. 
Hence, the elegance is 10 + 3^2 = 19, and we can show that it is the maximum achievable elegance.

### Example 3
- **Input:** `items = [[1,1],[2,1],[3,1]], k = 3`
- **Output:** `7`
- **Explanation:** In this example, we have to select a subsequence of size 3. 
We should select all the items. 
The total profit will be 1 + 2 + 3 = 6, and the subsequence contains 1 distinct category [1]. 
Hence, the maximum elegance is 6 + 1^2 = 7.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Elegance of a K-Length Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `items = [[3,2],[5,1],[10,1]], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `17`.
4. **Verification:** In this example, we have to select a subsequence of size 2.
We can select items[0] = [3,2] and items[2] = [10,1].
The total profit in this subsequence is 3 + 10 = 13, and the subsequence contains 2 distinct categories [2,1].
Hence, the elegance is 13 + 2^2 = 17, and we can show that it is the maximum achievable elegance.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: x[0], reverse=True)
        
        total_profit = 0
        seen = set()
        dup_profits = []
        
        for i in range(k):
            profit, cat = items[i]
            total_profit += profit
            if cat not in seen:
                seen.add(cat)
            else:
                dup_profits.append(profit)
                
        max_elegance = total_profit + len(seen) ** 2
        
        for i in range(k, len(items)):
            if not dup_profits:
                break
            profit, cat = items[i]
            if cat not in seen:
                seen.add(cat)
                total_profit += profit - dup_profits.pop()
                max_elegance = max(max_elegance, total_profit + len(seen) ** 2)
                
        return max_elegance
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2501-3000/2552-maximum-sum-of-distinct-subarrays-with-length-k/)
- [2030. Smallest K-Length Subsequence With Occurrences of a Letter](../../2001-2500/2157-smallest-k-length-subsequence-with-occurrences-of-a-letter/)
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2204-find-subsequence-of-length-k-with-the-largest-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/)
