# LeetCode 3574: Maximize Subarray GCD Score

**LeetCode Problem #3574 — Maximize Subarray GCD Score**
Solve LeetCode Maximize Subarray GCD Score using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Subarray GCD Score |
| LeetCode | #3574 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of positive integers `nums` and an integer `k`.

You may perform at most `k` operations. In each operation, you can choose one element in the array and **double** its value. Each element can be doubled **at most** once.

The **score** of a contiguous ** subarray ** is defined as the **product** of its length and the *greatest common divisor (GCD)* of all its elements.

Your task is to return the **maximum** **score** that can be achieved by selecting a contiguous subarray from the modified array.

**Note:**

The **greatest common divisor (GCD)** of an array is the largest integer that evenly divides all the array elements.

## Constraints
- `1 <= n == nums.length <= 1500`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `nums = [2,4], k = 1`
- **Output:** `8`
- **Explanation:** Double `nums[0]` to 4 using one operation. The modified array becomes `[4, 4]`. 
 The GCD of the subarray `[4, 4]` is 4, and the length is 2. 
 Thus, the maximum possible score is `2 &times; 4 = 8`.

### Example 2
- **Input:** `nums = [3,5,7], k = 2`
- **Output:** `14`
- **Explanation:** Double `nums[2]` to 14 using one operation. The modified array becomes `[3, 5, 14]`. 
 The GCD of the subarray `[14]` is 14, and the length is 1. 
 Thus, the maximum possible score is `1 &times; 14 = 14`.

### Example 3
- **Input:** `nums = [5,5,5], k = 1`
- **Output:** `15`
- **Explanation:** The subarray `[5, 5, 5]` has a GCD of 5, and its length is 3. 
 Since doubling any element doesn't improve the score, the maximum score is `3 &times; 5 = 15`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximize Subarray GCD Score**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4], k = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Double `nums[0]` to 4 using one operation. The modified array becomes `[4, 4]`. 
 The GCD of the subarray `[4, 4]` is 4, and the length is 2. 
 Thus, the maximum possible score is `2 &times; 4 = 8`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

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
var maxGCDScore = function(nums, k) {
    const n = nums.length;

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Precompute the highest power of 2 dividing each nums[i]
    // Using division/modulo avoids 32-bit bitwise truncation since nums[i] <= 10^9
    const pow2 = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        let x = nums[i];
        let p = 1;
        while ((x & 1) === 0) {
            x >>= 1;
            p <<= 1;
        }
        pow2[i] = p;
    }

    let maxScore = 0;

    for (let i = 0; i < n; i++) {
        let g = 0;
        let minPow2 = Infinity;
        let minCount = 0;

        for (let j = i; j < n; j++) {
            g = gcd(g, nums[j]);
            const p = pow2[j];

            if (p < minPow2) {
                minPow2 = p;
                minCount = 1;
            } else if (p === minPow2) {
                minCount++;
            }

            const effectiveGcd = minCount <= k ? g * 2 : g;
            const score = effectiveGcd * (j - i + 1);
            if (score > maxScore) {
                maxScore = score;
            }
        }
    }

    return maxScore;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1793. Maximum Score of a Good Subarray](../../1501-2000/1793-maximum-score-of-a-good-subarray/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3001-3500/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)
- [4010. Maximize Pair Strength Using GCD](../../4001-4500/4010-maximize-pair-strength-using-gcd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-subarray-gcd-score/)
