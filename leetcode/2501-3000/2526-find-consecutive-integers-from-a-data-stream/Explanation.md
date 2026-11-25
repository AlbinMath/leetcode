# LeetCode 2526: Find Consecutive Integers from a Data Stream

**LeetCode Problem #2526 — Find Consecutive Integers from a Data Stream**
Solve LeetCode Find Consecutive Integers from a Data Stream using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Consecutive Integers from a Data Stream |
| LeetCode | #2526 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
For a stream of integers, implement a data structure that checks if the last `k` integers parsed in the stream are **equal** to `value`.

Implement the **DataStream** class:

`DataStream(int value, int k)` Initializes the object with an empty integer stream and the two integers `value` and `k`. 
 `boolean consec(int num)` Adds `num` to the stream of integers. Returns `true` if the last `k` integers are equal to `value`, and `false` otherwise. If there are less than `k` integers, the condition does not hold true, so returns `false`.

## Constraints
- `1 <= value, num <= 10^9`
- `1 <= k <= 10^5`
- At most `10^5` calls will be made to `consec`.

## Examples
### Example 1
- **Input:** `["DataStream", "consec", "consec", "consec", "consec"]
[[4, 3], [4], [4], [4], [3]]`
- **Output:** `[null, false, false, true, false]`
- **Explanation:** DataStream dataStream = new DataStream(4, 3); //value = 4, k = 3 
dataStream.consec(4); // Only 1 integer is parsed, so returns False. 
dataStream.consec(4); // Only 2 integers are parsed.
 // Since 2 is less than k, returns False. 
dataStream.consec(4); // The 3 integers parsed are all equal to value, so returns True. 
dataStream.consec(3); // The last k integers parsed in the stream are [4,4,3].
 // Since 3 is not equal to value, it returns False.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Consecutive Integers from a Data Stream**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["DataStream", "consec", "consec", "consec", "consec"]
[[4, 3], [4], [4], [4], [3]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, false, false, true, false]`.
4. **Verification:** DataStream dataStream = new DataStream(4, 3); //value = 4, k = 3 
dataStream.consec(4); // Only 1 integer is parsed, so returns False. 
dataStream.consec(4); // Only 2 integers are parsed.
 // Since 2 is less than k, returns False. 
dataStream.consec(4); // The 3 integers parsed are all equal to value, so returns True. 
dataStream.consec(3); // The last k integers parsed in the stream are [4,4,3].
 // Since 3 is not equal to value, it returns False.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.run = 0      # length of the current streak of `value`

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.run += 1
        else:
            self.run = 0
        return self.run >= self.k
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
- [295. Find Median from Data Stream](../../0001-0500/0295-find-median-from-data-stream/)
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../../2001-2500/2177-find-three-consecutive-integers-that-sum-to-a-given-number/)
- [600. Non-negative Integers without Consecutive Ones](../../0501-1000/0600-non-negative-integers-without-consecutive-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/)
