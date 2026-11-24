# LeetCode 3871: Count Commas in Range II

**LeetCode Problem #3871 — Count Commas in Range II**
Solve LeetCode Count Commas in Range II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Commas in Range II |
| LeetCode | #3871 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`.

Return the **total** number of commas used when writing all integers from `[1, n]` (inclusive) in **standard** number formatting.

In **standard** formatting:

A comma is inserted after **every three** digits from the right. 
 Numbers with **fewer** than 4 digits contain no commas.

## Constraints
- `1 <= n <= 10^15`

## Examples
### Example 1
- **Input:** `n = 1002`
- **Output:** `3`
- **Explanation:** The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

### Example 2
- **Input:** `n = 998`
- **Output:** `0`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Commas in Range II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1002`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

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
    let ans = 0;
    let power = 1000;

    while (power <= n) {
        ans += n - power + 1;
        power *= 1000;
    }

    return ans;
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3870. Count Commas in Range](../../3501-4000/3870-count-commas-in-range/)
- [327. Count of Range Sum](../../0001-0500/0327-count-of-range-sum/)
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1523-count-odd-numbers-in-an-interval-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-commas-in-range-ii/)
