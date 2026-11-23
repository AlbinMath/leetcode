# LeetCode 3739: Count Subarrays With Majority Element II

**LeetCode Problem #3739 — Count Subarrays With Majority Element II**
Solve LeetCode Count Subarrays With Majority Element II using PHP and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays With Majority Element II |
| LeetCode | #3739 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `target`.

Return the number of ** subarrays ** of `nums` in which `target` is the **majority element**.

The **majority element** of a subarray is the element that appears **strictly more than half** of the times in that subarray.

## Constraints
- `1 <= nums.length <= 10^​​​​​​​5`
- `1 <= nums[i] <= 10^​​​​​​​9`
- `1 <= target <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,3], target = 2`
- **Output:** `5`
- **Explanation:** Valid subarrays with `target = 2` as the majority element: 

 
 `nums[1..1] = [2]` 
 `nums[2..2] = [2]` 
 `nums[1..2] = [2,2]` 
 `nums[0..2] = [1,2,2]` 
 `nums[1..3] = [2,2,3]` 
 

 So there are 5 such subarrays.

### Example 2
- **Input:** `nums = [1,1,1,1], target = 1`
- **Output:** `10`

### Example 3
- **Input:** `nums = [1,2,3], target = 4`
- **Output:** `0`
- **Explanation:** `target = 4` does not appear in `nums` at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Subarrays With Majority Element II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,3], target = 2`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Valid subarrays with `target = 2` as the majority element: 

 
 `nums[1..1] = [2]` 
 `nums[2..2] = [2]` 
 `nums[1..2] = [2,2]` 
 `nums[0..2] = [1,2,2]` 
 `nums[1..3] = [2,2,3]` 
 

 So there are 5 such subarrays.

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
     * @param Integer $target
     * @return Integer
     */
    function countMajoritySubarrays($nums, $target) {
        $n = count($nums);

        /*
         * Prefix sums can range from -n to n.
         * Shift by n so they become valid Fenwick indices.
         */
        $OFFSET = $n + 2;
        $SIZE = 2 * $n + 5;

        $bit = array_fill(0, $SIZE, 0);

        // Add a prefix sum to Fenwick tree.
        $add = function ($idx) use (&$bit, $SIZE) {
            while ($idx < $SIZE) {
                $bit[$idx]++;
                $idx += $idx & (-$idx);
            }
        };

        // Count prefix sums with index <= idx.
        $query = function ($idx) use (&$bit) {
            $sum = 0;

            while ($idx > 0) {
                $sum += $bit[$idx];
                $idx -= $idx & (-$idx);
            }

            return $sum;
        };

        /*
         * Empty prefix has sum 0.
         */
        $prefix = 0;
        $add($OFFSET);

        $answer = 0;

        foreach ($nums as $x) {

            if ($x == $target) {
                $prefix++;
            } else {
                $prefix--;
            }

            /*
             * Need previousPrefix < currentPrefix.
             *
             * Prefix sum p is stored at:
             * p + OFFSET
             *
             * So we query up to:
             * currentPrefix + OFFSET - 1
             */
            $index = $prefix + $OFFSET;

            $answer += $query($index - 1);

            // Store current prefix.
            $add($index);
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
- [3737. Count Subarrays With Majority Element I](../../4001-4500/4074-count-subarrays-with-majority-element-i/)
- [2962. Count Subarrays Where Max Element Appears at Least K Times](../../3001-3500/3213-count-subarrays-where-max-element-appears-at-least-k-times/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-ii/)
