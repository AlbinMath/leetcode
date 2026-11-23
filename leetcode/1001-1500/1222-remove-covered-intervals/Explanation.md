# LeetCode 1288: Remove Covered Intervals

**LeetCode Problem #1288 — Remove Covered Intervals**
Solve LeetCode Remove Covered Intervals using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Covered Intervals |
| LeetCode | #1288 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `intervals` where `intervals[i] = [l_i, r_i]` represent the interval `[l_i, r_i)`, remove all intervals that are covered by another interval in the list.

The interval `[a, b)` is covered by the interval `[c, d)` if and only if `c <= a` and `b <= d`.

Return *the number of remaining intervals*.

## Constraints
- `1 <= intervals.length <= 1000`
- `intervals[i].length == 2`
- `0 <= l_i < r_i <= 10^5`
- All the given intervals are **unique**.

## Examples
### Example 1
- **Input:** `intervals = [[1,4],[3,6],[2,8]]`
- **Output:** `2`
- **Explanation:** Interval [3,6] is covered by [2,8], therefore it is removed.

### Example 2
- **Input:** `intervals = [[1,4],[2,3]]`
- **Output:** `1`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Sorting + Greedy**.

1. **Sort:** Sort intervals by start ascending. If starts are equal, sort by end **descending**. This ensures that if two intervals share the same start, the longer one comes first.
2. **Iterate:** Track `maxEnd` — the maximum end value seen so far. For each interval:
   - If `interval[1] > maxEnd`: This interval is NOT covered (it extends beyond all previous intervals), so increment the `count` and update `maxEnd`.
   - Otherwise: This interval is covered by a previous one (its end is ≤ `maxEnd`), so skip it.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `intervals = [[1,4],[3,6],[2,8]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Interval [3,6] is covered by [2,8], therefore it is removed.

## Complexity Analysis
- **Time Complexity:** O(log n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.*;

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        // Sort by start ascending.
        // If starts are equal, sort end descending.
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(b[1], a[1]);
            }
            return Integer.compare(a[0], b[0]);
        });

        int count = 0;
        int maxEnd = 0;

        for (int[] interval : intervals) {
            // This interval is not covered
            if (interval[1] > maxEnd) {
                count++;
                maxEnd = interval[1];
            }
        }

        return count;
    }
}
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [1893. Check if All the Integers in a Range Are Covered](../../2001-2500/2005-check-if-all-the-integers-in-a-range-are-covered/)
- [2271. Maximum White Tiles Covered by a Carpet](../../2001-2500/2359-maximum-white-tiles-covered-by-a-carpet/)
- [2397. Maximum Rows Covered by Columns](../../2001-2500/2482-maximum-rows-covered-by-columns/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-covered-intervals/)
