# LeetCode 696: Count Binary Substrings

**LeetCode Problem #696 — Count Binary Substrings**
Solve LeetCode Count Binary Substrings using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Binary Substrings |
| LeetCode | #696 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a binary string `s`, return the number of non-empty substrings that have the same number of `0`'s and `1`'s, and all the `0`'s and all the `1`'s in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "00110011"`
- **Output:** `6`
- **Explanation:** There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

### Example 2
- **Input:** `s = "10101"`
- **Output:** `4`
- **Explanation:** There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Binary Substrings**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "00110011"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

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
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1

        count += min(prev, curr)

        return count
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1448. Count Good Nodes in Binary Tree](../../1001-1500/1448-count-good-nodes-in-binary-tree/)
- [1638. Count Substrings That Differ by One Character](../../1501-2000/1638-count-substrings-that-differ-by-one-character/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-binary-substrings/)
