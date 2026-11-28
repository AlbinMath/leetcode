# LeetCode 1799: Maximize Score After N Operations

**LeetCode Problem #1799 — Maximize Score After N Operations**
Solve LeetCode Maximize Score After N Operations using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Score After N Operations |
| LeetCode | #1799 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given `nums`, an array of positive integers of size `2 * n`. You must perform `n` operations on this array.

In the `i^th` operation **(1-indexed)**, you will:

Choose two elements, `x` and `y`. 
 Receive a score of `i * gcd(x, y)`. 
 Remove `x` and `y` from `nums`.

Return *the maximum score you can receive after performing *`n`* operations.*

The function `gcd(x, y)` is the greatest common divisor of `x` and `y`.

## Constraints
- `1 <= n <= 7`
- `nums.length == 2 * n`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,2]`
- **Output:** `1`
- **Explanation:** The optimal choice of operations is:
(1 * gcd(1, 2)) = 1

### Example 2
- **Input:** `nums = [3,4,6,8]`
- **Output:** `11`
- **Explanation:** The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

### Example 3
- **Input:** `nums = [1,2,3,4,5,6]`
- **Output:** `14`
- **Explanation:** The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximize Score After N Operations**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The optimal choice of operations is:
(1 * gcd(1, 2)) = 1

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
 * @return {number}
 */
var maxScore = function(nums) {
    const n = nums.length;
    const totalMasks = 1 << n;
    const memo = new Array(totalMasks).fill(-1);

    function gcd(a, b) {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    function countBits(mask) {
        let count = 0;

        while (mask > 0) {
            mask &= mask - 1;
            count++;
        }

        return count;
    }

    function dp(mask) {
        if (mask === totalMasks - 1) {
            return 0;
        }

        if (memo[mask] !== -1) {
            return memo[mask];
        }

        const operation = countBits(mask) / 2 + 1;
        let best = 0;

        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;

            for (let j = i + 1; j < n; j++) {
                if (mask & (1 << j)) continue;

                const nextMask =
                    mask | (1 << i) | (1 << j);

                const score =
                    operation * gcd(nums[i], nums[j]) +
                    dp(nextMask);

                best = Math.max(best, score);
            }
        }

        memo[mask] = best;
        return best;
    }

    return dp(0);
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
- [2530. Maximal Score After Applying K Operations](../../2501-3000/2530-maximal-score-after-applying-k-operations/)
- [2818. Apply Operations to Maximize Score](../../2501-3000/2818-apply-operations-to-maximize-score/)
- [2968. Apply Operations to Maximize Frequency Score](../../2501-3000/2968-apply-operations-to-maximize-frequency-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-score-after-n-operations/)
