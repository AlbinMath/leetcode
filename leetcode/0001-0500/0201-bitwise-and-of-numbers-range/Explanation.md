# LeetCode 201: Bitwise AND of Numbers Range

**LeetCode Problem #201 — Bitwise AND of Numbers Range**
Solve LeetCode Bitwise AND of Numbers Range using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Bitwise AND of Numbers Range |
| LeetCode | #201 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `left` and `right` that represent the range `[left, right]`, return *the bitwise AND of all numbers in this range, inclusive*.

## Constraints
- `0 <= left <= right <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `left = 5, right = 7`
- **Output:** `4`

### Example 2
- **Input:** `left = 0, right = 0`
- **Output:** `0`

### Example 3
- **Input:** `left = 1, right = 2147483647`
- **Output:** `0`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Bitwise AND of Numbers Range**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `left = 5, right = 7`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var rangeBitwiseAnd = function(left, right) {
    let shifts = 0;

    while (left < right) {
        left >>>= 1;
        right >>>= 1;
        shifts++;
    }

    return left << shifts;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1630-count-odd-numbers-in-an-interval-range/)
- [2523. Closest Prime Numbers in Range](../../2501-3000/2610-closest-prime-numbers-in-range/)
- [3751. Total Waviness of Numbers in Range I](../../4001-4500/4057-total-waviness-of-numbers-in-range-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
