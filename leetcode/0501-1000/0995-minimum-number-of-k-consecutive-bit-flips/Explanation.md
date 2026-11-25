# LeetCode 995: Minimum Number of K Consecutive Bit Flips

**LeetCode Problem #995 — Minimum Number of K Consecutive Bit Flips**
Solve LeetCode Minimum Number of K Consecutive Bit Flips using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of K Consecutive Bit Flips |
| LeetCode | #995 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary array `nums` and an integer `k`.

A **k-bit flip** is choosing a **subarray** of length `k` from `nums` and simultaneously changing every `0` in the subarray to `1`, and every `1` in the subarray to `0`.

Return *the minimum number of **k-bit flips** required so that there is no *`0`* in the array*. If it is not possible, return `-1`.

A **subarray** is a **contiguous** part of an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [0,1,0], k = 1`
- **Output:** `2`
- **Explanation:** Flip nums[0], then flip nums[2].

### Example 2
- **Input:** `nums = [1,1,0], k = 2`
- **Output:** `-1`
- **Explanation:** No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

### Example 3
- **Input:** `nums = [0,0,0,1,0,1,1,0], k = 3`
- **Output:** `3`
- **Explanation:** Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Number of K Consecutive Bit Flips**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,0], k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Flip nums[0], then flip nums[2].

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
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minKBitFlips = function (nums, k) {
    const n = nums.length;
    const ends = new Uint8Array(n + 1); // ends[i] = 1 if a flip expires at i
    let flipped = 0;
    let count = 0;

    for (let i = 0; i < n; i++) {
        if (ends[i]) flipped ^= 1;           // a flip stops covering index i
        if ((nums[i] ^ flipped) === 0) {     // current effective bit is 0
            if (i + k > n) return -1;        // not enough room for a flip
            flipped ^= 1;
            ends[i + k] = 1;
            count++;
        }
    }
    return count;
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
- [2220. Minimum Bit Flips to Convert Number](../../2001-2500/2220-minimum-bit-flips-to-convert-number/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/)
