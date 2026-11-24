# LeetCode 3312: Sorted GCD Pair Queries

**LeetCode Problem #3312 — Sorted GCD Pair Queries**
Solve LeetCode Sorted GCD Pair Queries using PHP and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sorted GCD Pair Queries |
| LeetCode | #3312 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer array `queries`.

Let `gcdPairs` denote an array obtained by calculating the GCD of all possible pairs `(nums[i], nums[j])`, where `0 <= i < j < n`, and then sorting these values in **ascending** order.

For each query `queries[i]`, you need to find the element at index `queries[i]` in `gcdPairs`.

Return an integer array `answer`, where `answer[i]` is the value at `gcdPairs[queries[i]]` for each query.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

## Constraints
- `2 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 5 * 10^4`
- `1 <= queries.length <= 10^5`
- `0 <= queries[i] < n * (n - 1) / 2`

## Examples
### Example 1
- **Input:** `nums = [2,3,4], queries = [0,2,2]`
- **Output:** `[1,2,2]`
- **Explanation:** `gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1]`. 

 After sorting in ascending order, `gcdPairs = [1, 1, 2]`. 

 So, the answer is `[gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2]`.

### Example 2
- **Input:** `nums = [4,4,2,1], queries = [5,3,1,0]`
- **Output:** `[4,2,1,1]`
- **Explanation:** `gcdPairs` sorted in ascending order is `[1, 1, 1, 2, 2, 4]`.

### Example 3
- **Input:** `nums = [2,2], queries = [0,0]`
- **Output:** `[2,2]`
- **Explanation:** `gcdPairs = [2]`.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sorted GCD Pair Queries**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,4], queries = [0,2,2]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,2]`.
4. **Verification:** `gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1]`. 

 After sorting in ascending order, `gcdPairs = [1, 1, 2]`. 

 So, the answer is `[gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @return Integer[]
     */
    function gcdValues($nums, $queries) {

        $n = count($nums);
        $maxVal = max($nums);

        // Frequency of each value
        $freq = array_fill(0, $maxVal + 1, 0);

        foreach ($nums as $x) {
            $freq[$x]++;
        }

        /*
         * exact[g] = number of pairs whose GCD is exactly g.
         *
         * We calculate from large gcd to small gcd.
         */
        $exact = array_fill(0, $maxVal + 1, 0);

        for ($g = $maxVal; $g >= 1; $g--) {

            // Number of elements divisible by g
            $count = 0;

            for ($x = $g; $x <= $maxVal; $x += $g) {
                $count += $freq[$x];
            }

            // Number of pairs whose GCD is a multiple of g
            $pairs = intdiv($count * ($count - 1), 2);

            /*
             * Remove pairs whose exact GCD is 2g, 3g, ...
             */
            for ($multiple = $g + $g; $multiple <= $maxVal; $multiple += $g) {
                $pairs -= $exact[$multiple];
            }

            $exact[$g] = $pairs;
        }

        /*
         * Prefix sums:
         *
         * prefix[g] = number of pairs with GCD <= g
         */
        $prefix = 0;

        for ($g = 1; $g <= $maxVal; $g++) {
            $prefix += $exact[$g];
            $exact[$g] = $prefix;
        }

        /*
         * For each query q, find the smallest g such that
         *
         * prefix[g] > q
         *
         * because queries use 0-based indexing.
         */
        $answer = [];

        foreach ($queries as $q) {

            $lo = 1;
            $hi = $maxVal;

            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);

                if ($exact[$mid] > $q) {
                    $hi = $mid;
                } else {
                    $lo = $mid + 1;
                }
            }

            $answer[] = $lo;
        }

        return $answer;
    }
}
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [4010. Maximize Pair Strength Using GCD](../../4001-4500/4371-maximize-pair-strength-using-gcd/)
- [1998. GCD Sort of an Array](../../2001-2500/2125-gcd-sort-of-an-array/)
- [2447. Number of Subarrays With GCD Equal to K](../../2501-3000/2546-number-of-subarrays-with-gcd-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sorted-gcd-pair-queries/)
