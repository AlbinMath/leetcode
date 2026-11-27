# LeetCode 3501: Maximize Active Section with Trade II

**LeetCode Problem #3501 — Maximize Active Section with Trade II**
Solve LeetCode Maximize Active Section with Trade II using PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Active Section with Trade II |
| LeetCode | #3501 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary string `s` of length `n`, where:

`'1'` represents an **active** section. 
 `'0'` represents an **inactive** section.

You can perform **at most one trade** to maximize the number of active sections in `s`. In a trade, you:

Convert a contiguous block of `'1'`s that is surrounded by `'0'`s to all `'0'`s. 
 Afterward, convert a contiguous block of `'0'`s that is surrounded by `'1'`s to all `'1'`s.

Additionally, you are given a **2D array** `queries`, where `queries[i] = [l_i, r_i]` represents a substring `s[l_i...r_i]`.

For each query, determine the **maximum** possible number of active sections in `s` after making the optimal trade on the substring `s[l_i...r_i]`.

Return an array `answer`, where `answer[i]` is the result for `queries[i]`.

**Note**

For each query, treat `s[l_i...r_i]` as if it is **augmented** with a `'1'` at both ends, forming `t = '1' + s[l_i...r_i] + '1'`. The augmented `'1'`s **do not** contribute to the final count. 
 The queries are independent of each other.

## Constraints
- `1 <= n == s.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.
- `queries[i] = [l_i, r_i]`
- `0 <= l_i <= r_i < n`

## Examples
### Example 1
- **Input:** `s = "01", queries = [[0,1]]`
- **Output:** `[1]`
- **Explanation:** Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 1.

### Example 2
- **Input:** `s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]`
- **Output:** `[4,3,1,1]`
- **Explanation:** Query `[0, 3]` &rarr; Substring `"0100"` &rarr; Augmented to `"101001"` 
 Choose `"0100"`, convert `"0100"` &rarr; `"0000"` &rarr; `"1111"`. 
 The final string without augmentation is `"1111"`. The maximum number of active sections is 4. 
 
 
 Query `[0, 2]` &rarr; Substring `"010"` &rarr; Augmented to `"10101"` 
 Choose `"010"`, convert `"010"` &rarr; `"000"` &rarr; `"111"`. 
 The final string without augmentation is `"1110"`. The maximum number of active sections is 3. 
 
 
 Query `[1, 3]` &rarr; Substring `"100"` &rarr; Augmented to `"11001"` 
 Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 1. 
 
 
 Query `[2, 3]` &rarr; Substring `"00"` &rarr; Augmented to `"1001"` 
 Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 1.

### Example 3
- **Input:** `s = "1000100", queries = [[1,5],[0,6],[0,4]]`
- **Output:** `[6,7,2]`
- **Explanation:** Query `[1, 5]` &rarr; Substring "00010" &rarr; Augmented to "1000101" 
 Choose "00010" , convert "00010" &rarr; "00000" &rarr; "11111" . 
 The final string without augmentation is "1111110" . The maximum number of active sections is 6. 
 
 
 Query `[0, 6]` &rarr; Substring "1000100" &rarr; Augmented to "110001001" 
 Choose "000100" , convert "000100" &rarr; "000000" &rarr; "111111" . 
 The final string without augmentation is "1111111" . The maximum number of active sections is 7. 
 
 
 Query `[0, 4]` &rarr; Substring "10001" &rarr; Augmented to "1100011" 
 Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 2.

### Example 4
- **Input:** `s = "01010", queries = [[0,3],[1,4],[1,3]]`
- **Output:** `[4,4,2]`
- **Explanation:** Query `[0, 3]` &rarr; Substring `"0101"` &rarr; Augmented to `"101011"` 
 Choose `"010"`, convert `"010"` &rarr; `"000"` &rarr; `"111"`. 
 The final string without augmentation is `"11110"`. The maximum number of active sections is 4. 
 
 
 Query `[1, 4]` &rarr; Substring `"1010"` &rarr; Augmented to `"110101"` 
 Choose `"010"`, convert `"010"` &rarr; `"000"` &rarr; `"111"`. 
 The final string without augmentation is `"01111"`. The maximum number of active sections is 4. 
 
 
 Query `[1, 3]` &rarr; Substring `"101"` &rarr; Augmented to `"11011"` 
 Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 2.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximize Active Section with Trade II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "01", queries = [[0,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1]`.
