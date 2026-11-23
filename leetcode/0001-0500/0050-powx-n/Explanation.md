# LeetCode 50: Pow(x, n)

**LeetCode Problem #50 — Pow(x, n)**
Solve LeetCode Pow(x, n) using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pow(x, n) |
| LeetCode | #50 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Implement pow(x, n) , which calculates `x` raised to the power `n` (i.e., `x^n`).

## Constraints
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31-1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.
- `-10^4 <= x^n <= 10^4`

## Examples
### Example 1
- **Input:** `x = 2.00000, n = 10`
- **Output:** `1024.00000`

### Example 2
- **Input:** `x = 2.10000, n = 3`
- **Output:** `9.26100`

### Example 3
- **Input:** `x = 2.00000, n = -2`
- **Output:** `0.25000`
- **Explanation:** 2^-2 = 1/2^2 = 1/4 = 0.25

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Pow(x, n)**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `x = 2.00000, n = 10`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1024.00000`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def myPow(self, x, n):
        negative = n < 0

        if n < 0:
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        if negative:
            return 1.0 / result

        return result
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [51. N-Queens](../../0001-0500/0051-n-queens/)
- [52. N-Queens II](../../0001-0500/0052-n-queens-ii/)
- [429. N-ary Tree Level Order Traversal](../../0501-1000/0764-n-ary-tree-level-order-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/powx-n/)
