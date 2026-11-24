# LeetCode 4098: Minimize the Maximum Value of GCD-Connected Array

**LeetCode Problem #4098 — Minimize the Maximum Value of GCD-Connected Array**
Solve LeetCode Minimize the Maximum Value of GCD-Connected Array using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize the Maximum Value of GCD-Connected Array |
| LeetCode | #4098 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three integers `n`, `index`, and `value`.

An integer array `nums` of length `n` is called **GCD-Connected** if:

`nums[i] > 0` for `0 <= i <= n - 1`. 
 `nums[i] < nums[i + 1]` for `0 <= i <= n - 2`. 
 `nums[index] = value`. 
 ` gcd (nums[i], nums[i + 1]) > 1` for `0 <= i <= n - 2`.

Return the **minimum** possible maximum value, `nums[n - 1]`, among all GCD-Connected arrays `nums`. If no such array exists, return -1.

## Constraints
- `2 <= n <= 10^9`
- `1 <= value <= 10^9`
- `0 <= index <= n - 1`

## Examples
### Example 1
- **Input:** `n = 4, index = 2, value = 8`
- **Output:** `10`
- **Explanation:** The GCD-Connected array will look like: ​​​​​​​`nums = [?, ?, 8, ?]` since `nums[2] = 8`. 
 Since `nums[3] > 8` and `gcd(8, 9) = 1`, every valid GCD-Connected array must have `nums[3] >= 10`. 
 One optimal array satisfying all conditions is `[2, 4, 8, 10]`. 
 Thus, the minimum possible value of `nums[3]` is 10.

### Example 2
- **Input:** `n = 2, index = 1, value = 3`
- **Output:** `-1`
- **Explanation:** The GCD-Connected array will look like: `nums = [?, 3]` since `nums[1] = 3`. 
 Since we need `0 < nums[0] < nums[1] = 3`, there are only two possible arrays: `[1, 3]` and `[2, 3]`. Neither of them satisfies `gcd(nums[0], nums[1]) > 1`. 
 Therefore, no valid GCD-Connected array exists, and the answer is -1.

### Example 3
- **Input:** `n = 2, index = 0, value = 3`
- **Output:** `6`
- **Explanation:** The GCD-Connected array will look like: `nums = [3, ?]` since `nums[0] = 3`. 
 Since `nums[1] > 3` and `gcd(3, 4) = gcd(3, 5) = 1`, every valid GCD-Connected array must have `nums[1] >= 6`. 
 One optimal array is `[3, 6]`. 
 Thus, the minimum possible value of `nums[1]` is 6.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimize the Maximum Value of GCD-Connected Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, index = 2, value = 8`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The GCD-Connected array will look like: ​​​​​​​`nums = [?, ?, 8, ?]` since `nums[2] = 8`. 
 Since `nums[3] > 8` and `gcd(8, 9) = 1`, every valid GCD-Connected array must have `nums[3] >= 10`. 
 One optimal array satisfying all conditions is `[2, 4, 8, 10]`. 
 Thus, the minimum possible value of `nums[3]` is 10.

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
var minimumMaxValue = function(n, index, value) {
    const smallestPrimeFactor = (x) => {
        if (x % 2 === 0) return 2;
        for (let d = 3; d * d <= x; d += 2) {
            if (x % d === 0) return d;
        }
        return x;
    };

    if (index > 0) {
        if (value === 1) return -1;
        const p = smallestPrimeFactor(value);
        if (value - p <= 2 * (index - 1)) {
            return -1;
        }
    }

    const rightSteps = n - 1 - index;
    if (rightSteps === 0) {
        return value;
    }

    if (value === 1) {
        return -1;
    }

    const p = smallestPrimeFactor(value);
    return value + p + 2 * (rightSteps - 1);
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
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)
- [1695. Maximum Erasure Value](../../1501-2000/1695-maximum-erasure-value/)
- [1881. Maximum Value after Insertion](../../1501-2000/1881-maximum-value-after-insertion/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-the-maximum-value-of-gcd-connected-array/)
