# LeetCode 3771: Total Score of Dungeon Runs

**LeetCode Problem #3771 — Total Score of Dungeon Runs**
Solve LeetCode Total Score of Dungeon Runs using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Total Score of Dungeon Runs |
| LeetCode | #3771 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **positive** integer `hp` and two **positive** **1-indexed** integer arrays `damage` and `requirement`.

There is a dungeon with `n` trap rooms numbered from 1 to `n`. Entering room `i` reduces your health points by `damage[i]`. After that reduction, if your remaining health points are **at least** `requirement[i]`, you earn **1 point **for that room.

Let `score(j)` be the number of **points** you get if you start with `hp` health points and enter the rooms `j`, `j + 1`, ..., `n` in this order.

Return the integer `score(1) + score(2) + ... + score(n)`, the sum of scores over all starting rooms.

**Note**: You cannot skip rooms. You can finish your journey even if your health points become non-positive.

## Constraints
- `1 <= hp <= 10^9`
- `1 <= n == damage.length == requirement.length <= 10^5`
- `1 <= damage[i], requirement[i] <= 10^4`

## Examples
### Example 1
- **Input:** `hp = 11, damage = [3,6,7], requirement = [4,2,5]`
- **Output:** `3`
- **Explanation:** `score(1) = 2`, `score(2) = 1`, `score(3) = 0`. The total score is `2 + 1 + 0 = 3`. 

 As an example, `score(1) = 2` because you get 2 points if you start from room 1. 

 
 You start with 11 health points. 
 Enter room 1. Your health points are now `11 - 3 = 8`. You get 1 point because `8 >= 4`. 
 Enter room 2. Your health points are now `8 - 6 = 2`. You get 1 point because `2 >= 2`. 
 Enter room 3. Your health points are now `2 - 7 = -5`. You do not get any points because `-5 < 5`.

### Example 2
- **Input:** `hp = 2, damage = [10000,1], requirement = [1,1]`
- **Output:** `1`
- **Explanation:** `score(1) = 0`, `score(2) = 1`. The total score is `0 + 1 = 1`. 

 `score(1) = 0` because you do not get any points if you start from room 1. 

 
 You start with 2 health points. 
 Enter room 1. Your health points are now `2 - 10000 = -9998`. You do not get any points because `-9998 < 1`. 
 Enter room 2. Your health points are now `-9998 - 1 = -9999`. You do not get any points because `-9999 < 1`. 
 

 `score(2) = 1` because you get 1 point if you start from room 2. 

 
 You start with 2 health points. 
 Enter room 2. Your health points are now `2 - 1 = 1`. You get 1 point because `1 >= 1`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Total Score of Dungeon Runs**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `hp = 11, damage = [3,6,7], requirement = [4,2,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** `score(1) = 2`, `score(2) = 1`, `score(3) = 0`. The total score is `2 + 1 + 0 = 3`. 

 As an example, `score(1) = 2` because you get 2 points if you start from room 1. 

 
 You start with 11 health points. 
 Enter room 1. Your health points are now `11 - 3 = 8`. You get 1 point because `8 >= 4`. 
 Enter room 2. Your health points are now `8 - 6 = 2`. You get 1 point because `2 >= 2`. 
 Enter room 3. Your health points are now `2 - 7 = -5`. You do not get any points because `-5 < 5`.

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
from bisect import bisect_left
from typing import List

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + damage[i]

        ans = 0
        for i in range(1, n + 1):                 # room i (1-indexed)
            t = requirement[i - 1] + pre[i] - hp
            k = bisect_left(pre, t, 0, i)         # smallest k in [0, i-1] with pre[k] >= t
            ans += i - k                          # k can be i (none valid) -> adds 0
        return ans
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
- [856. Score of Parentheses](../../0501-1000/0856-score-of-parentheses/)
- [861. Score After Flipping Matrix](../../0501-1000/0861-score-after-flipping-matrix/)
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1255-maximum-score-words-formed-by-letters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/total-score-of-dungeon-runs/)
