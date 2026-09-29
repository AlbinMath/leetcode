# Remove Covered Intervals

## Problem Explanation
Given a list of intervals, remove all intervals that are covered by another interval. Interval `[a, b)` is covered by `[c, d)` if `c <= a` and `b <= d`. Return the number of remaining intervals.

## How the Code Works
The code uses **Sorting + Greedy**.

1. **Sort:** Sort intervals by start ascending. If starts are equal, sort by end **descending**. This ensures that if two intervals share the same start, the longer one comes first.
2. **Iterate:** Track `maxEnd` — the maximum end value seen so far. For each interval:
   - If `interval[1] > maxEnd`: This interval is NOT covered (it extends beyond all previous intervals), so increment the `count` and update `maxEnd`.
   - Otherwise: This interval is covered by a previous one (its end is ≤ `maxEnd`), so skip it.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(\log N)$.
