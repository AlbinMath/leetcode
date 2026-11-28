# LeetCode 2251: Number of Flowers in Full Bloom

**LeetCode Problem #2251 — Number of Flowers in Full Bloom**
Solve LeetCode Number of Flowers in Full Bloom using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Flowers in Full Bloom |
| LeetCode | #2251 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer array `flowers`, where `flowers[i] = [start_i, end_i]` means the `i^th` flower will be in **full bloom** from `start_i` to `end_i` (**inclusive**). You are also given a **0-indexed** integer array `people` of size `n`, where `people[i]` is the time that the `i^th` person will arrive to see the flowers.

Return *an integer array *`answer`* of size *`n`*, where *`answer[i]`* is the **number** of flowers that are in full bloom when the *`i^th`* person arrives.*

## Constraints
- `1 <= flowers.length <= 5 * 10^4`
- `flowers[i].length == 2`
- `1 <= start_i <= end_i <= 10^9`
- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= 10^9`

## Examples
### Example 1
- **Input:** `flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]`
- **Output:** `[1,2,2,2]`
- **Explanation:** The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

### Example 2
- **Input:** `flowers = [[1,10],[3,3]], people = [3,3,2]`
- **Output:** `[2,2,1]`
- **Explanation:** The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Flowers in Full Bloom**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,2,2]`.
4. **Verification:** The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

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
import heapq

class Solution:
    def fullBloomFlowers(self, flowers, people):
        flowers.sort()
        order = sorted(range(len(people)), key=lambda i: people[i])
        ans = [0] * len(people)
        heap, j = [], 0
        for i in order:
            t = people[i]
            while j < len(flowers) and flowers[j][0] <= t:
                heapq.heappush(heap, flowers[j][1])
                j += 1
            while heap and heap[0] < t:
                heapq.heappop(heap)
            ans[i] = len(heap)
        return ans
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
- [2136. Earliest Possible Day of Full Bloom](../../2001-2500/2136-earliest-possible-day-of-full-bloom/)
- [1904. The Number of Full Rounds You Have Played](../../1501-2000/1904-the-number-of-full-rounds-you-have-played/)
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-flowers-in-full-bloom/)
