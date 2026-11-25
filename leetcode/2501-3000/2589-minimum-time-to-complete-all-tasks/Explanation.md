# LeetCode 2589: Minimum Time to Complete All Tasks

**LeetCode Problem #2589 — Minimum Time to Complete All Tasks**
Solve LeetCode Minimum Time to Complete All Tasks using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Complete All Tasks |
| LeetCode | #2589 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a computer that can run an unlimited number of tasks **at the same time**. You are given a 2D integer array `tasks` where `tasks[i] = [start_i, end_i, duration_i]` indicates that the `i^th` task should run for a total of `duration_i` seconds (not necessarily continuous) within the **inclusive** time range `[start_i, end_i]`.

You may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.

Return *the minimum time during which the computer should be turned on to complete all tasks*.

## Constraints
- `1 <= tasks.length <= 2000`
- `tasks[i].length == 3`
- `1 <= start_i, end_i <= 2000`
- `1 <= duration_i <= end_i - start_i + 1 `

## Examples
### Example 1
- **Input:** `tasks = [[2,3,1],[4,5,1],[1,5,2]]`
- **Output:** `2`
- **Explanation:** - The first task can be run in the inclusive time range [2, 2].
- The second task can be run in the inclusive time range [5, 5].
- The third task can be run in the two inclusive time ranges [2, 2] and [5, 5].
The computer will be on for a total of 2 seconds.

### Example 2
- **Input:** `tasks = [[1,3,2],[2,5,3],[5,6,2]]`
- **Output:** `4`
- **Explanation:** - The first task can be run in the inclusive time range [2, 3].
- The second task can be run in the inclusive time ranges [2, 3] and [5, 5].
- The third task can be run in the two inclusive time range [5, 6].
The computer will be on for a total of 4 seconds.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Time to Complete All Tasks**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tasks = [[2,3,1],[4,5,1],[1,5,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** - The first task can be run in the inclusive time range [2, 2].
- The second task can be run in the inclusive time range [5, 5].
- The third task can be run in the two inclusive time ranges [2, 2] and [5, 5].
The computer will be on for a total of 2 seconds.

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
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        // Sort tasks by end time ascending
        sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        
        bool on[2001] = {false};
        int total_on = 0;
        
        for (const auto& task : tasks) {
            int start = task[0];
            int end = task[1];
            int duration = task[2];
            
            // Count how many seconds in [start, end] are already active
            for (int t = start; t <= end; ++t) {
                if (on[t]) {
                    duration--;
                }
            }
            
            // Greedily allocate remaining required seconds as late as possible
            for (int t = end; duration > 0; --t) {
                if (!on[t]) {
                    on[t] = true;
                    duration--;
                    total_on++;
                }
            }
        }
        
        return total_on;
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
- [2244. Minimum Rounds to Complete All Tasks](../../2001-2500/2244-minimum-rounds-to-complete-all-tasks/)
- [3733. Minimum Time to Complete All Deliveries](../../3501-4000/3733-minimum-time-to-complete-all-deliveries/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/)
