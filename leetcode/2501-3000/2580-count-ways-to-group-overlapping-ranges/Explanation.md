# LeetCode 2580: Count Ways to Group Overlapping Ranges

**LeetCode Problem #2580 — Count Ways to Group Overlapping Ranges**
Solve LeetCode Count Ways to Group Overlapping Ranges using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Ways to Group Overlapping Ranges |
| LeetCode | #2580 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `ranges` where `ranges[i] = [start_i, end_i]` denotes that all integers between `start_i` and `end_i` (both **inclusive**) are contained in the `i^th` range.

You are to split `ranges` into **two** (possibly empty) groups such that:

Each range belongs to exactly one group. 
 Any two **overlapping** ranges must belong to the **same** group.

Two ranges are said to be **overlapping** if there exists at least **one** integer that is present in both ranges.

For example, `[1, 3]` and `[2, 5]` are overlapping because `2` and `3` occur in both ranges.

Return *the **total number** of ways to split* `ranges` *into two groups*. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= ranges.length <= 10^5`
- `ranges[i].length == 2`
- `0 <= start_i <= end_i <= 10^9`

## Examples
### Example 1
- **Input:** `ranges = [[6,10],[5,15]]`
- **Output:** `2`
- **Explanation:** The two ranges are overlapping, so they must be in the same group.
Thus, there are two possible ways:
- Put both the ranges together in group 1.
- Put both the ranges together in group 2.

### Example 2
- **Input:** `ranges = [[1,3],[10,20],[2,5],[4,8]]`
- **Output:** `4`
- **Explanation:** Ranges [1,3], and [2,5] are overlapping. So, they must be in the same group.
Again, ranges [2,5] and [4,8] are also overlapping. So, they must also be in the same group. 
Thus, there are four possible ways to group them:
- All the ranges in group 1.
- All the ranges in group 2.
- Ranges [1,3], [2,5], and [4,8] in group 1 and [10,20] in group 2.
- Ranges [1,3], [2,5], and [4,8] in group 2 and [10,20] in group 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Ways to Group Overlapping Ranges**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `ranges = [[6,10],[5,15]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The two ranges are overlapping, so they must be in the same group.
Thus, there are two possible ways:
- Put both the ranges together in group 1.
- Put both the ranges together in group 2.

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
var countWays = function(ranges) {
    const MOD = 1000000007;

    ranges.sort((a, b) => a[0] - b[0]);

    let components = 0;
    let currentEnd = -1;
    for (const [start, end] of ranges) {
        if (start > currentEnd) {
            components++;
            currentEnd = end;
        } else {
            currentEnd = Math.max(currentEnd, end);
        }
    }

    let result = 1;

    for (let i = 0; i < components; i++) {
        result = (result * 2) % MOD;
    }

    return result;
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
- [1735. Count Ways to Make Array With Product](../../1501-2000/1735-count-ways-to-make-array-with-product/)
- [1916. Count Ways to Build Rooms in an Ant Colony](../../1501-2000/1916-count-ways-to-build-rooms-in-an-ant-colony/)
- [3725. Count Ways to Choose Coprime Integers from Rows](../../3501-4000/3725-count-ways-to-choose-coprime-integers-from-rows/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/)
