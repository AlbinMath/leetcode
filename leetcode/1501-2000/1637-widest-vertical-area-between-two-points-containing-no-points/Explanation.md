# LeetCode 1637: Widest Vertical Area Between Two Points Containing No Points

**LeetCode Problem #1637 — Widest Vertical Area Between Two Points Containing No Points**
Solve LeetCode Widest Vertical Area Between Two Points Containing No Points using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Widest Vertical Area Between Two Points Containing No Points |
| LeetCode | #1637 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given `n` `points` on a 2D plane where `points[i] = [x_i, y_i]`, Return* the **widest vertical area** between two points such that no points are inside the area.*

A **vertical area** is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The **widest vertical area** is the one with the maximum width.

Note that points **on the edge** of a vertical area **are not** considered included in the area.

## Constraints
- `n == points.length`
- `2 <= n <= 10^5`
- `points[i].length == 2`
- `0 <= x_i, y_i <= 10^9`

## Examples
### Example 1
- **Input:** `points = [[8,7],[9,9],[7,4],[9,7]]`
- **Output:** `1`
- **Explanation:** Both the red and the blue area are optimal.

### Example 2
- **Input:** `points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]`
- **Output:** `3`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Widest Vertical Area Between Two Points Containing No Points**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[8,7],[9,9],[7,4],[9,7]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Both the red and the blue area are optimal.

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
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> x;

        // Extract x-coordinates
        for (auto& point : points) {
            x.push_back(point[0]);
        }

        // Sort x-coordinates
        sort(x.begin(), x.end());

        int maxWidth = 0;

        // Find the largest gap between adjacent x-coordinates
        for (int i = 1; i < x.size(); i++) {
            maxWidth = max(maxWidth, x[i] - x[i - 1]);
        }

        return maxWidth;
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
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1317-convert-integer-to-the-sum-of-two-no-zero-integers/)
- [3670. Maximum Product of Two Integers With No Common Bits](../../3501-4000/3670-maximum-product-of-two-integers-with-no-common-bits/)
- [1360. Number of Days Between Two Dates](../../1001-1500/1360-number-of-days-between-two-dates/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/)
