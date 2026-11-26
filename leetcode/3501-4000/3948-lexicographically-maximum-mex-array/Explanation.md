# LeetCode 3948: Lexicographically Maximum MEX Array

**LeetCode Problem #3948 — Lexicographically Maximum MEX Array**
Solve LeetCode Lexicographically Maximum MEX Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Maximum MEX Array |
| LeetCode | #3948 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

You want to construct an array `result` by repeatedly performing the following operation until `nums` becomes empty:

Choose an integer `k` such that `1 <= k <= len(nums)`. 
 Compute the **MEX** of the first `k` elements of `nums`. 
 Append this **MEX** to `result`. 
 Remove the first `k` elements from `nums`.

Return the **lexicographically maximum** array `result` that can be obtained after performing the operations.

The **MEX** of an array is the **smallest non-negative** integer not present in the array.

An array `a` is **lexicographically greater** than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is greater than the corresponding element in `b`. If the first `min(a.length, b.length)` elements do not differ, then the longer array is the **lexicographically greater** one.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [0,1,0]`
- **Output:** `[2,1]`
- **Explanation:** Take the first `k = 2` elements `[0, 1]` which has MEX = 2. Current `result = [2]`. 
 Remaining array `[0]` has MEX = 1. Thus, the final `result = [2, 1]`.

### Example 2
- **Input:** `nums = [1,0,2]`
- **Output:** `[3]`
- **Explanation:** Take the first `k = 3` elements `[1, 0, 2]` which has MEX = 3. 
 ` nums ` is now empty. Thus, the final `result = [3]`.

### Example 3
- **Input:** `nums = [3,1]`
- **Output:** `[0,0]`
- **Explanation:** ​​​​​​​ 

 
 Take `k = 1`, first element `[3]` has MEX = 0. Current `result = [0]`. 
 Remaining array `[1]` has MEX = 0. Thus, the final `result = [0, 0]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Maximum MEX Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1]`.
4. **Verification:** Take the first `k = 2` elements `[0, 1]` which has MEX = 2. Current `result = [2]`. 
 Remaining array `[0]` has MEX = 1. Thus, the final `result = [2, 1]`.

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
 * @param {number[]} nums
 * @return {number[]}
 */
var maximumMEX = function (nums) {
    const n = nums.length;

    // suf[i] = mex of nums[i..n-1]
    const suf = new Array(n + 1).fill(0);
    const present = new Uint8Array(n + 2);
    let mex = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (nums[i] <= n) present[nums[i]] = 1;
        while (present[mex]) mex++;
        suf[i] = mex;
    }

    const res = [];
    const stamp = new Int32Array(n + 2).fill(-1);
    let seg = 0, i = 0;

    while (i < n) {
        const M = suf[i];
        if (M === 0) {
            res.push(0);
            i++;
            continue;
        }
        let cnt = 0;
        while (cnt < M) {
            const v = nums[i];
            if (v < M && stamp[v] !== seg) {
                stamp[v] = seg;
                cnt++;
            }
            i++;
        }
        res.push(M);
        seg++;
    }
    return res;
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
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-maximum-mex-array/)
