# LeetCode 1909: Remove One Element to Make the Array Strictly Increasing

**LeetCode Problem #1909 — Remove One Element to Make the Array Strictly Increasing**
Solve LeetCode Remove One Element to Make the Array Strictly Increasing using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove One Element to Make the Array Strictly Increasing |
| LeetCode | #1909 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **0-indexed** integer array `nums`, return `true` *if it can be made **strictly increasing** after removing **exactly one** element, or *`false`* otherwise. If the array is already strictly increasing, return *`true`.

The array `nums` is **strictly increasing** if `nums[i - 1] < nums[i]` for each index `(1 <= i < nums.length).`

## Constraints
- `2 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2, 10 ,5,7]`
- **Output:** `true`
- **Explanation:** By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.

### Example 2
- **Input:** `nums = [2,3,1,2]`
- **Output:** `false`
- **Explanation:** [3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.

### Example 3
- **Input:** `nums = [1,1,1]`
- **Output:** `false`
- **Explanation:** The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove One Element to Make the Array Strictly Increasing**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2, 10 ,5,7]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        int n = nums.size();

        for (int i = 1; i < n; i++) {
            if (nums[i] <= nums[i - 1]) {
                vector<int> a = nums;
                vector<int> b = nums;

                a.erase(a.begin() + i - 1);
                b.erase(b.begin() + i);

                return isIncreasing(a) || isIncreasing(b);
            }
        }

        return true;
    }

    bool isIncreasing(vector<int>& nums) {
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] <= nums[i - 1]) {
                return false;
            }
        }

        return true;
    }
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
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1827-minimum-operations-to-make-the-array-increasing/)
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3191-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)
- [1636. Sort Array by Increasing Frequency](../../1501-2000/1636-sort-array-by-increasing-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/)
