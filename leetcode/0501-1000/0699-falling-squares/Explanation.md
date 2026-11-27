# LeetCode 699: Falling Squares

**LeetCode Problem #699 — Falling Squares**
Solve LeetCode Falling Squares using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Falling Squares |
| LeetCode | #699 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are several squares being dropped onto the X-axis of a 2D plane.

You are given a 2D integer array `positions` where `positions[i] = [left_i, sideLength_i]` represents the `i^th` square with a side length of `sideLength_i` that is dropped with its left edge aligned with X-coordinate `left_i`.

Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands **on the top side of another square** or **on the X-axis**. A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved.

After each square is dropped, you must record the **height of the current tallest stack of squares**.

Return *an integer array *`ans`* where *`ans[i]`* represents the height described above after dropping the *`i^th`* square*.

## Constraints
- `1 <= positions.length <= 1000`
- `1 <= left_i <= 10^8`
- `1 <= sideLength_i <= 10^6`

## Examples
### Example 1
- **Input:** `positions = [[1,2],[2,3],[6,1]]`
- **Output:** `[2,5,5]`
- **Explanation:** After the first drop, the tallest stack is square 1 with a height of 2.
After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
Thus, we return an answer of [2, 5, 5].

### Example 2
- **Input:** `positions = [[100,100],[200,100]]`
- **Output:** `[100,100]`
- **Explanation:** After the first drop, the tallest stack is square 1 with a height of 100.
After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
Thus, we return an answer of [100, 100].
Note that square 2 only brushes the right side of square 1, which does not count as landing on it.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Falling Squares**, we observe the problem requirements and utilize the **Stack & Queue** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `positions = [[1,2],[2,3],[6,1]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,5,5]`.
4. **Verification:** After the first drop, the tallest stack is square 1 with a height of 2.
After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
Thus, we return an answer of [2, 5, 5].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        landed = []  
        ans = []
        max_height = 0
        
        for left, size in positions:
            right = left + size
            base_height = 0
            
            for prev_l, prev_r, prev_h in landed:
                if left < prev_r and prev_l < right:
                    if prev_h > base_height:
                        base_height = prev_h
                        
            current_height = base_height + size
            landed.append((left, right, current_height))
            
            max_height = max(max_height, current_height)
            ans.append(max_height)
            
        return ans
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [803. Bricks Falling When Hit](../../0501-1000/0803-bricks-falling-when-hit/)
- [931. Minimum Falling Path Sum](../../0501-1000/0931-minimum-falling-path-sum/)
- [1289. Minimum Falling Path Sum II](../../1001-1500/1289-minimum-falling-path-sum-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/falling-squares/)
