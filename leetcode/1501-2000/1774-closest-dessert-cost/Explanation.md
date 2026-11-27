# LeetCode 1774: Closest Dessert Cost

**LeetCode Problem #1774 — Closest Dessert Cost**
Solve LeetCode Closest Dessert Cost using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Closest Dessert Cost |
| LeetCode | #1774 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You would like to make dessert and are preparing to buy the ingredients. You have `n` ice cream base flavors and `m` types of toppings to choose from. You must follow these rules when making your dessert:

There must be **exactly one** ice cream base. 
 You can add **one or more** types of topping or have no toppings at all. 
 There are **at most two** of **each type** of topping.

You are given three inputs:

`baseCosts`, an integer array of length `n`, where each `baseCosts[i]` represents the price of the `i^th` ice cream base flavor. 
 `toppingCosts`, an integer array of length `m`, where each `toppingCosts[i]` is the price of **one** of the `i^th` topping. 
 `target`, an integer representing your target price for dessert.

You want to make a dessert with a total cost as close to `target` as possible.

Return *the closest possible cost of the dessert to *`target`. If there are multiple, return *the **lower** one.*

## Constraints
- `n == baseCosts.length`
- `m == toppingCosts.length`
- `1 <= n, m <= 10`
- `1 <= baseCosts[i], toppingCosts[i] <= 10^4`
- `1 <= target <= 10^4`

## Examples
### Example 1
- **Input:** `baseCosts = [1,7], toppingCosts = [3,4], target = 10`
- **Output:** `10`
- **Explanation:** Consider the following combination (all 0-indexed):
- Choose base 1: cost 7
- Take 1 of topping 0: cost 1 x 3 = 3
- Take 0 of topping 1: cost 0 x 4 = 0
Total: 7 + 3 + 0 = 10.

### Example 2
- **Input:** `baseCosts = [2,3], toppingCosts = [4,5,100], target = 18`
- **Output:** `17`
- **Explanation:** Consider the following combination (all 0-indexed):
- Choose base 1: cost 3
- Take 1 of topping 0: cost 1 x 4 = 4
- Take 2 of topping 1: cost 2 x 5 = 10
- Take 0 of topping 2: cost 0 x 100 = 0
Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.

### Example 3
- **Input:** `baseCosts = [3,10], toppingCosts = [2,5], target = 9`
- **Output:** `8`
- **Explanation:** It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Closest Dessert Cost**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `baseCosts = [1,7], toppingCosts = [3,4], target = 10`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** Consider the following combination (all 0-indexed):
- Choose base 1: cost 7
- Take 1 of topping 0: cost 1 x 3 = 3
- Take 0 of topping 1: cost 0 x 4 = 0
Total: 7 + 3 + 0 = 10.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        best = baseCosts[0]

        def better(c: int) -> None:
            nonlocal best
            d, bd = abs(c - target), abs(best - target)
            if d < bd or (d == bd and c < best):
                best = c

        m = len(toppingCosts)

        def dfs(i: int, cost: int) -> None:
            better(cost)
            if i == m or cost >= target:
                return  # adding more only moves further above target
            dfs(i + 1, cost)
            dfs(i + 1, cost + toppingCosts[i])
            dfs(i + 1, cost + 2 * toppingCosts[i])

        for b in baseCosts:
            dfs(0, b)
        return best
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [746. Min Cost Climbing Stairs](../../0501-1000/0746-min-cost-climbing-stairs/)
- [857. Minimum Cost to Hire K Workers](../../0501-1000/0857-minimum-cost-to-hire-k-workers/)
- [1000. Minimum Cost to Merge Stones](../../0501-1000/1000-minimum-cost-to-merge-stones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/closest-dessert-cost/)
