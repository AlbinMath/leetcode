# Minimum Initial Energy To Finish Tasks

## Problem Explanation
Each task has an `actual` energy cost and a `minimum` energy requirement to start it. Find the minimum initial energy needed to complete all tasks in some order.

## How the Code Works
1. **Sort:** Tasks are sorted by `(minimum - actual)` in descending order. This prioritizes tasks with the largest gap between their minimum requirement and actual cost.
2. **Greedy:** Iterate through tasks, tracking the cumulative `actual` energy spent (`current`). For each task, update `energy = max(energy, current + minimum)`.
3. Return `energy`.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$.
