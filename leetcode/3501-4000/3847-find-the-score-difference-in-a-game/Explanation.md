# LeetCode 3847: Find the Score Difference in a Game

**LeetCode Problem #3847 — Find the Score Difference in a Game**
Solve LeetCode Find the Score Difference in a Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Score Difference in a Game |
| LeetCode | #3847 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`, where `nums[i]` represents the points scored in the `i^th` game.

There are **exactly **two players. Initially, the first player is **active** and the second player is **inactive**.

The following rules apply **sequentially** for each game `i`:

If `nums[i]` is odd, the active and inactive players swap roles. 
 In every 6th game (that is, game indices `5, 11, 17, ...`), the active and inactive players swap roles. 
 The active player plays the `i^th` game and gains `nums[i]` points.

Return the **score difference**, defined as the first player's **total** score **minus** the second player's **total** score.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `0`
- **Explanation:** ​​​​​​​ 

 
 Game 0: Since the points are odd, the second player becomes active and gains `nums[0] = 1` point. 
 Game 1: No swap occurs. The second player gains `nums[1] = 2` points. 
 Game 2: Since the points are odd, the first player becomes active and gains `nums[2] = 3` points. 
 The score difference is `3 - 3 = 0`.

### Example 2
- **Input:** `nums = [2,4,2,1,2,1]`
- **Output:** `4`
- **Explanation:** Games 0 to 2: The first player gains `2 + 4 + 2 = 8` points. 
 Game 3: Since the points are odd, the second player is now active and gains `nums[3] = 1` point. 
 Game 4: The second player gains `nums[4] = 2` points. 
 Game 5: Since the points are odd, the players swap roles. Then, because this is the 6th game, the players swap again. The second player gains `nums[5] = 1` point. 
 The score difference is `8 - 4 = 4`.

### Example 3
- **Input:** `nums = [1]`
- **Output:** `-1`
- **Explanation:** Game 0: Since the points are odd, the second player is now active and gains `nums[0] = 1` point. 
 The score difference is `0 - 1 = -1`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Score Difference in a Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** ​​​​​​​ 

 
 Game 0: Since the points are odd, the second player becomes active and gains `nums[0] = 1` point. 
 Game 1: No swap occurs. The second player gains `nums[1] = 2` points. 
 Game 2: Since the points are odd, the first player becomes active and gains `nums[2] = 3` points. 
 The score difference is `3 - 3 = 0`.

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
class Solution:
    def scoreDifference(self, nums: list[int]) -> int:
        sign = 1
        diff = 0
        for i, x in enumerate(nums):
            if x % 2 == 1:
                sign = -sign
            if i % 6 == 5:
                sign = -sign
            diff += sign * x
        return diff
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
- [389. Find the Difference](../../0001-0500/0389-find-the-difference/)
- [2215. Find the Difference of Two Arrays](../../2001-2500/2215-find-the-difference-of-two-arrays/)
- [1275. Find Winner on a Tic Tac Toe Game](../../1001-1500/1275-find-winner-on-a-tic-tac-toe-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-score-difference-in-a-game/)
