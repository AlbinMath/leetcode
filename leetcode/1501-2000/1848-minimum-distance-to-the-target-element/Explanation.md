# LeetCode 1848: Minimum Distance to the Target Element

**LeetCode Problem #1848 — Minimum Distance to the Target Element**
Solve LeetCode Minimum Distance to the Target Element using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Distance to the Target Element |
| LeetCode | #1848 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` **(0-indexed)** and two integers `target` and `start`, find an index `i` such that `nums[i] == target` and `abs(i - start)` is **minimized**. Note that `abs(x)` is the absolute value of `x`.

Return `abs(i - start)`.

It is **guaranteed** that `target` exists in `nums`.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
- `0 <= start < nums.length`
- `target` is in `nums`.

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5], target = 5, start = 3`
- **Output:** `1`
- **Explanation:** nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

### Example 2
- **Input:** `nums = [1], target = 1, start = 0`
- **Output:** `0`
- **Explanation:** nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.

### Example 3
- **Input:** `nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0`
- **Output:** `0`
- **Explanation:** Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Distance to the Target Element**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5], target = 5, start = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

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
    int getMinDistance(vector<int>& nums, int target, int start) {
        int minDistance = INT_MAX;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                minDistance = min(minDistance, abs(i - start));
            }
        }

        return minDistance;
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
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)
- [1320. Minimum Distance to Type a Word Using Two Fingers](../../1001-1500/1320-minimum-distance-to-type-a-word-using-two-fingers/)
- [2463. Minimum Total Distance Traveled](../../2001-2500/2463-minimum-total-distance-traveled/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-distance-to-the-target-element/)
