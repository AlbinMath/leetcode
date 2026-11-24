# LeetCode 1655: Distribute Repeating Integers

**LeetCode Problem #1655 — Distribute Repeating Integers**
Solve LeetCode Distribute Repeating Integers using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distribute Repeating Integers |
| LeetCode | #1655 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of `n` integers, `nums`, where there are at most `50` unique values in the array. You are also given an array of `m` customer order quantities, `quantity`, where `quantity[i]` is the amount of integers the `i^th` customer ordered. Determine if it is possible to distribute `nums` such that:

The `i^th` customer gets **exactly** `quantity[i]` integers, 
 The integers the `i^th` customer gets are **all equal**, and 
 Every customer is satisfied.

Return `true`* if it is possible to distribute *`nums`* according to the above conditions*.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 1000`
- `m == quantity.length`
- `1 <= m <= 10`
- `1 <= quantity[i] <= 10^5`
- There are at most `50` unique values in `nums`.

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4], quantity = [2]`
- **Output:** `false`
- **Explanation:** The 0^th customer cannot be given two different integers.

### Example 2
- **Input:** `nums = [1,2,3,3], quantity = [2]`
- **Output:** `true`
- **Explanation:** The 0^th customer is given [3,3]. The integers [1,2] are not used.

### Example 3
- **Input:** `nums = [1,1,2,2], quantity = [2,2]`
- **Output:** `true`
- **Explanation:** The 0^th customer is given [1,1], and the 1st customer is given [2,2].

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Distribute Repeating Integers**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4], quantity = [2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** The 0^th customer cannot be given two different integers.

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
 * @param {number[]} quantity
 * @return {boolean}
 */
var canDistribute = function(nums, quantity) {
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    const counts = [...freq.values()];
    const m = quantity.length;
    const totalMasks = 1 << m;
    const full = totalMasks - 1;

    // Precompute total demand for every customer subset.
    const sum = new Array(totalMasks).fill(0);

    for (let mask = 1; mask < totalMasks; mask++) {
        const bit = mask & -mask;
        const index = Math.log2(bit);

        sum[mask] = sum[mask ^ bit] + quantity[index];
    }

    // dp[mask] = whether this customer subset can be satisfied.
    let dp = new Array(totalMasks).fill(false);
    dp[0] = true;

    for (const count of counts) {
        const next = dp.slice();

        for (let mask = 0; mask < totalMasks; mask++) {
            if (!dp[mask]) continue;

            // Customers not yet assigned.
            const remaining = full ^ mask;

            // Try every non-empty subset of remaining customers.
            for (
                let sub = remaining;
                sub > 0;
                sub = (sub - 1) & remaining
            ) {
                if (sum[sub] <= count) {
                    next[mask | sub] = true;
                }
            }
        }

        dp = next;

        if (dp[full]) return true;
    }

    return dp[full];
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
- [575. Distribute Candies](../../0501-1000/0575-distribute-candies/)
- [979. Distribute Coins in Binary Tree](../../0501-1000/0979-distribute-coins-in-binary-tree/)
- [1103. Distribute Candies to People](../../1001-1500/1103-distribute-candies-to-people/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distribute-repeating-integers/)
