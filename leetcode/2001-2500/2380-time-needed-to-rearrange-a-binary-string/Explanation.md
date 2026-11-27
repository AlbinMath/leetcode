# LeetCode 2380: Time Needed to Rearrange a Binary String

**LeetCode Problem #2380 — Time Needed to Rearrange a Binary String**
Solve LeetCode Time Needed to Rearrange a Binary String using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Time Needed to Rearrange a Binary String |
| LeetCode | #2380 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `s`.

In one second, **all** occurrences of `"01"` are **simultaneously** replaced with `"10"`. This process **repeats** until no occurrences of `"01"` exist.

Return the number of seconds needed to complete this process.

## Constraints
- `1 <= s.length <= 1000`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "0110101"`
- **Output:** `4`
- **Explanation:** After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.

### Example 2
- **Input:** `s = "11100"`
- **Output:** `0`
- **Explanation:** No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
so we return 0.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Time Needed to Rearrange a Binary String**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "0110101"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var secondsToRemoveOccurrences = function(s) {
    let zeros = 0;
    let seconds = 0;

    for (const ch of s) {
        if (ch === '0') {
            zeros++;
        } else if (zeros > 0) {
            seconds = Math.max(seconds + 1, zeros);
        }
    }

    return seconds;
};
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
- [1376. Time Needed to Inform All Employees](../../1001-1500/1376-time-needed-to-inform-all-employees/)
- [2073. Time Needed to Buy Tickets](../../2001-2500/2073-time-needed-to-buy-tickets/)
- [2385. Amount of Time for Binary Tree to Be Infected](../../2001-2500/2385-amount-of-time-for-binary-tree-to-be-infected/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/)
