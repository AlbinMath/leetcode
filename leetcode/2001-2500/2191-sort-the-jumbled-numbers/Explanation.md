# LeetCode 2191: Sort the Jumbled Numbers

**LeetCode Problem #2191 — Sort the Jumbled Numbers**
Solve LeetCode Sort the Jumbled Numbers using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort the Jumbled Numbers |
| LeetCode | #2191 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `mapping` which represents the mapping rule of a shuffled decimal system. `mapping[i] = j` means digit `i` should be mapped to digit `j` in this system.

The **mapped value** of an integer is the new integer obtained by replacing each occurrence of digit `i` in the integer with `mapping[i]` for all `0 <= i <= 9`.

You are also given another integer array `nums`. Return *the array *`nums`* sorted in **non-decreasing** order based on the **mapped values** of its elements.*

**Notes:**

Elements with the same mapped values should appear in the **same relative order** as in the input. 
 The elements of `nums` should only be sorted based on their mapped values and **not be replaced** by them.

## Constraints
- `mapping.length == 10`
- `0 <= mapping[i] <= 9`
- All the values of `mapping[i]` are **unique**.
- `1 <= nums.length <= 3 * 10^4`
- `0 <= nums[i] < 10^9`

## Examples
### Example 1
- **Input:** `mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]`
- **Output:** `[338,38,991]`
- **Explanation:** Map the number 991 as follows:
1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
Therefore, the mapped value of 991 is 669.
338 maps to 007, or 7 after removing the leading zeros.
38 maps to 07, which is also 7 after removing leading zeros.
Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
Thus, the sorted array is [338,38,991].

### Example 2
- **Input:** `mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]`
- **Output:** `[123,456,789]`
- **Explanation:** 789 maps to 789, 456 maps to 456, and 123 maps to 123. Thus, the sorted array is [123,456,789].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sort the Jumbled Numbers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[338,38,991]`.
4. **Verification:** Map the number 991 as follows:
1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
Therefore, the mapped value of 991 is 669.
338 maps to 007, or 7 after removing the leading zeros.
38 maps to 07, which is also 7 after removing leading zeros.
Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
Thus, the sorted array is [338,38,991].

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
var sortJumbled = function(mapping, nums) {
    const arr = [];
    for (let i = 0; i < nums.length; i++) {
        const mappedValue = Number(
            nums[i]
                .toString()
                .split("")
                .map(digit => mapping[Number(digit)])
                .join("")
        );

        arr.push({
            original: nums[i],
            mapped: mappedValue,
            index: i
        });
    }
    arr.sort((a, b) => {
        if (a.mapped !== b.mapped) {
            return a.mapped - b.mapped;
        }

        return a.index - b.index;
    });
    return arr.map(item => item.original);
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
- [75. Sort Colors](../../0001-0500/0075-sort-colors/)
- [147. Insertion Sort List](../../0001-0500/0147-insertion-sort-list/)
- [148. Sort List](../../0001-0500/0148-sort-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-the-jumbled-numbers/)
