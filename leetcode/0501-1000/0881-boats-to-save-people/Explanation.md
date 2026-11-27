# LeetCode 881: Boats to Save People

**LeetCode Problem #881 — Boats to Save People**
Solve LeetCode Boats to Save People using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Boats to Save People |
| LeetCode | #881 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `people` where `people[i]` is the weight of the `i^th` person, and an **infinite number of boats** where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

Return *the minimum number of boats to carry every given person*.

## Constraints
- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`

## Examples
### Example 1
- **Input:** `people = [1,2], limit = 3`
- **Output:** `1`
- **Explanation:** 1 boat (1, 2)

### Example 2
- **Input:** `people = [3,2,2,1], limit = 3`
- **Output:** `3`
- **Explanation:** 3 boats (1, 2), (2) and (3)

### Example 3
- **Input:** `people = [3,5,3,4], limit = 5`
- **Output:** `4`
- **Explanation:** 4 boats (3), (3), (4), (5)

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Boats to Save People**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `people = [1,2], limit = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** 1 boat (1, 2)

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
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people) - 1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            hi -= 1
            boats += 1
        return boats
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
- [1103. Distribute Candies to People](../../1001-1500/1103-distribute-candies-to-people/)
- [1282. Group the People Given the Group Size They Belong To](../../1001-1500/1282-group-the-people-given-the-group-size-they-belong-to/)
- [1452. People Whose List of Favorite Companies Is Not a Subset of Another List](../../1001-1500/1452-people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/boats-to-save-people/)
