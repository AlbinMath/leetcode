# LeetCode 1922: Count Good Numbers

**LeetCode Problem #1922 — Count Good Numbers**
Solve LeetCode Count Good Numbers using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Good Numbers |
| LeetCode | #1922 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A digit string is **good** if the digits **(0-indexed)** at **even** indices are **even** and the digits at **odd** indices are **prime** (`2`, `3`, `5`, or `7`).

For example, `"2582"` is good because the digits (`2` and `8`) at even positions are even and the digits (`5` and `2`) at odd positions are prime. However, `"3245"` is **not** good because `3` is at an even index but is not even.

Given an integer `n`, return *the **total** number of good digit strings of length *`n`. Since the answer may be large, **return it modulo **`10^9 + 7`.

A **digit string** is a string consisting of digits `0` through `9` that may contain leading zeros.

## Constraints
- `1 <= n <= 10^15`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `5`
- **Explanation:** The good numbers of length 1 are "0", "2", "4", "6", "8".

### Example 2
- **Input:** `n = 4`
- **Output:** `400`

### Example 3
- **Input:** `n = 50`
- **Output:** `564908303`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Good Numbers**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The good numbers of length 1 are "0", "2", "4", "6", "8".

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
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        odd = n // 2
        even = n - odd
        return pow(5, even, MOD) * pow(4, odd, MOD) % MOD
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
- [1448. Count Good Nodes in Binary Tree](../../1501-2000/1544-count-good-nodes-in-binary-tree/)
- [1534. Count Good Triplets](../../1501-2000/1656-count-good-triplets/)
- [2179. Count Good Triplets in an Array](../../2001-2500/2280-count-good-triplets-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-good-numbers/)
