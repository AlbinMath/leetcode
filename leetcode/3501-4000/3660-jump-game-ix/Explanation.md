# LeetCode 3660: Jump Game IX

**LeetCode Problem #3660 — Jump Game IX**
Solve LeetCode Jump Game IX using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game IX |
| LeetCode | #3660 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

From any index `i`, you can jump to another index `j` under the following rules:

Jump to index `j` where `j > i` is allowed only if `nums[j] < nums[i]`. 
 Jump to index `j` where `j < i` is allowed only if `nums[j] > nums[i]`.

For each index `i`, find the **maximum** **value** in `nums` that can be reached by following **any** sequence of valid jumps starting at `i`.

Return an array `ans` where `ans[i]` is the **maximum** **value** reachable starting from index `i`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9​​​​​​​`

## Examples
### Example 1
- **Input:** `nums = [2,1,3]`
- **Output:** `[2,2,3]`
- **Explanation:** For `i = 0`: No jump increases the value. 
 For `i = 1`: Jump to `j = 0` as `nums[j] = 2` is greater than `nums[i]`. 
 For `i = 2`: Since `nums[2] = 3` is the maximum value in `nums`, no jump increases the value. 
 

 Thus, `ans = [2, 2, 3]`.

### Example 2
- **Input:** `nums = [2,3,1]`
- **Output:** `[3,3,3]`
- **Explanation:** For `i = 0`: Jump forward to `j = 2` as `nums[j] = 1` is less than `nums[i] = 2`, then from `i = 2` jump to `j = 1` as `nums[j] = 3` is greater than `nums[2]`. 
 For `i = 1`: Since `nums[1] = 3` is the maximum value in `nums`, no jump increases the value. 
 For `i = 2`: Jump to `j = 1` as `nums[j] = 3` is greater than `nums[2] = 1`. 
 

 Thus, `ans = [3, 3, 3]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Jump Game IX**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,2,3]`.
4. **Verification:** For `i = 0`: No jump increases the value. 
 For `i = 1`: Jump to `j = 0` as `nums[j] = 2` is greater than `nums[i]`. 
 For `i = 2`: Since `nums[2] = 3` is the maximum value in `nums`, no jump increases the value. 
 

 Thus, `ans = [2, 2, 3]`.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();

        vector<int> ans(n);
        vector<int> preMax(n);

        // Prefix maximum
        preMax[0] = nums[0];

        for (int i = 1; i < n; i++) {
            preMax[i] = max(preMax[i - 1], nums[i]);
        }

        // Traverse from right to left
        int sufMin = INT_MAX;

        for (int i = n - 1; i >= 0; i--) {
            if (i == n - 1 || preMax[i] <= sufMin) {
                ans[i] = preMax[i];
            } else {
                ans[i] = ans[i + 1];
            }

            // Important: update AFTER processing i
            sufMin = min(sufMin, nums[i]);
        }

        return ans;
    }
};
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
- [2029. Stone Game IX](../../2001-2500/2029-stone-game-ix/)
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-ix/)
