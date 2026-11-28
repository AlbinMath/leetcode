# LeetCode 2390: Removing Stars From a String

**LeetCode Problem #2390 — Removing Stars From a String**
Solve LeetCode Removing Stars From a String using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Removing Stars From a String |
| LeetCode | #2390 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s`, which contains stars `*`.

In one operation, you can:

Choose a star in `s`. 
 Remove the closest **non-star** character to its **left**, as well as remove the star itself.

Return *the string after **all** stars have been removed*.

**Note:**

The input will be generated such that the operation is always possible. 
 It can be shown that the resulting string will always be unique.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters and stars `*`.
- The operation above can be performed on `s`.

## Examples
### Example 1
- **Input:** `s = "leet**cod*e"`
- **Output:** `"lecoe"`
- **Explanation:** Performing the removals from left to right:
- The closest character to the 1^st star is 't' in "lee

### Example 2
- **Input:** `s = "erase*****"`
- **Output:** `""`
- **Explanation:** The entire string is removed, so we return an empty string.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Removing Stars From a String**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leet**cod*e"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"lecoe"`.
4. **Verification:** Performing the removals from left to right:
- The closest character to the 1^st star is 't' in "lee

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
var removeStars = function(s) {
    const stack = [];

    for (const ch of s) {
        if (ch === '*') {
            stack.pop();
        } else {
            stack.push(ch);
        }
    }

    return stack.join('');
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
- [3170. Lexicographically Minimum String After Removing Stars](../../3001-3500/3170-lexicographically-minimum-string-after-removing-stars/)
- [1717. Maximum Score From Removing Substrings](../../1501-2000/1717-maximum-score-from-removing-substrings/)
- [1753. Maximum Score From Removing Stones](../../1501-2000/1753-maximum-score-from-removing-stones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/)
