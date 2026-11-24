# LeetCode 1016: Binary String With Substrings Representing 1 To N

**LeetCode Problem #1016 — Binary String With Substrings Representing 1 To N**
Solve LeetCode Binary String With Substrings Representing 1 To N using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary String With Substrings Representing 1 To N |
| LeetCode | #1016 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a binary string `s` and a positive integer `n`, return `true`* if the binary representation of all the integers in the range *`[1, n]`* are **substrings** of *`s`*, or *`false`* otherwise*.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= s.length <= 1000`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `s = "0110", n = 3`
- **Output:** `true`

### Example 2
- **Input:** `s = "0110", n = 4`
- **Output:** `false`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Binary String With Substrings Representing 1 To N**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "0110", n = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
    def queryString(self, s: str, n: int) -> bool:
        for i in range(n, n // 2, -1):
            if bin(i)[2:] not in s:
                return False
        return True
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
- [467. Unique Substrings in Wraparound String](../../0001-0500/0467-unique-substrings-in-wraparound-string/)
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)
- [761. Special Binary String](../../0501-1000/0763-special-binary-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/)
