# LeetCode 2106: Maximum Fruits Harvested After at Most K Steps

**LeetCode Problem #2106 — Maximum Fruits Harvested After at Most K Steps**
Solve LeetCode Maximum Fruits Harvested After at Most K Steps using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Fruits Harvested After at Most K Steps |
| LeetCode | #2106 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array `fruits` where `fruits[i] = [position_i, amount_i]` depicts `amount_i` fruits at the position `position_i`. `fruits` is already **sorted** by `position_i` in **ascending order**, and each `position_i` is **unique**.

You are also given an integer `startPos` and an integer `k`. Initially, you are at the position `startPos`. From any position, you can either walk to the **left or right**. It takes **one step** to move **one unit** on the x-axis, and you can walk **at most** `k` steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.

Return *the **maximum total number** of fruits you can harvest*.

## Constraints
- `1 <= fruits.length <= 10^5`
- `fruits[i].length == 2`
- `0 <= startPos, position_i <= 2 * 10^5`
- `position_i-1 < position_i` for any `i > 0` (**0-indexed**)
- `1 <= amount_i <= 10^4`
- `0 <= k <= 2 * 10^5`

## Examples
### Example 1
- **Input:** `fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4`
- **Output:** `9`
- **Explanation:** The optimal way is to:
- Move right to position 6 and harvest 3 fruits
- Move right to position 8 and harvest 6 fruits
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.

### Example 2
- **Input:** `fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4`
- **Output:** `14`
- **Explanation:** You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
The optimal way is to:
- Harvest the 7 fruits at the starting position 5
- Move left to position 4 and harvest 1 fruit
- Move right to position 6 and harvest 2 fruits
- Move right to position 7 and harvest 4 fruits
You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.

### Example 3
- **Input:** `fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2`
- **Output:** `0`
- **Explanation:** You can move at most k = 2 steps and cannot reach any position with fruits.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Fruits Harvested After at Most K Steps**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The optimal way is to:
- Move right to position 6 and harvest 3 fruits
- Move right to position 8 and harvest 6 fruits
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.

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
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def min_steps(left_pos: int, right_pos: int) -> int:
            return (right_pos - left_pos) + min(abs(startPos - left_pos), abs(startPos - right_pos))
        
        left = 0
        curr_fruits = 0
        max_fruits = 0
        
        for right, (pos, amount) in enumerate(fruits):
            curr_fruits += amount
            while left <= right and min_steps(fruits[left][0], pos) > k:
                curr_fruits -= fruits[left][1]
                left += 1
            if curr_fruits > max_fruits:
                max_fruits = curr_fruits
                
        return max_fruits
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
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../../3001-3500/3428-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)
- [3430. Maximum and Minimum Sums of at Most Size K Subarrays](../../3001-3500/3430-maximum-and-minimum-sums-of-at-most-size-k-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/)
