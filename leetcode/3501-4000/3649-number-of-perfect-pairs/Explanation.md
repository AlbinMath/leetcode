# LeetCode 3649: Number of Perfect Pairs

**LeetCode Problem #3649 — Number of Perfect Pairs**
Solve LeetCode Number of Perfect Pairs using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Perfect Pairs |
| LeetCode | #3649 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A pair of indices `(i, j)` is called **perfect** if the following conditions are satisfied:

`i < j` 
 Let `a = nums[i]`, `b = nums[j]`. Then:
 
 `min(|a - b|, |a + b|) <= min(|a|, |b|)` 
 `max(|a - b|, |a + b|) >= max(|a|, |b|)`

Return the number of **distinct** perfect pairs.

**Note:** The absolute value `|x|` refers to the **non-negative** value of `x`.

## Constraints
- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [0,1,2,3]`
- **Output:** `2`
- **Explanation:** There are 2 perfect pairs: 

 
 
 
 `(i, j)` 
 `(a, b)` 
 `min(|a &minus; b|, |a + b|)` 
 `min(|a|, |b|)` 
 `max(|a &minus; b|, |a + b|)` 
 `max(|a|, |b|)` 
 
 
 
 
 (1, 2) 
 (1, 2) 
 `min(|1 &minus; 2|, |1 + 2|) = 1` 
 1 
 `max(|1 &minus; 2|, |1 + 2|) = 3` 
 2 
 
 
 (2, 3) 
 (2, 3) 
 `min(|2 &minus; 3|, |2 + 3|) = 1` 
 2 
 `max(|2 &minus; 3|, |2 + 3|) = 5` 
 3

### Example 2
- **Input:** `nums = [-3,2,-1,4]`
- **Output:** `4`
- **Explanation:** There are 4 perfect pairs: 

 
 
 
 `(i, j)` 
 `(a, b)` 
 `min(|a &minus; b|, |a + b|)` 
 `min(|a|, |b|)` 
 `max(|a &minus; b|, |a + b|)` 
 `max(|a|, |b|)` 
 
 
 
 
 (0, 1) 
 (-3, 2) 
 `min(|-3 - 2|, |-3 + 2|) = 1` 
 2 
 `max(|-3 - 2|, |-3 + 2|) = 5` 
 3 
 
 
 (0, 3) 
 (-3, 4) 
 `min(|-3 - 4|, |-3 + 4|) = 1` 
 3 
 `max(|-3 - 4|, |-3 + 4|) = 7` 
 4 
 
 
 (1, 2) 
 (2, -1) 
 `min(|2 - (-1)|, |2 + (-1)|) = 1` 
 1 
 `max(|2 - (-1)|, |2 + (-1)|) = 3` 
 2 
 
 
 (1, 3) 
 (2, 4) 
 `min(|2 - 4|, |2 + 4|) = 2` 
 2 
 `max(|2 - 4|, |2 + 4|) = 6` 
 4

### Example 3
- **Input:** `nums = [1,10,100,1000]`
- **Output:** `0`
- **Explanation:** There are no perfect pairs. Thus, the answer is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Perfect Pairs**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are 2 perfect pairs: 

 
 
 
 `(i, j)` 
 `(a, b)` 
 `min(|a &minus; b|, |a + b|)` 
 `min(|a|, |b|)` 
 `max(|a &minus; b|, |a + b|)` 
 `max(|a|, |b|)` 
 
 
 
 
 (1, 2) 
 (1, 2) 
 `min(|1 &minus; 2|, |1 + 2|) = 1` 
 1 
 `max(|1 &minus; 2|, |1 + 2|) = 3` 
 2 
 
 
 (2, 3) 
 (2, 3) 
 `min(|2 &minus; 3|, |2 + 3|) = 1` 
 2 
 `max(|2 &minus; 3|, |2 + 3|) = 5` 
 3

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
var perfectPairs = function(nums) {
    const arr = nums.map(Math.abs).sort((a, b) => a - b);

    let count = 0;
    let left = 0;
    for (let right = 0; right < arr.length; right++) {
        while (arr[right] > 2 * arr[left]) {
            left++;
        }
        count += right - left;
    }

    return count;
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
- [507. Perfect Number](../../0501-1000/0507-perfect-number/)
- [1128. Number of Equivalent Domino Pairs](../../1001-1500/1128-number-of-equivalent-domino-pairs/)
- [1512. Number of Good Pairs](../../1501-2000/1512-number-of-good-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-perfect-pairs/)
