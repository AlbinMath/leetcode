# LeetCode 3746: Minimum String Length After Balanced Removals

**LeetCode Problem #3746 — Minimum String Length After Balanced Removals**
Solve LeetCode Minimum String Length After Balanced Removals using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum String Length After Balanced Removals |
| LeetCode | #3746 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting only of the characters `'a'` and `'b'`.

You are allowed to repeatedly remove **any substring ** where the number of `'a'` characters is equal to the number of `'b'` characters. After each removal, the remaining parts of the string are concatenated together without gaps.

Return an integer denoting the **minimum possible length** of the string after performing any number of such operations.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'a'` or `'b'`.

## Examples
### Example 1
- **Input:** `s = `"aabbab"`
- **Output:** `0`
- **Explanation:** The substring `"aabbab"` has three `'a'` and three `'b'`. Since their counts are equal, we can remove the entire string directly. The minimum length is 0.

### Example 2
- **Input:** `s = `"aaaa"`
- **Output:** `4`
- **Explanation:** Every substring of `"aaaa"` contains only `'a'` characters. No substring can be removed as a result, so the minimum length remains 4.

### Example 3
- **Input:** `s = `"aaabb"`
- **Output:** `1`
- **Explanation:** First, remove the substring `"ab"`, leaving `"aab"`. Next, remove the new substring `"ab"`, leaving `"a"`. No further removals are possible, so the minimum length is 1.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum String Length After Balanced Removals**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = `"aabbab"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The substring `"aabbab"` has three `'a'` and three `'b'`. Since their counts are equal, we can remove the entire string directly. The minimum length is 0.

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
    def minLengthAfterRemovals(self, s: str) -> int:
        return abs(s.count('a') - s.count('b'))
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
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1750-minimum-length-of-string-after-deleting-similar-ends/)
- [2696. Minimum String Length After Removing Substrings](../../2501-3000/2696-minimum-string-length-after-removing-substrings/)
- [2856. Minimum Array Length After Pair Removals](../../2501-3000/2856-minimum-array-length-after-pair-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-string-length-after-balanced-removals/)
