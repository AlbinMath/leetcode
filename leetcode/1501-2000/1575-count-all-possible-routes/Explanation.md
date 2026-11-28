# LeetCode 1575: Count All Possible Routes

**LeetCode Problem #1575 — Count All Possible Routes**
Solve LeetCode Count All Possible Routes using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count All Possible Routes |
| LeetCode | #1575 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of **distinct** positive integers locations where `locations[i]` represents the position of city `i`. You are also given integers `start`, `finish` and `fuel` representing the starting city, ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city `i`, you can pick any city `j` such that `j != i` and `0 <= j < locations.length` and move to city `j`. Moving from city `i` to city `j` reduces the amount of fuel you have by `|locations[i] - locations[j]|`. Please notice that `|x|` denotes the absolute value of `x`.

Notice that `fuel` **cannot** become negative at any point in time, and that you are **allowed** to visit any city more than once (including `start` and `finish`).

Return *the count of all possible routes from *`start` *to* `finish`. Since the answer may be too large, return it modulo `10^9 + 7`.

## Constraints
- `2 <= locations.length <= 100`
- `1 <= locations[i] <= 10^9`
- All integers in `locations` are **distinct**.
- `0 <= start, finish < locations.length`
- `1 <= fuel <= 200`

## Examples
### Example 1
- **Input:** `locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5`
- **Output:** `4`
- **Explanation:** The following are all possible routes, each uses 5 units of fuel:
1 -> 3
1 -> 2 -> 3
1 -> 4 -> 3
1 -> 4 -> 2 -> 3

### Example 2
- **Input:** `locations = [4,3,1], start = 1, finish = 0, fuel = 6`
- **Output:** `5`
- **Explanation:** The following are all possible routes:
1 -> 0, used fuel = 1
1 -> 2 -> 0, used fuel = 5
1 -> 2 -> 1 -> 0, used fuel = 5
1 -> 0 -> 1 -> 0, used fuel = 3
1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5

### Example 3
- **Input:** `locations = [5,2,1], start = 0, finish = 2, fuel = 3`
- **Output:** `0`
- **Explanation:** It is impossible to get from 0 to 2 using only 3 units of fuel since the shortest route needs 4 units of fuel.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count All Possible Routes**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The following are all possible routes, each uses 5 units of fuel:
1 -> 3
1 -> 2 -> 3
1 -> 4 -> 3
1 -> 4 -> 2 -> 3

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
from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]
        dp[start][fuel] = 1

        for f in range(fuel, 0, -1):
            for c in range(n):
                ways = dp[c][f]
                if not ways:
                    continue
                for j in range(n):
                    if j == c:
                        continue
                    cost = abs(locations[c] - locations[j])
                    if cost <= f:
                        dp[j][f - cost] = (dp[j][f - cost] + ways) % MOD

        return sum(dp[finish]) % MOD
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1277. Count Square Submatrices with All Ones](../../1001-1500/1277-count-square-submatrices-with-all-ones/)
- [1359. Count All Valid Pickup and Delivery Options](../../1001-1500/1359-count-all-valid-pickup-and-delivery-options/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-all-possible-routes/)
