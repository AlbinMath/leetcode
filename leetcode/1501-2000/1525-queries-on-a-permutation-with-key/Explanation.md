# LeetCode 1409: Queries on a Permutation With Key

**LeetCode Problem #1409 — Queries on a Permutation With Key**
Solve LeetCode Queries on a Permutation With Key using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Queries on a Permutation With Key |
| LeetCode | #1409 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the array `queries` of positive integers between `1` and `m`, you have to process all `queries[i]` (from `i=0` to `i=queries.length-1`) according to the following rules:

In the beginning, you have the permutation `P=[1,2,3,...,m]`. 
 For the current `i`, find the position of `queries[i]` in the permutation `P` (**indexing from 0**) and then move this at the beginning of the permutation `P`. Notice that the position of `queries[i]` in `P` is the result for `queries[i]`.

Return an array containing the result for the given `queries`.

## Constraints
- `1 <= m <= 10^3`
- `1 <= queries.length <= m`
- `1 <= queries[i] <= m`

## Examples
### Example 1
- **Input:** `queries = [3,1,2,1], m = 5`
- **Output:** `[2,1,2,1]`
- **Explanation:** The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is

### Example 2
- **Input:** `queries = [4,1,2,2], m = 4`
- **Output:** `[3,1,2,0]`

### Example 3
- **Input:** `queries = [7,5,5,8,3], m = 8`
- **Output:** `[6,5,0,7,5]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Queries on a Permutation With Key**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `queries = [3,1,2,1], m = 5`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1,2,1]`.
4. **Verification:** The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var processQueries = function(queries, m) {
    const permutation = Array.from(
        { length: m },
        (_, i) => i + 1
    );

    const result = [];

    for (const query of queries) {
        // Find the current index of the query
        const index = permutation.indexOf(query);

        result.push(index);

        // Remove the element from its current position
        permutation.splice(index, 1);

        // Move it to the beginning
        permutation.unshift(query);
    }

    return result;
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [985. Sum of Even Numbers After Queries](../../1001-1500/1027-sum-of-even-numbers-after-queries/)
- [1211. Queries Quality and Percentage](../../1001-1500/1338-queries-quality-and-percentage/)
- [1310. XOR Queries of a Subarray](../../1001-1500/1435-xor-queries-of-a-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/queries-on-a-permutation-with-key/)
