# LeetCode 2811: Check if it is Possible to Split Array

**LeetCode Problem #2811 — Check if it is Possible to Split Array**
Solve LeetCode Check if it is Possible to Split Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if it is Possible to Split Array |
| LeetCode | #2811 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` of length `n` and an integer `m`. You need to determine if it is possible to split the array into `n` arrays of size 1 by performing a series of steps.

An array is called **good** if:

The length of the array is **one**, or 
 The sum of the elements of the array is **greater than or equal** to `m`.

In each step, you can select an existing array (which may be the result of previous steps) with a length of **at least two** and split it into **two **arrays, if both resulting arrays are good.

Return true if you can split the given array into `n` arrays, otherwise return false.

## Constraints
- `1 <= n == nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= m <= 200`

## Examples
### Example 1
- **Input:** `nums = [2, 2, 1], m = 4`
- **Output:** `true`
- **Explanation:** Split `[2, 2, 1]` to `[2, 2]` and `[1]`. The array `[1]` has a length of one, and the array `[2, 2]` has the sum of its elements equal to `4 >= m`, so both are good arrays. 
 Split `[2, 2]` to `[2]` and `[2]`. both arrays have the length of one, so both are good arrays.

### Example 2
- **Input:** `nums = [2, 1, 3], m = 5`
- **Output:** `false`
- **Explanation:** The first move has to be either of the following: 

 
 Split `[2, 1, 3]` to `[2, 1]` and `[3]`. The array `[2, 1]` has neither length of one nor sum of elements greater than or equal to `m`. 
 Split `[2, 1, 3]` to `[2]` and `[1, 3]`. The array `[1, 3]` has neither length of one nor sum of elements greater than or equal to `m`. 
 

 So as both moves are invalid (they do not divide the array into two good arrays), we are unable to split `nums` into `n` arrays of size 1.

### Example 3
- **Input:** `nums = [2, 3, 3, 2, 3], m = 6`
- **Output:** `true`
- **Explanation:** Split `[2, 3, 3, 2, 3]` to `[2]` and `[3, 3, 2, 3]`. 
 Split `[3, 3, 2, 3]` to `[3, 3, 2]` and `[3]`. 
 Split `[3, 3, 2]` to `[3, 3]` and `[2]`. 
 Split `[3, 3]` to `[3]` and `[3]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if it is Possible to Split Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2, 2, 1], m = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Split `[2, 2, 1]` to `[2, 2]` and `[1]`. The array `[1]` has a length of one, and the array `[2, 2]` has the sum of its elements equal to `4 >= m`, so both are good arrays. 
 Split `[2, 2]` to `[2]` and `[2]`. both arrays have the length of one, so both are good arrays.

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
var canSplitArray = function(nums, m) {
    if (nums.length <= 2) return true;

    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] + nums[i + 1] >= m) {
            return true;
        }
    }

    return false;
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
- [1250. Check If It Is a Good Array](../../1001-1500/1250-check-if-it-is-a-good-array/)
- [1497. Check If Array Pairs Are Divisible by k](../../1001-1500/1497-check-if-array-pairs-are-divisible-by-k/)
- [1752. Check if Array Is Sorted and Rotated](../../1501-2000/1752-check-if-array-is-sorted-and-rotated/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-it-is-possible-to-split-array/)
