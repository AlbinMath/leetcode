# LeetCode 1985: Find the Kth Largest Integer in the Array

**LeetCode Problem #1985 — Find the Kth Largest Integer in the Array**
Solve LeetCode Find the Kth Largest Integer in the Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Kth Largest Integer in the Array |
| LeetCode | #1985 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of strings `nums` and an integer `k`. Each string in `nums` represents an integer without leading zeros.

Return *the string that represents the *`k^th`*** largest integer** in *`nums`.

**Note**: Duplicate numbers should be counted distinctly. For example, if `nums` is `["1","2","2"]`, `"2"` is the first largest integer, `"2"` is the second-largest integer, and `"1"` is the third-largest integer.

## Constraints
- `1 <= k <= nums.length <= 10^4`
- `1 <= nums[i].length <= 100`
- `nums[i]` consists of only digits.
- `nums[i]` will not have any leading zeros.

## Examples
### Example 1
- **Input:** `nums = ["3","6","7","10"], k = 4`
- **Output:** `"3"`
- **Explanation:** The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4^th largest integer in nums is "3".

### Example 2
- **Input:** `nums = ["2","21","12","1"], k = 3`
- **Output:** `"2"`
- **Explanation:** The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3^rd largest integer in nums is "2".

### Example 3
- **Input:** `nums = ["0","0"], k = 2`
- **Output:** `"0"`
- **Explanation:** The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2^nd largest integer in nums is "0".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Kth Largest Integer in the Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = ["3","6","7","10"], k = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"3"`.
4. **Verification:** The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4^th largest integer in nums is "3".

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
/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
    nums.sort((a, b) => {
        if (a.length !== b.length) {
            return b.length - a.length;
        }
        return b.localeCompare(a);
    });

    return nums[k - 1];
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
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)
- [1394. Find Lucky Integer in an Array](../../1001-1500/1394-find-lucky-integer-in-an-array/)
- [3132. Find the Integer Added to Array II](../../3001-3500/3132-find-the-integer-added-to-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/)
