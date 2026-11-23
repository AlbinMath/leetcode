# LeetCode 1619: Mean of Array After Removing Some Elements

**LeetCode Problem #1619 — Mean of Array After Removing Some Elements**
Solve LeetCode Mean of Array After Removing Some Elements using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Mean of Array After Removing Some Elements |
| LeetCode | #1619 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr`, return *the mean of the remaining integers after removing the smallest `5%` and the largest `5%` of the elements.*

Answers within `10^-5` of the **actual answer** will be considered accepted.

## Constraints
- `20 <= arr.length <= 1000`
- `arr.length` **is a multiple** of `20`.
- ` 0 <= arr[i] <= 10^5 `

## Examples
### Example 1
- **Input:** `arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]`
- **Output:** `2.00000`
- **Explanation:** After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.

### Example 2
- **Input:** `arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]`
- **Output:** `4.00000`

### Example 3
- **Input:** `arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]`
- **Output:** `4.77778`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Mean of Array After Removing Some Elements**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2.00000`.
4. **Verification:** After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.

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
    double trimMean(vector<int>& arr) {
        sort(arr.begin(), arr.end());

        int n = arr.size();
        int remove = n / 20;

        double sum = 0;

        for (int i = remove; i < n - remove; i++) {
            sum += arr[i];
        }

        return sum / (n - 2 * remove);
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
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2695-find-score-of-an-array-after-marking-all-elements/)
- [3041. Maximize Consecutive Elements in an Array After Modification](../../3001-3500/3298-maximize-consecutive-elements-in-an-array-after-modification/)
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2212-removing-minimum-and-maximum-from-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/mean-of-array-after-removing-some-elements/)
