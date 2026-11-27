# LeetCode 3897: Maximum Value of Concatenated Binary Segments

**LeetCode Problem #3897 — Maximum Value of Concatenated Binary Segments**
Solve LeetCode Maximum Value of Concatenated Binary Segments using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value of Concatenated Binary Segments |
| LeetCode | #3897 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums0`, each of size `n`.

`nums1[i]` represents the number of `'1'`s in the `i^th` segment. 
 `nums0[i]` represents the number of `'0'`s in the `i^th` segment.

For each index `i`, construct a binary segment consisting of:

`nums1[i]` occurrences of `'1'` followed by 
 `nums0[i]` occurrences of `'0'`.

You may **rearrange** the order of these **segments** in any way. After rearranging, **concatenate** all segments to form a single binary string.

Return the **maximum** possible integer value of the concatenated binary string.

Since the result can be very large, return the answer **modulo** `10^9 + 7`.

## Constraints
- `1 <= n == nums1.length == nums0.length <= 10^5`
- `0 <= nums1[i], nums0[i] <= 10^4`
- `nums1[i] + nums0[i] > 0`
- The total sum of all elements in `nums1` and `nums0` does not exceed 2 * 10^5.

## Examples
### Example 1
- **Input:** `nums1 = [1,2], nums0 = [1,0]`
- **Output:** `14`
- **Explanation:** At index 0, `nums1[0] = 1` and `nums0[0] = 1`, so the segment formed is `"10"`. 
 At index 1, `nums1[1] = 2` and `nums0[1] = 0`, so the segment formed is `"11"`. 
 Reordering the segments as `"11"` followed by `"10"` produces the binary string `"1110"`. 
 The binary number `"1110"` has value 14 which is the maximum possible value.

### Example 2
- **Input:** `nums1 = [3,1], nums0 = [0,3]`
- **Output:** `120`
- **Explanation:** At index 0, `nums1[0] = 3` and `nums0[0] = 0`, so the segment formed is `"111"`. 
 At index 1, `nums1[1] = 1` and `nums0[1] = 3`, so the segment formed is `"1000"`. 
 Reordering the segments as `"111"` followed by `"1000"` produces the binary string `"1111000"`. 
 The binary number `"1111000"` has value 120 which is the maximum possible value.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Value of Concatenated Binary Segments**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2], nums0 = [1,0]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** At index 0, `nums1[0] = 1` and `nums0[0] = 1`, so the segment formed is `"10"`. 
 At index 1, `nums1[1] = 2` and `nums0[1] = 0`, so the segment formed is `"11"`. 
 Reordering the segments as `"11"` followed by `"10"` produces the binary string `"1110"`. 
 The binary number `"1110"` has value 14 which is the maximum possible value.

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
var maxValue = function(nums1, nums0) {
    const MOD = 1000000007n;
    const n = nums1.length;

    const segments = [];

    let totalLength = 0;

    for (let i = 0; i < n; i++) {
        segments.push([nums1[i], nums0[i]]);
        totalLength += nums1[i] + nums0[i];
    }

    function compare(A, B) {
        const x = [
            [1, A[0]],
            [0, A[1]],
            [1, B[0]],
            [0, B[1]]
        ];

        const y = [
            [1, B[0]],
            [0, B[1]],
            [1, A[0]],
            [0, A[1]]
        ];

        let i = 0;
        let j = 0;
        let remX = 0;
        let remY = 0;

        while (i < 4 && j < 4) {
            while (i < 4 && remX === 0) {
                remX = x[i][1];
                if (remX === 0) i++;
            }

            while (j < 4 && remY === 0) {
                remY = y[j][1];
                if (remY === 0) j++;
            }

            if (i === 4 || j === 4) break;

            if (x[i][0] !== y[j][0]) {
                return x[i][0] === 1 ? -1 : 1;
            }

            const take = Math.min(remX, remY);

            remX -= take;
            remY -= take;

            if (remX === 0) i++;
            if (remY === 0) j++;
        }

        return 0;
    }

    segments.sort(compare);

    const pow2 = new Array(totalLength + 1);
    pow2[0] = 1n;

    for (let i = 1; i <= totalLength; i++) {
        pow2[i] = (pow2[i - 1] * 2n) % MOD;
    }

    let ans = 0n;

    for (const [ones, zeros] of segments) {
        ans = (ans * pow2[ones] + pow2[ones] - 1n) % MOD;

        ans = (ans * pow2[zeros]) % MOD;
    }

    return Number(ans);
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
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [654. Maximum Binary Tree](../../0501-1000/0654-maximum-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/)
