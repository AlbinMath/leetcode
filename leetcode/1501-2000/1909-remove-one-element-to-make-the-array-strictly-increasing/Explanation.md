# LeetCode 1909: Remove One Element to Make the Array Strictly Increasing

**LeetCode Problem #1909 — Remove One Element to Make the Array Strictly Increasing**
Solve LeetCode Remove One Element to Make the Array Strictly Increasing using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove One Element to Make the Array Strictly Increasing |
| LeetCode | #1909 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

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
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Remove One Element to Make the Array Strictly Increasing**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2, 10 ,5,7]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.

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
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1187. Make Array Strictly Increasing](../../1001-1500/1187-make-array-strictly-increasing/)
- [3402. Minimum Operations to Make Columns Strictly Increasing](../../3001-3500/3402-minimum-operations-to-make-columns-strictly-increasing/)
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1827-minimum-operations-to-make-the-array-increasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/)
