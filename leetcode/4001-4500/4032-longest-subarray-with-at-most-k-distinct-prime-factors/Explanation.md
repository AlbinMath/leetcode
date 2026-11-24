# LeetCode 4032: Longest Subarray With at Most K Distinct Prime Factors

**LeetCode Problem #4032 — Longest Subarray With at Most K Distinct Prime Factors**
Solve LeetCode Longest Subarray With at Most K Distinct Prime Factors using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subarray With at Most K Distinct Prime Factors |
| LeetCode | #4032 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` consisting of positive integers and an integer `k`.

The **prime factor set** of a **subarray** is the **union** of the distinct **prime** factors of all its elements.

Return the length of the **longest** subarray whose prime factor set contains **at most** `k` distinct prime factors. If no such subarray exists, return 0.

## Constraints
- `1 <= nums.length <= 10^5`
- `2 <= nums[i] <= 10^5`
- `1 <= k <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [7,6,10,12,11], k = 3`
- **Output:** `3`
- **Explanation:** Consider the subarray `[6, 10, 12]`: 

 
 The distinct prime factors of 6 are `{2, 3}`. 
 The distinct prime factors of 10 are `{2, 5}`. 
 The distinct prime factors of 12 are `{2, 3}`. 
 The union of these sets is `{2, 3, 5}`, which contains 3 distinct prime factors. 
 

 No longer subarray satisfies the condition. Therefore, the answer is 3.

### Example 2
- **Input:** `nums = [4,6,9,18], k = 4`
- **Output:** `4`
- **Explanation:** Consider the entire array `[4, 6, 9, 18]`: 

 
 The distinct prime factors of 4 are `{2}`. 
 The distinct prime factors of 6 are `{2, 3}`. 
 The distinct prime factors of 9 are `{3}`. 
 The distinct prime factors of 18 are `{2, 3}`. 
 The union of these sets is `{2, 3}`, which contains 2 distinct prime factors. 
 

 Since `2 <= 4`, the entire array is valid. Therefore, the answer is 4.

### Example 3
- **Input:** `nums = [6,10,15], k = 2`
- **Output:** `1`
- **Explanation:** Every subarray of length at least 2 has prime factor set `{2, 3, 5}`, which contains 3 distinct prime factors. 

 Since `3 > 2`, only subarrays of length 1 are valid. Therefore, the answer is 1.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Longest Subarray With at Most K Distinct Prime Factors**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [7,6,10,12,11], k = 3`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Consider the subarray `[6, 10, 12]`: 

 
 The distinct prime factors of 6 are `{2, 3}`. 
 The distinct prime factors of 10 are `{2, 5}`. 
 The distinct prime factors of 12 are `{2, 3}`. 
 The union of these sets is `{2, 3, 5}`, which contains 3 distinct prime factors. 
 

 No longer subarray satisfies the condition. Therefore, the answer is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var longestSubarray = function(nums, k) {
    const n = nums.length;
    let maxVal = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    // 1. Build Smallest Prime Factor (SPF) sieve up to maxVal
    const spf = new Int32Array(maxVal + 1);
    for (let i = 2; i <= maxVal; i++) {
        if (spf[i] === 0) {
            for (let j = i; j <= maxVal; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }

    // Helper to extract distinct prime factors of x
    const getPrimeFactors = (x) => {
        const factors = [];
        while (x > 1) {
            const p = spf[x];
            factors.push(p);
            while (x % p === 0) {
                x = Math.floor(x / p);
            }
        }
        return factors;
    };

    // Pre-factorize nums so each element is factorized only once
    const elemFactors = new Array(n);
    for (let i = 0; i < n; i++) {
        elemFactors[i] = getPrimeFactors(nums[i]);
    }

    // 2. Sliding window over nums
    const primeFreq = new Int32Array(maxVal + 1);
    let distinctCount = 0;
    let left = 0;
    let maxLen = 0;

    for (let right = 0; right < n; right++) {
        const rightFactors = elemFactors[right];
        for (let i = 0; i < rightFactors.length; i++) {
            const p = rightFactors[i];
            if (primeFreq[p] === 0) distinctCount++;
            primeFreq[p]++;
        }

        while (distinctCount > k) {
            const leftFactors = elemFactors[left];
            for (let i = 0; i < leftFactors.length; i++) {
                const p = leftFactors[i];
                primeFreq[p]--;
                if (primeFreq[p] === 0) distinctCount--;
            }
            left++;
        }

        const windowLen = right - left + 1;
        if (windowLen > maxLen) {
            maxLen = windowLen;
        }
    }

    return maxLen;
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [2958. Length of Longest Subarray With at Most K Frequency](../../2501-3000/2958-length-of-longest-subarray-with-at-most-k-frequency/)
- [2521. Distinct Prime Factors of Product of Array](../../2501-3000/2521-distinct-prime-factors-of-product-of-array/)
- [3545. Minimum Deletions for At Most K Distinct Characters](../../3501-4000/3545-minimum-deletions-for-at-most-k-distinct-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subarray-with-at-most-k-distinct-prime-factors/)
