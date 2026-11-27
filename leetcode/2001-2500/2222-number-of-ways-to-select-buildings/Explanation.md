# LeetCode 2222: Number of Ways to Select Buildings

**LeetCode Problem #2222 — Number of Ways to Select Buildings**
Solve LeetCode Number of Ways to Select Buildings using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Select Buildings |
| LeetCode | #2222 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** binary string `s` which represents the types of buildings along a street where:

`s[i] = '0'` denotes that the `i^th` building is an office and 
 `s[i] = '1'` denotes that the `i^th` building is a restaurant.

As a city official, you would like to **select** 3 buildings for random inspection. However, to ensure variety, **no two consecutive** buildings out of the **selected** buildings can be of the same type.

For example, given `s = "0 **0** 1 **1** 0 **1** "`, we cannot select the `1^st`, `3^rd`, and `5^th` buildings as that would form `"0** 11 **"` which is **not** allowed due to having two consecutive buildings of the same type.

Return *the number of valid ways to select 3 buildings.*

## Constraints
- `3 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "001101"`
- **Output:** `6`
- **Explanation:** The following sets of indices selected are valid:
- [0,2,4] from "

### Example 2
- **Input:** `s = "11100"`
- **Output:** `0`
- **Explanation:** It can be shown that there are no valid selections.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Ways to Select Buildings**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "001101"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The following sets of indices selected are valid:
- [0,2,4] from "

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
var numberOfWays = function(s) {
    let totalZeros = 0;
    let totalOnes = 0;
    for (let ch of s) {
        if (ch === '0') {
            totalZeros++;
        } else {
            totalOnes++;
        }
    }
    let leftZeros = 0;
    let leftOnes = 0;
    let result = 0;

    for (let ch of s) {
        if (ch === '0') {
            let rightOnes = totalOnes - leftOnes;
            result += leftOnes * rightOnes;
            leftZeros++;
        } else {
            let rightZeros = totalZeros - leftZeros;
            result += leftZeros * rightZeros;
            leftOnes++;
        }
    }
    return result;
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
- [1269. Number of Ways to Stay in the Same Place After Some Steps](../../1001-1500/1269-number-of-ways-to-stay-in-the-same-place-after-some-steps/)
- [1411. Number of Ways to Paint N × 3 Grid](../../1001-1500/1411-number-of-ways-to-paint-n-3-grid/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1001-1500/1434-number-of-ways-to-wear-different-hats-to-each-other/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-select-buildings/)
