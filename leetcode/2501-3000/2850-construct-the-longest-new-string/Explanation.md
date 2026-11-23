# LeetCode 2745: Construct the Longest New String

**LeetCode Problem #2745 — Construct the Longest New String**
Solve LeetCode Construct the Longest New String using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct the Longest New String |
| LeetCode | #2745 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given three integers `x`, `y`, and `z`.

You have `x` strings equal to `"AA"`, `y` strings equal to `"BB"`, and `z` strings equal to `"AB"`. You want to choose some (possibly all or none) of these strings and concatenate them in some order to form a new string. This new string must not contain `"AAA"` or `"BBB"` as a substring.

Return *the maximum possible length of the new string*.

A substring is a contiguous **non-empty** sequence of characters within a string.

## Constraints
- `1 <= x, y, z <= 50`

## Examples
### Example 1
- **Input:** `x = 2, y = 5, z = 1`
- **Output:** `12`
- **Explanation:** We can concatenate the strings "BB", "AA", "BB", "AA", "BB", and "AB" in that order. Then, our new string is "BBAABBAABBAB". 
That string has length 12, and we can show that it is impossible to construct a string of longer length.

### Example 2
- **Input:** `x = 3, y = 2, z = 2`
- **Output:** `14`
- **Explanation:** We can concatenate the strings "AB", "AB", "AA", "BB", "AA", "BB", and "AA" in that order. Then, our new string is "ABABAABBAABBAA". 
That string has length 14, and we can show that it is impossible to construct a string of longer length.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Construct the Longest New String**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `x = 2, y = 5, z = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** We can concatenate the strings "BB", "AA", "BB", "AA", "BB", and "AB" in that order. Then, our new string is "BBAABBAABBAB". 
That string has length 12, and we can show that it is impossible to construct a string of longer length.

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
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            return 2 * (x + y + z)
        return 2 * (2 * min(x, y) + 1 + z)
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
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)
- [2182. Construct String With Repeat Limit](../../2001-2500/2300-construct-string-with-repeat-limit/)
- [2375. Construct Smallest Number From DI String](../../2001-2500/2456-construct-smallest-number-from-di-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-the-longest-new-string/)
