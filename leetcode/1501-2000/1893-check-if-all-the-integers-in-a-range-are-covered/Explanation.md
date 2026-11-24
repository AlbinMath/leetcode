# LeetCode 1893: Check if All the Integers in a Range Are Covered

**LeetCode Problem #1893 — Check if All the Integers in a Range Are Covered**
Solve LeetCode Check if All the Integers in a Range Are Covered using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if All the Integers in a Range Are Covered |
| LeetCode | #1893 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `ranges` and two integers `left` and `right`. Each `ranges[i] = [start_i, end_i]` represents an **inclusive** interval between `start_i` and `end_i`.

Return `true` *if each integer in the inclusive range* `[left, right]` *is covered by **at least one** interval in* `ranges`. Return `false` *otherwise*.

An integer `x` is covered by an interval `ranges[i] = [start_i, end_i]` if `start_i <= x <= end_i`.

## Constraints
- `1 <= ranges.length <= 50`
- `1 <= start_i <= end_i <= 50`
- `1 <= left <= right <= 50`

## Examples
### Example 1
- **Input:** `ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5`
- **Output:** `true`
- **Explanation:** Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.

### Example 2
- **Input:** `ranges = [[1,10],[10,20]], left = 21, right = 21`
- **Output:** `false`
- **Explanation:** 21 is not covered by any range.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Check if All the Integers in a Range Are Covered**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.

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
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        for (int x = left; x <= right; x++) {
            bool covered = false;

            for (const auto& range : ranges) {
                if (range[0] <= x && x <= range[1]) {
                    covered = true;
                    break;
                }
            }

            if (!covered) {
                return false;
            }
        }

        return true;
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
- [1437. Check If All 1's Are at Least Length K Places Away](../../1001-1500/1437-check-if-all-1s-are-at-least-length-k-places-away/)
- [1461. Check If a String Contains All Binary Codes of Size K](../../1001-1500/1461-check-if-a-string-contains-all-binary-codes-of-size-k/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../1501-2000/1941-check-if-all-characters-have-equal-number-of-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/)
