# LeetCode 352: Data Stream as Disjoint Intervals

**LeetCode Problem #352 — Data Stream as Disjoint Intervals**
Solve LeetCode Data Stream as Disjoint Intervals using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Data Stream as Disjoint Intervals |
| LeetCode | #352 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a data stream input of non-negative integers `a_1, a_2, ..., a_n`, summarize the numbers seen so far as a list of disjoint intervals.

Implement the `SummaryRanges` class:

`SummaryRanges()` Initializes the object with an empty stream. 
 `void addNum(int value)` Adds the integer `value` to the stream. 
 `int[][] getIntervals()` Returns a summary of the integers in the stream currently as a list of disjoint intervals `[start_i, end_i]`. The answer should be sorted by `start_i`.

## Constraints
- `0 <= value <= 10^4`
- At most `3 * 10^4` calls will be made to `addNum` and `getIntervals`.
- At most `10^2` calls will be made to `getIntervals`.

## Examples
### Example 1
- **Input:** `["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]`
- **Output:** `[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]`
- **Explanation:** SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1); // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3); // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7); // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2); // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6); // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Data Stream as Disjoint Intervals**, we observe the problem requirements and utilize the **Heap** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]`.
4. **Verification:** SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1); // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3); // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7); // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2); // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6); // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from bisect import bisect_right
from typing import List

class SummaryRanges:
    def __init__(self):
        self.starts = []
        self.ends = []

    def addNum(self, value: int) -> None:
        i = bisect_right(self.starts, value)  # first interval with start > value
        # already covered by the previous interval
        if i > 0 and self.ends[i - 1] >= value:
            return
        join_left = i > 0 and self.ends[i - 1] + 1 == value
        join_right = i < len(self.starts) and self.starts[i] - 1 == value
        if join_left and join_right:
            self.ends[i - 1] = self.ends[i]
            del self.starts[i]
            del self.ends[i]
        elif join_left:
            self.ends[i - 1] = value
        elif join_right:
            self.starts[i] = value
        else:
            self.starts.insert(i, value)
            self.ends.insert(i, value)

    def getIntervals(self) -> List[List[int]]:
        return [[s, e] for s, e in zip(self.starts, self.ends)]
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [295. Find Median from Data Stream](../../0001-0500/0295-find-median-from-data-stream/)
- [2526. Find Consecutive Integers from a Data Stream](../../2501-3000/2526-find-consecutive-integers-from-a-data-stream/)
- [915. Partition Array into Disjoint Intervals](../../0501-1000/0915-partition-array-into-disjoint-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)
