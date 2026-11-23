# LeetCode 3561: Resulting String After Adjacent Removals

**LeetCode Problem #3561 — Resulting String After Adjacent Removals**
Solve LeetCode Resulting String After Adjacent Removals using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Resulting String After Adjacent Removals |
| LeetCode | #3561 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters.

You **must** repeatedly perform the following operation while the string `s` has **at least** two **consecutive **characters:

Remove the **leftmost** pair of **adjacent** characters in the string that are **consecutive** in the alphabet, in either order (e.g., `'a'` and `'b'`, or `'b'` and `'a'`). 
 Shift the remaining characters to the left to fill the gap.

Return the resulting string after no more operations can be performed.

**Note:** Consider the alphabet as circular, thus `'a'` and `'z'` are consecutive.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abc"`
- **Output:** `"c"`
- **Explanation:** Remove `"ab"` from the string, leaving `"c"` as the remaining string. 
 No further operations are possible. Thus, the resulting string after all possible removals is `"c"`.

### Example 2
- **Input:** `s = "adcb"`
- **Output:** `""`
- **Explanation:** Remove `"dc"` from the string, leaving `"ab"` as the remaining string. 
 Remove `"ab"` from the string, leaving `""` as the remaining string. 
 No further operations are possible. Thus, the resulting string after all possible removals is `""`.

### Example 3
- **Input:** `s = "zadb"`
- **Output:** `"db"`
- **Explanation:** Remove `"za"` from the string, leaving `"db"` as the remaining string. 
 No further operations are possible. Thus, the resulting string after all possible removals is `"db"`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Resulting String After Adjacent Removals**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"c"`.
4. **Verification:** Remove `"ab"` from the string, leaving `"c"` as the remaining string. 
 No further operations are possible. Thus, the resulting string after all possible removals is `"c"`.

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
    def resultingString(self, s: str) -> str:
        stk = []
        
        for c in s:
            if stk and abs(ord(c) - ord(stk[-1])) in (1, 25):
                stk.pop()
            else:
                stk.append(c)
                
        return "".join(stk)
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
- [3746. Minimum String Length After Balanced Removals](../../4001-4500/4090-minimum-string-length-after-balanced-removals/)
- [1481. Least Number of Unique Integers after K Removals](../../1501-2000/1604-least-number-of-unique-integers-after-k-removals/)
- [2322. Minimum Score After Removals on a Tree](../../2001-2500/2400-minimum-score-after-removals-on-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/resulting-string-after-adjacent-removals/)
