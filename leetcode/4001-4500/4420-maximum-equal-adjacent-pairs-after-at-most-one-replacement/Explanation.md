# LeetCode 4066: Maximum Equal Adjacent Pairs After at Most One Replacement

**LeetCode Problem #4066 — Maximum Equal Adjacent Pairs After at Most One Replacement**
Solve LeetCode Maximum Equal Adjacent Pairs After at Most One Replacement using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Equal Adjacent Pairs After at Most One Replacement |
| LeetCode | #4066 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **1-indexed** integer array `nums`.

You can choose two **distinct** values `x` and `y` and perform the following operation **at most** once:

Replace every occurrence of `x` in `nums` with `y`.

Return the **maximum** possible number of pairs of adjacent elements that are equal after performing the operation.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,2]`
- **Output:** `2`
- **Explanation:** One optimal solution is to choose `x = 3` and `y = 2`. 
 The resulting array is `[1, 2, 2, 2]`. 
 There are 2 pairs of adjacent elements that are equal: `(nums[2], nums[3])` and `(nums[3], nums[4])`. 
 Therefore, the answer is 2.

### Example 2
- **Input:** `nums = [1,2,1,2,1]`
- **Output:** `4`
- **Explanation:** One optimal solution is to choose `x = 1` and `y = 2`. 
 The resulting array is `[2, 2, 2, 2, 2]`. 
 There are 4 pairs of adjacent elements that are equal: `(nums[1], nums[2])`, `(nums[2], nums[3])`, `(nums[3], nums[4])`, and `(nums[4], nums[5])`. 
 Therefore, the answer is 4.

### Example 3
- **Input:** `nums = [1,1,1]`
- **Output:** `2`
- **Explanation:** One optimal solution is to perform no operation. 
 Thus, the resulting array is `[1, 1, 1]`. 
 There are 2 pairs of adjacent elements that are equal: `(nums[1], nums[2])` and `(nums[2], nums[3])`. 
 Therefore, the answer is 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Equal Adjacent Pairs After at Most One Replacement**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One optimal solution is to choose `x = 3` and `y = 2`. 
 The resulting array is `[1, 2, 2, 2]`. 
 There are 2 pairs of adjacent elements that are equal: `(nums[2], nums[3])` and `(nums[3], nums[4])`. 
 Therefore, the answer is 2.

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
var maxEqualAdjacentPairs = function(nums) {
    let map = new Map();
    let ans = 0;
    let maxCount = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        let x = nums[i];
        let y = nums[i + 1];

        if (x === y) {
            ans++;
        } else {
            let key = `${Math.min(x, y)},${Math.max(x, y)}`;

            let freq = (map.get(key) || 0) + 1;
            map.set(key, freq);

            maxCount = Math.max(maxCount, freq);
        }
    }

    return ans + maxCount;
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
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2229-maximum-fruits-harvested-after-at-most-k-steps/)
- [3830. Longest Alternating Subarray After Removing At Most One Element](../../4001-4500/4198-longest-alternating-subarray-after-removing-at-most-one-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-equal-adjacent-pairs-after-at-most-one-replacement/)
