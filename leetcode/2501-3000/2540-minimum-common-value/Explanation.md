# LeetCode 2540: Minimum Common Value

**LeetCode Problem #2540 — Minimum Common Value**
Solve LeetCode Minimum Common Value using C++ and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Common Value |
| LeetCode | #2540 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return *the **minimum integer common** to both arrays*. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

Note that an integer is said to be **common** to `nums1` and `nums2` if both arrays have **at least one** occurrence of that integer.

## Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^9`
- Both `nums1` and `nums2` are sorted in **non-decreasing** order.

## Examples
### Example 1
- **Input:** `nums1 = [1,2,3], nums2 = [2,4]`
- **Output:** `2`
- **Explanation:** The smallest element common to both arrays is 2, so we return 2.

### Example 2
- **Input:** `nums1 = [1,2,3,6], nums2 = [2,3,4,5]`
- **Output:** `2`
- **Explanation:** There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
Use **two pointers**, one for each array. If values match, return it. Otherwise advance the pointer with the smaller value. If either pointer reaches the end, return -1. Time: $O(N + M)$, Space: $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,3], nums2 = [2,4]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The smallest element common to both arrays is 2, so we return 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i = 0, j = 0;

        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] == nums2[j])
                return nums1[i];

            if (nums1[i] < nums2[j])
                i++;
            else
                j++;
        }

        return -1;
    }
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1413. Minimum Value to Get Positive Step by Step Sum](../../1001-1500/1413-minimum-value-to-get-positive-step-by-step-sum/)
- [1896. Minimum Cost to Change the Final Value of Expression](../../1501-2000/1896-minimum-cost-to-change-the-final-value-of-expression/)
- [3066. Minimum Operations to Exceed Threshold Value II](../../3001-3500/3066-minimum-operations-to-exceed-threshold-value-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-common-value/)
