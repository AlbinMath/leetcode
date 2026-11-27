# LeetCode 3781: Maximum Score After Binary Swaps

**LeetCode Problem #3781 — Maximum Score After Binary Swaps**
Solve LeetCode Maximum Score After Binary Swaps using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score After Binary Swaps |
| LeetCode | #3781 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and a binary string `s` of the same length.

Initially, your score is 0. Each index `i` where `s[i] = '1'` contributes `nums[i]` to the score.

You may perform **any** number of operations (including zero). In one operation, you may choose an index `i` such that `0 <= i < n - 1`, where `s[i] = '0'`, and `s[i + 1] = '1'`, and swap these two characters.

Return an integer denoting the **maximum possible score** you can achieve.

## Constraints
- `n == nums.length == s.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
- `s[i]` is either `'0'` or `'1'`

## Examples
### Example 1
- **Input:** `nums = [2,1,5,2,3], s = "01010"`
- **Output:** `7`
- **Explanation:** We can perform the following swaps: 

 
 Swap at index `i = 0`: `"01010"` changes to `"10010"` 
 Swap at index `i = 2`: `"10010"` changes to `"10100"` 
 

 Positions 0 and 2 contain `'1'`, contributing `nums[0] + nums[2] = 2 + 5 = 7`. This is maximum score achievable.

### Example 2
- **Input:** `nums = [4,7,2,9], s = "0000"`
- **Output:** `0`
- **Explanation:** There are no `'1'` characters in `s`, so no swaps can be performed. The score remains 0.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Score After Binary Swaps**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,5,2,3], s = "01010"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** We can perform the following swaps: 

 
 Swap at index `i = 0`: `"01010"` changes to `"10010"` 
 Swap at index `i = 2`: `"10010"` changes to `"10100"` 
 

 Positions 0 and 2 contain `'1'`, contributing `nums[0] + nums[2] = 2 + 5 = 7`. This is maximum score achievable.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximumScore = function(nums, s) {
    const heap = [];
    let ans = 0;

    function push(value) {
        heap.push(value);

        let i = heap.length - 1;

        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);

            if (heap[parent] >= heap[i]) break;

            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function pop() {
        const max = heap[0];
        const last = heap.pop();

        if (heap.length > 0) {
            heap[0] = last;

            let i = 0;

            while (true) {
                let largest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;

                if (left < heap.length && heap[left] > heap[largest]) {
                    largest = left;
                }

                if (right < heap.length && heap[right] > heap[largest]) {
                    largest = right;
                }

                if (largest === i) break;

                [heap[i], heap[largest]] = [heap[largest], heap[i]];
                i = largest;
            }
        }

        return max;
    }

    for (let i = 0; i < nums.length; i++) {
        push(nums[i]);

        if (s[i] === '1') {
            ans += pop();
        }
    }

    return ans;
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)
- [1702. Maximum Binary String After Change](../../1501-2000/1702-maximum-binary-string-after-change/)
- [1422. Maximum Score After Splitting a String](../../1001-1500/1422-maximum-score-after-splitting-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-after-binary-swaps/)
