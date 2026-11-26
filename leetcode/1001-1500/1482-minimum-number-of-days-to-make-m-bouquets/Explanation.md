# LeetCode 1482: Minimum Number of Days to Make m Bouquets

**LeetCode Problem #1482 — Minimum Number of Days to Make m Bouquets**
Solve LeetCode Minimum Number of Days to Make m Bouquets using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Days to Make m Bouquets |
| LeetCode | #1482 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `bloomDay`, an integer `m` and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent flowers** from the garden.

The garden consists of `n` flowers, the `i^th` flower will bloom in the `bloomDay[i]` and then can be used in **exactly one** bouquet.

Return the **minimum** number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

## Constraints
- `bloomDay.length == n`
- `1 <= n <= 10^5`
- `1 <= bloomDay[i] <= 10^9`
- `1 <= m <= 10^6`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `bloomDay = [1,10,3,10,2], m = 3, k = 1`
- **Output:** `3`
- **Explanation:** Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _] // we can only make one bouquet.
After day 2: [x, _, _, _, x] // we can only make two bouquets.
After day 3: [x, _, x, _, x] // we can make 3 bouquets. The answer is 3.

### Example 2
- **Input:** `bloomDay = [1,10,3,10,2], m = 3, k = 2`
- **Output:** `-1`
- **Explanation:** We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

### Example 3
- **Input:** `bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3`
- **Output:** `12`
- **Explanation:** We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Days to Make m Bouquets**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `bloomDay = [1,10,3,10,2], m = 3, k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _] // we can only make one bouquet.
After day 2: [x, _, _, _, x] // we can only make two bouquets.
After day 3: [x, _, x, _, x] // we can make 3 bouquets. The answer is 3.

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
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def can_make(d: int) -> bool:
            bouquets = run = 0
            for b in bloomDay:
                if b <= d:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0
                        if bouquets >= m:
                            return True
                else:
                    run = 0
            return False

        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
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
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1347-minimum-number-of-steps-to-make-two-strings-anagram/)
- [1553. Minimum Number of Days to Eat N Oranges](../../1501-2000/1553-minimum-number-of-days-to-eat-n-oranges/)
- [1568. Minimum Number of Days to Disconnect Island](../../1501-2000/1568-minimum-number-of-days-to-disconnect-island/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
