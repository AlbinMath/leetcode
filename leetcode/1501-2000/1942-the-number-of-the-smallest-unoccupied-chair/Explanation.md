# LeetCode 1942: The Number of the Smallest Unoccupied Chair

**LeetCode Problem #1942 — The Number of the Smallest Unoccupied Chair**
Solve LeetCode The Number of the Smallest Unoccupied Chair using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Number of the Smallest Unoccupied Chair |
| LeetCode | #1942 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a party where `n` friends numbered from `0` to `n - 1` are attending. There is an **infinite** number of chairs in this party that are numbered from `0` to `infinity`. When a friend arrives at the party, they sit on the unoccupied chair with the **smallest number**.

For example, if chairs `0`, `1`, and `5` are occupied when a friend comes, they will sit on chair number `2`.

When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a **0-indexed** 2D integer array `times` where `times[i] = [arrival_i, leaving_i]`, indicating the arrival and leaving times of the `i^th` friend respectively, and an integer `targetFriend`. All arrival times are **distinct**.

Return* the **chair number** that the friend numbered *`targetFriend`* will sit on*.

## Constraints
- `n == times.length`
- `2 <= n <= 10^4`
- `times[i].length == 2`
- `1 <= arrival_i < leaving_i <= 10^5`
- `0 <= targetFriend <= n - 1`
- Each `arrival_i` time is **distinct**.

## Examples
### Example 1
- **Input:** `times = [[1,4],[2,3],[4,6]], targetFriend = 1`
- **Output:** `1`
- **Explanation:** - Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.

### Example 2
- **Input:** `times = [[3,10],[1,5],[2,6]], targetFriend = 0`
- **Output:** `2`
- **Explanation:** - Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **The Number of the Smallest Unoccupied Chair**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `times = [[1,4],[2,3],[4,6]], targetFriend = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** - Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = sorted((arr, lv, idx) for idx, (arr, lv) in enumerate(times))
        
        available_chairs = []  # min-heap of freed chair numbers
        occupied_chairs = []   # min-heap of (leaving_time, chair_number)
        next_new_chair = 0
        
        for arrival, leaving, friend_id in events:
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, freed_chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, freed_chair)
            if available_chairs:
                chair = heapq.heappop(available_chairs)
            else:
                chair = next_new_chair
                next_new_chair += 1
                
            if friend_id == targetFriend:
                return chair
                
            heapq.heappush(occupied_chairs, (leaving, chair))
            
        return -1
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [668. Kth Smallest Number in Multiplication Table](../../0501-1000/0668-kth-smallest-number-in-multiplication-table/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../../1001-1500/1334-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number](../../1501-2000/1850-minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/)