4. **Verification:** Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 1.

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
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maxActiveSectionsAfterTrade($s, $queries) {
        $n = strlen($s);
        $ones = substr_count($s, '1');

        // [start, length] for every zero group
        $zeroGroups = [];

        // For every position, store the index of the latest zero group.
        $zeroGroupIndex = array_fill(0, $n, -1);

        for ($i = 0; $i < $n; $i++) {

            if ($s[$i] === '0') {
                if ($i > 0 && $s[$i - 1] === '0') {
                    $idx = count($zeroGroups) - 1;
                    $zeroGroups[$idx][1]++;
                } else {
                    $zeroGroups[] = [$i, 1];
                }
            }

            // IMPORTANT:
            // Even if s[i] == '1', keep the latest zero-group index.
            $zeroGroupIndex[$i] = count($zeroGroups) - 1;
        }

        $g = count($zeroGroups);

        // Need at least two zero groups to perform a trade.
        if ($g < 2) {
            return array_fill(0, count($queries), $ones);
        }

        /*
         * merge[i] = size of zero group i + zero group i+1
         *
         * Choosing the 1-block between these two zero groups
         * allows the two zero groups to be merged and then
         * converted into 1s.
         */
        $merge = [];

        for ($i = 0; $i < $g - 1; $i++) {
            $merge[$i] =
                $zeroGroups[$i][1] +
                $zeroGroups[$i + 1][1];
        }

        /*
         * Sparse table for range maximum query.
         */
        $m = count($merge);

        $log = array_fill(0, $m + 1, 0);

        for ($i = 2; $i <= $m; $i++) {
            $log[$i] = $log[intdiv($i, 2)] + 1;
        }

        $K = $log[$m] + 1;

        $st = array_fill(0, $K, []);
        $st[0] = $merge;

        for ($k = 1; $k < $K; $k++) {
            $len = 1 << $k;
            $half = $len >> 1;
            $limit = $m - $len + 1;

            $row = [];

            for ($i = 0; $i < $limit; $i++) {
                $row[$i] = max(
                    $st[$k - 1][$i],
                    $st[$k - 1][$i + $half]
                );
            }

            $st[$k] = $row;
        }

        // Range maximum query on merge[]
        $rangeMax = function ($l, $r) use (&$st, &$log) {
            if ($l > $r) {
                return 0;
            }

            $len = $r - $l + 1;
            $k = $log[$len];
            $block = 1 << $k;

            return max(
                $st[$k][$l],
                $st[$k][$r - $block + 1]
            );
        };

        $answer = [];

        foreach ($queries as $query) {

            $l = $query[0];
            $r = $query[1];

            // No trade
            $best = $ones;

            $leftGroup = $zeroGroupIndex[$l];
            $rightGroup = $zeroGroupIndex[$r];

            /*
             * Portion of the left zero group inside [l, r].
             */
            $left = -1;

            if ($leftGroup !== -1) {
                $start = $zeroGroups[$leftGroup][0];
                $length = $zeroGroups[$leftGroup][1];

                $left = $length - ($l - $start);
            }

            /*
             * Portion of the right zero group inside [l, r].
             */
            $right = -1;

            if ($rightGroup !== -1) {
                $start = $zeroGroups[$rightGroup][0];

                $right = $r - $start + 1;
            }

            /*
             * Determine zero-group pairs completely usable
             * inside the query.
             */
            $startGroup = $leftGroup + 1;

            $endGroup = ($s[$r] === '1')
                ? $rightGroup
                : $rightGroup - 1;

            /*
             * Case 1:
             * Query begins and ends inside zero groups,
             * and those are adjacent zero groups.
             */
            if (
                $s[$l] === '0' &&
                $s[$r] === '0' &&
                $leftGroup + 1 === $rightGroup
            ) {
                $best = max(
                    $best,
                    $ones + $left + $right
                );
            }

            /*
             * Case 2:
             * Choose any completely contained pair of zero groups.
             */
            else {
                $mergeL = $startGroup;
                $mergeR = $endGroup - 1;

                if ($mergeL <= $mergeR) {
                    $best = max(
                        $best,
                        $ones + $rangeMax($mergeL, $mergeR)
                    );
                }
            }

            /*
             * Case 3:
             * Use the left partial zero group together
             * with the next complete zero group.
             */
            if (
                $s[$l] === '0' &&
                $leftGroup + 1 <=
                (($s[$r] === '1')
                    ? $rightGroup
                    : $rightGroup - 1)
            ) {
                $best = max(
                    $best,
                    $ones +
                    $left +
                    $zeroGroups[$leftGroup + 1][1]
                );
            }

            /*
             * Case 4:
             * Use the right partial zero group together
             * with the previous complete zero group.
             */
            if (
                $s[$r] === '0' &&
                $leftGroup < $rightGroup - 1
            ) {
                $best = max(
                    $best,
                    $ones +
                    $right +
                    $zeroGroups[$rightGroup - 1][1]
                );
            }

            $answer[] = $best;
        }

        return $answer;
    }
}
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
- [3499. Maximize Active Section with Trade I](../../3001-3500/3499-maximize-active-section-with-trade-i/)
- [1817. Finding the Users Active Minutes](../../1501-2000/1817-finding-the-users-active-minutes/)
- [849. Maximize Distance to Closest Person](../../0501-1000/0849-maximize-distance-to-closest-person/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-active-section-with-trade-ii/)
