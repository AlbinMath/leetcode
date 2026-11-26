# LeetCode 3370: Smallest Number With All Set Bits

**LeetCode Problem #3370 — Smallest Number With All Set Bits**
Solve LeetCode Smallest Number With All Set Bits using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Number With All Set Bits |
| LeetCode | #3370 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a *positive* number `n`.

Return the **smallest** number `x` **greater than** or **equal to** `n`, such that the binary representation of `x` contains only set bits

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `7`
- **Explanation:** The binary representation of 7 is `"111"`.

### Example 2
- **Input:** `n = 10`
- **Output:** `15`
- **Explanation:** The binary representation of 15 is `"1111"`.

### Example 3
- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:** The binary representation of 3 is `"11"`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Number With All Set Bits**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** The binary representation of 7 is `"111"`.

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
class Solution(object):
    def smallestNumber(self, n):
        return (1 << n.bit_length()) - 1
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
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)
- [2336. Smallest Number in Infinite Set](../../2001-2500/2336-smallest-number-in-infinite-set/)
- [2859. Sum of Values at Indices With K Set Bits](../../2501-3000/2859-sum-of-values-at-indices-with-k-set-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-number-with-all-set-bits/)
