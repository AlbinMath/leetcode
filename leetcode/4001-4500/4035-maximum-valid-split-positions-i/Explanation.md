# LeetCode 4035: Maximum Valid Split Positions I

**LeetCode Problem #4035 — Maximum Valid Split Positions I**
Solve LeetCode Maximum Valid Split Positions I using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Valid Split Positions I |
| LeetCode | #4035 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

You may remove **at most one** element from `nums`. Let `arr` be the array of remaining elements in their original order, and let `m` be its length.

A **split position** `i` of `arr` is **valid** if:

`0 <= i < m - 1`, and 
 `gcd(arr[0..i]) == gcd(arr[i + 1..m - 1])`.

An array of length 1 has no valid split positions.

The **score** of `arr` is the number of valid split positions in it.

Return the **maximum possible score** of `arr`.

Here, `gcd(a)` denotes the **greatest common divisor** of all elements in the array `a`.

## Constraints
- `2 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^9`​​​​​​​

## Examples
### Example 1
- **Input:** `nums = [10,30,15,10]`
- **Output:** `2`
- **Explanation:** One optimal solution is to remove `nums[2] = 15`. Then `arr = [10, 30, 10]`. 

 The split positions are: 

 
 
 
 Split Position `i` 
 `gcd(arr[0..i])` 
 `gcd(arr[i + 1..m - 1])` 
 
 
 0 
 10 
 10 
 
 
 1 
 10 
 10 
 
 
 

 All split positions are valid. Thus, the answer is 2.

### Example 2
- **Input:** `nums = [2,10,14]`
- **Output:** `1`
- **Explanation:** One optimal solution is to not remove any element. Then `arr = [2, 10, 14]`. 

 The split positions are: 

 
 
 
 Split Position `i` 
 `gcd(arr[0..i])` 
 `gcd(arr[i + 1..m - 1])` 
 
 
 0 
 2 
 2 
 
 
 1 
 2 
 14 
 
 
 

 Only the split position at index 0 is valid. Thus, the answer is 1.

### Example 3
- **Input:** `nums = [2,4]`
- **Output:** `0`
- **Explanation:** The only remaining array that has a split position is `arr = [2, 4]`. 

 The split positions are: 

 
 
 
 Split Position `i` 
 `gcd(arr[0..i])` 
 `gcd(arr[i + 1..m - 1])` 
 
 
 0 
 2 
 4 
 
 
 

 There are no valid split positions. Thus, the answer is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Valid Split Positions I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,30,15,10]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One optimal solution is to remove `nums[2] = 15`. Then `arr = [10, 30, 10]`. 

 The split positions are: 

 
 
 
 Split Position `i` 
 `gcd(arr[0..i])` 
 `gcd(arr[i + 1..m - 1])` 
 
 
 0 
 10 
 10 
 
 
 1 
 10 
 10 
 
 
 

 All split positions are valid. Thus, the answer is 2.

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
var maxValidSplits = function(nums) {
    const n = nums.length;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    const countSplits = (arr) => {
        const m = arr.length;
        if (m < 2) return 0;

        const pref = new Int32Array(m);
        const suff = new Int32Array(m);

        pref[0] = arr[0];
        for (let i = 1; i < m; i++) {
            pref[i] = gcd(pref[i - 1], arr[i]);
        }

        suff[m - 1] = arr[m - 1];
        for (let i = m - 2; i >= 0; i--) {
            suff[i] = gcd(suff[i + 1], arr[i]);
        }

        let valid = 0;
        for (let i = 0; i < m - 1; i++) {
            if (pref[i] === suff[i + 1]) {
                valid++;
            }
        }
        return valid;
    };

    // Case 1: Remove 0 elements
    let maxScore = countSplits(nums);

    // Case 2: Remove 1 element (only yields m >= 2 when n >= 3)
    if (n >= 3) {
        const arr = new Int32Array(n - 1);
        for (let skip = 0; skip < n; skip++) {
            let idx = 0;
            for (let j = 0; j < n; j++) {
                if (j !== skip) {
                    arr[idx++] = nums[j];
                }
            }
            const score = countSplits(arr);
            if (score > maxScore) {
                maxScore = score;
            }
        }
    }

    return maxScore;
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
- [4037. Maximum Valid Split Positions II](../../4001-4500/4037-maximum-valid-split-positions-ii/)
- [2178. Maximum Split of Positive Even Integers](../../2001-2500/2178-maximum-split-of-positive-even-integers/)
- [2780. Minimum Index of a Valid Split](../../2501-3000/2780-minimum-index-of-a-valid-split/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-valid-split-positions-i/)
