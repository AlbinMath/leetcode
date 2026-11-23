# LeetCode 3870: Count Commas in Range

**LeetCode Problem #3870 — Count Commas in Range**
Solve LeetCode Count Commas in Range using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Commas in Range |
| LeetCode | #3870 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`.

Return the **total** number of commas used when writing all integers from `[1, n]` (inclusive) in **standard** number formatting.

In **standard** formatting:

A comma is inserted after **every three** digits from the right. 
 Numbers with **fewer** than 4 digits contain no commas.

## Constraints
- `1 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 1002`
- **Output:** `3`
- **Explanation:** The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

### Example 2
- **Input:** `n = 998`
- **Output:** `0`
- **Explanation:** All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Commas in Range**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1002`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

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
/**
 * @param {number} n
 * @return {number}
 */
var countCommas = function(n) {
    let count = 0;

    for (let i = 1000; i <= n; i++) {
        count += Math.floor((i.toString().length - 1) / 3);
    }

    return count;
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
- [3871. Count Commas in Range II](../../4001-4500/4248-count-commas-in-range-ii/)
- [327. Count of Range Sum](../../0001-0500/0327-count-of-range-sum/)
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1630-count-odd-numbers-in-an-interval-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-commas-in-range/)
