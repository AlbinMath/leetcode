# LeetCode 3395: Subsequences with a Unique Middle Mode I

**LeetCode Problem #3395 — Subsequences with a Unique Middle Mode I**
Solve LeetCode Subsequences with a Unique Middle Mode I using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subsequences with a Unique Middle Mode I |
| LeetCode | #3395 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums`, find the number of subsequences of size 5 of `nums` with a **unique middle mode**.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **mode** of a sequence of numbers is defined as the element that appears the **maximum** number of times in the sequence.

A sequence of numbers contains a** unique mode** if it has only one mode.

A sequence of numbers `seq` of size 5 contains a **unique middle mode** if the *middle element* (`seq[2]`) is a **unique mode**.

## Constraints
- `5 <= nums.length <= 1000`
- ` -10^9 <= nums[i] <= 10^9 `

## Examples
### Example 1
- **Input:** `nums = [1,1,1,1,1,1]`
- **Output:** `6`
- **Explanation:** `[1, 1, 1, 1, 1]` is the only subsequence of size 5 that can be formed, and it has a unique middle mode of 1. This subsequence can be formed in 6 different ways, so the output is 6.

### Example 2
- **Input:** `nums = [1,2,2,3,3,4]`
- **Output:** `4`
- **Explanation:** `[1, 2, 2, 3, 4]` and `[1, 2, 3, 3, 4]` each have a unique middle mode because the number at index 2 has the greatest frequency in the subsequence. `[1, 2, 2, 3, 3]` does not have a unique middle mode because 2 and 3 appear twice.

### Example 3
- **Input:** `nums = [0,1,2,3,4,5,6,7,8]`
- **Output:** `0`
- **Explanation:** There is no subsequence of length 5 with a unique middle mode.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Subsequences with a Unique Middle Mode I**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,1,1,1,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** `[1, 1, 1, 1, 1]` is the only subsequence of size 5 that can be formed, and it has a unique middle mode of 1. This subsequence can be formed in 6 different ways, so the output is 6.

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
var subsequencesWithMiddleMode = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;

    const C2 = a => a * (a - 1) / 2;
    const C = (a, b) => {
        if (b < 0 || b > a || a < 0) return 0;
        if (b === 0) return 1;
        if (b === 1) return a;
        if (b === 2) return C2(a);
        return a * (a - 1) * (a - 2) / 6;
    };

    const left = new Map();
    const right = new Map();

    for (const v of nums) {
        right.set(v, (right.get(v) || 0) + 1);
    }

    let ans = 0;

    for (let mid = 0; mid < n; mid++) {
        const x = nums[mid];

        right.set(x, right.get(x) - 1);
        if (right.get(x) === 0) right.delete(x);

        const L = mid;
        const R = n - mid - 1;
        const lx = left.get(x) || 0;
        const rx = right.get(x) || 0;

        if (L >= 2 && R >= 2) {
            const ol = L - lx;
            const or = R - rx;

            // Case 1: x appears at least 3 times.
            let ways = 0;

            for (let i = 0; i <= 2; i++) {
                for (let j = 0; j <= 2; j++) {
                    if (i + j < 2) continue;

                    ways += C(lx, i) * C(ol, 2 - i)
                          * C(rx, j) * C(or, 2 - j);
                }
            }

            // Case 2: x appears exactly twice.
            // x is selected once from the left, or once from the right.
            let dupL = 0;
            let dupR = 0;

            for (const [v, count] of left) {
                if (v !== x) dupL += C2(count);
            }
            for (const [v, count] of right) {
                if (v !== x) dupR += C2(count);
            }

            // One x from the left, then one distinct left value
            // and two distinct right values, all mutually distinct.
            for (const [v, lv] of left) {
                if (v === x) continue;
                const rv = right.get(v) || 0;
                const validRightPairs =
                    C2(or) - dupR - rv * (or - rv);

                ways += lx * lv * validRightPairs;
            }

            // One x from the right, then two distinct left values
            // and one distinct right value, all mutually distinct.
            for (const [v, rv] of right) {
                if (v === x) continue;
                const lv = left.get(v) || 0;
                const validLeftPairs =
                    C2(ol) - dupL - lv * (ol - lv);

                ways += rx * rv * validLeftPairs;
            }

            ans = ((ans + ways) % MOD + MOD) % MOD;
        }

        left.set(x, (left.get(x) || 0) + 1);
    }

    return ans;
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
- [1930. Unique Length-3 Palindromic Subsequences](../../2001-2500/2059-unique-length-3-palindromic-subsequences/)
- [1987. Number of Unique Good Subsequences](../../2001-2500/2115-number-of-unique-good-subsequences/)
- [876. Middle of the Linked List](../../0501-1000/0908-middle-of-the-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/)
