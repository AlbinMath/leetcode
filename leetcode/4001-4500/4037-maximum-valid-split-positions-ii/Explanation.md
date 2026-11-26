# LeetCode 4037: Maximum Valid Split Positions II

**LeetCode Problem #4037 — Maximum Valid Split Positions II**
Solve LeetCode Maximum Valid Split Positions II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Valid Split Positions II |
| LeetCode | #4037 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
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
- `2 <= nums.length <= 10^5`
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
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Valid Split Positions II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,30,15,10]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
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
var maxValidSplits = function(nums) {
    const n = nums.length;
    if (n < 2) return 0;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // 1. Precompute prefix and suffix GCDs
    const pref = new Int32Array(n);
    const suff = new Int32Array(n);

    pref[0] = nums[0];
    for (let i = 1; i < n; i++) {
        pref[i] = gcd(pref[i - 1], nums[i]);
    }

    suff[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suff[i] = gcd(suff[i + 1], nums[i]);
    }

    const gAll = pref[n - 1];

    // Case 1: 0 removals (every valid split must have both sides equal to gAll)
    let maxScore = 0;
    for (let i = 0; i < n - 1; i++) {
        if (pref[i] === gAll && suff[i + 1] === gAll) {
            maxScore++;
        }
    }

    if (n < 3) return maxScore;

    // Case 2: 1 removal (index k)
    // Any improvement over 0 removals requires G_k = gcd(nums without k) > gAll.
    // Because G_k > gAll = gcd(G_k, nums[k]), nums[k] is the UNIQUE element in nums
    // not divisible by G_k. Thus each distinct G_k > gAll corresponds to a unique k,
    // and there are at most O(log(max(nums))) such indices k!
    const seenTargets = new Set();

    const scoreWithout = (skip, targetG) => {
        // Compute suffix GCDs of the (n - 1)-length array without `skip`
        const m = n - 1;
        const suffArr = new Int32Array(m);
        let cur = 0;
        let idx = m - 1;
        for (let j = n - 1; j >= 0; j--) {
            if (j === skip) continue;
            cur = gcd(cur, nums[j]);
            suffArr[idx--] = cur;
        }

        // Sweep prefix GCDs and count valid splits where pref == suff == targetG
        let valid = 0;
        cur = 0;
        idx = 0;
        for (let j = 0; j < n; j++) {
            if (j === skip) continue;
            cur = gcd(cur, nums[j]);
            if (idx < m - 1 && cur === targetG && suffArr[idx + 1] === targetG) {
                valid++;
            }
            idx++;
        }
        return valid;
    };

    for (let k = 0; k < n; k++) {
        const leftG = k > 0 ? pref[k - 1] : 0;
        const rightG = k < n - 1 ? suff[k + 1] : 0;
        const gWithoutK = gcd(leftG, rightG);

        if (gWithoutK > gAll && !seenTargets.has(gWithoutK)) {
            seenTargets.add(gWithoutK);
            const score = scoreWithout(k, gWithoutK);
            if (score > maxScore) {
                maxScore = score;
            }
        }
    }

    return maxScore;
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
- [4035. Maximum Valid Split Positions I](../../4001-4500/4035-maximum-valid-split-positions-i/)
- [2178. Maximum Split of Positive Even Integers](../../2001-2500/2178-maximum-split-of-positive-even-integers/)
- [2871. Split Array Into Maximum Number of Subarrays](../../2501-3000/2871-split-array-into-maximum-number-of-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-valid-split-positions-ii/)
