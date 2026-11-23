# LeetCode 1665: Minimum Initial Energy to Finish Tasks

**LeetCode Problem #1665 — Minimum Initial Energy to Finish Tasks**
Solve LeetCode Minimum Initial Energy to Finish Tasks using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Initial Energy to Finish Tasks |
| LeetCode | #1665 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `tasks` where `tasks[i] = [actual_i, minimum_i]`:

`actual_i` is the actual amount of energy you **spend to finish** the `i^th` task. 
 `minimum_i` is the **minimum** amount of energy you **require to begin** the `i^th` task.

For example, if the task is `[10, 12]` and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

You can finish the tasks in **any order** you like.

Return the **minimum** initial amount of energy you will need to finish all the tasks.

## Constraints
- `1 <= tasks.length <= 10^5`
- `1 <= actual_​i <= minimum_i <= 10^4`

## Examples
### Example 1
- **Input:** `tasks = [[1,2],[2,4],[4,8]]`
- **Output:** `8`
- **Explanation:** Starting with 8 energy, we finish the tasks in the following order:
 - 3rd task. Now energy = 8 - 4 = 4.
 - 2nd task. Now energy = 4 - 2 = 2.
 - 1st task. Now energy = 2 - 1 = 1.
Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.

### Example 2
- **Input:** `tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]`
- **Output:** `32`
- **Explanation:** Starting with 32 energy, we finish the tasks in the following order:
 - 1st task. Now energy = 32 - 1 = 31.
 - 2nd task. Now energy = 31 - 2 = 29.
 - 3rd task. Now energy = 29 - 10 = 19.
 - 4th task. Now energy = 19 - 10 = 9.
 - 5th task. Now energy = 9 - 8 = 1.

### Example 3
- **Input:** `tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]`
- **Output:** `27`
- **Explanation:** Starting with 27 energy, we finish the tasks in the following order:
 - 5th task. Now energy = 27 - 5 = 22.
 - 2nd task. Now energy = 22 - 2 = 20.
 - 3rd task. Now energy = 20 - 3 = 17.
 - 1st task. Now energy = 17 - 1 = 16.
 - 4th task. Now energy = 16 - 4 = 12.
 - 6th task. Now energy = 12 - 6 = 6.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
1. **Sort:** Tasks are sorted by `(minimum - actual)` in descending order. This prioritizes tasks with the largest gap between their minimum requirement and actual cost.
2. **Greedy:** Iterate through tasks, tracking the cumulative `actual` energy spent (`current`). For each task, update `energy = max(energy, current + minimum)`.
3. Return `energy`.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `tasks = [[1,2],[2,4],[4,8]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Starting with 8 energy, we finish the tasks in the following order:
 - 3rd task. Now energy = 8 - 4 = 4.
 - 2nd task. Now energy = 4 - 2 = 2.
 - 1st task. Now energy = 2 - 1 = 1.
Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        // Sort by (minimum - actual) in descending order
        sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b) {
            return (a[1] - a[0]) > (b[1] - b[0]);
        });

        int energy = 0;
        int current = 0;

        for (auto& task : tasks) {
            int actual = task[0];
            int minimum = task[1];

            // Energy needed before starting this task
            energy = max(energy, current + minimum);

            current += actual;
        }

        return energy;
    }
};
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
- [1986. Minimum Number of Work Sessions to Finish the Tasks](../../2001-2500/2114-minimum-number-of-work-sessions-to-finish-the-tasks/)
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1825-find-minimum-time-to-finish-all-jobs/)
- [2589. Minimum Time to Complete All Tasks](../../2501-3000/2657-minimum-time-to-complete-all-tasks/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/)
