# LeetCode 3524: Find X Value of Array I

**LeetCode Problem #3524 — Find X Value of Array I**
Solve LeetCode Find X Value of Array I using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find X Value of Array I |
| LeetCode | #3524 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of **positive** integers `nums`, and a **positive** integer `k`.

You are allowed to perform an operation **once** on `nums`, where in each operation you can remove any **non-overlapping** prefix and suffix from `nums` such that `nums` remains **non-empty**.

You need to find the **x-value** of `nums`, which is the number of ways to perform this operation so that the **product** of the remaining elements leaves a *remainder* of `x` when divided by `k`.

Return an array `result` of size `k` where `result[x]` is the **x-value** of `nums` for `0 <= x <= k - 1`.

A **prefix** of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A **suffix** of an array is a subarray that starts at any point within the array and extends to the end of the array.

**Note** that the prefix and suffix to be chosen for the operation can be **empty**.

## Constraints
- `1 <= nums[i] <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= k <= 5`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5], k = 3`
- **Output:** `[9,2,4]`
- **Explanation:** For `x = 0`, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove `nums[2] == 3`. 
 For `x = 1`, the possible operations are:
 
 Remove the empty prefix and the suffix `[2, 3, 4, 5]`. `nums` becomes `[1]`. 
 Remove the prefix `[1, 2, 3]` and the suffix `[5]`. `nums` becomes `[4]`. 
 
 
 For `x = 2`, the possible operations are:
 
 Remove the empty prefix and the suffix `[3, 4, 5]`. `nums` becomes `[1, 2]`. 
 Remove the prefix `[1]` and the suffix `[3, 4, 5]`. `nums` becomes `[2]`. 
 Remove the prefix `[1, 2, 3]` and the empty suffix. `nums` becomes `[4, 5]`. 
 Remove the prefix `[1, 2, 3, 4]` and the empty suffix. `nums` becomes `[5]`.

### Example 2
- **Input:** `nums = [1,2,4,8,16,32], k = 4`
- **Output:** `[18,1,2,0]`
- **Explanation:** For `x = 0`, the only operations that

### Example 3
- **Input:** `nums = [1,1,2,1,1], k = 2`
- **Output:** `[9,6]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Dynamic Programming** to count the products of all possible contiguous subarrays efficiently.
1. It initializes an array `result` of size `k` to store the final counts for each remainder.
2. It uses a `dp` array (size `k`), where `dp[r]` keeps track of how many subarrays ending at the *previous* element have a product whose remainder modulo `k` is `r`.
3. It iterates through each `num` in `nums`:
   - It calculates the remainder `x` of the current number itself (`num % k`).
   - It creates a `next` array to represent subarrays ending at the *current* position.
   - It counts the subarray that consists *only* of the current element: `next[x]++`.
   - It extends all previous subarrays: for every remainder `r` in `dp`, the new remainder if the current number is appended is `(r * x) % k`. It adds the count `dp[r]` to `next[newRemainder]`.
   - After computing all subarrays ending at the current position (`next`), it adds these counts to the overall `result` array.
   - Finally, it updates `dp = next` for the next iteration.
4. It returns the `result` array containing the aggregated counts.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5], k = 3`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[9,2,4]`.
4. **Verification:** For `x = 0`, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove `nums[2] == 3`. 
 For `x = 1`, the possible operations are:
 
 Remove the empty prefix and the suffix `[2, 3, 4, 5]`. `nums` becomes `[1]`. 
 Remove the prefix `[1, 2, 3]` and the suffix `[5]`. `nums` becomes `[4]`. 
 
 
 For `x = 2`, the possible operations are:
 
 Remove the empty prefix and the suffix `[3, 4, 5]`. `nums` becomes `[1, 2]`. 
 Remove the prefix `[1]` and the suffix `[3, 4, 5]`. `nums` becomes `[2]`. 
 Remove the prefix `[1, 2, 3]` and the empty suffix. `nums` becomes `[4, 5]`. 
 Remove the prefix `[1, 2, 3, 4]` and the empty suffix. `nums` becomes `[5]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var resultArray = function(nums, k) {
    const result = new Array(k).fill(0);

    // dp[r] = number of subarrays ending at previous position
    // whose product % k == r
    let dp = new Array(k).fill(0);

    for (const num of nums) {
        const x = num % k;
        const next = new Array(k).fill(0);

        // Subarray consisting only of the current element
        next[x]++;

        // Extend every previous subarray
        for (let r = 0; r < k; r++) {
            if (dp[r] > 0) {
                const newRemainder = (r * x) % k;
                next[newRemainder] += dp[r];
            }
        }

        // All subarrays ending here contribute to the answer
        for (let r = 0; r < k; r++) {
            result[r] += next[r];
        }

        dp = next;
    }

    return result;
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3525. Find X Value of Array II](../../3501-4000/3525-find-x-value-of-array-ii/)
- [2562. Find the Array Concatenation Value](../../2501-3000/2562-find-the-array-concatenation-value/)
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-x-value-of-array-i/)
