# LeetCode 1535: Find the Winner of an Array Game

**LeetCode Problem #1535 — Find the Winner of an Array Game**
Solve LeetCode Find the Winner of an Array Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Winner of an Array Game |
| LeetCode | #1535 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr` of **distinct** integers and an integer `k`.

A game will be played between the first two elements of the array (i.e. `arr[0]` and `arr[1]`). In each round of the game, we compare `arr[0]` with `arr[1]`, the larger integer wins and remains at position `0`, and the smaller integer moves to the end of the array. The game ends when an integer wins `k` consecutive rounds.

Return *the integer which will win the game*.

It is **guaranteed** that there will be a winner of the game.

## Constraints
- `2 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^6`
- `arr` contains **distinct** integers.
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `arr = [2,1,3,5,4,6,7], k = 2`
- **Output:** `5`
- **Explanation:** Let's see the rounds of the game:
Round | arr | winner | win_count
 1 | [2,1,3,5,4,6,7] | 2 | 1
 2 | [2,3,5,4,6,7,1] | 3 | 1
 3 | [3,5,4,6,7,1,2] | 5 | 1
 4 | [5,4,6,7,1,2,3] | 5 | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.

### Example 2
- **Input:** `arr = [3,2,1], k = 10`
- **Output:** `3`
- **Explanation:** 3 will win the first 10 rounds consecutively.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Winner of an Array Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,1,3,5,4,6,7], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Let's see the rounds of the game:
Round | arr | winner | win_count
 1 | [2,1,3,5,4,6,7] | 2 | 1
 2 | [2,3,5,4,6,7,1] | 3 | 1
 3 | [3,5,4,6,7,1,2] | 5 | 1
 4 | [5,4,6,7,1,2,3] | 5 | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.

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
    def getWinner(self, arr: List[int], k: int) -> int:
        cur = arr[0]
        wins = 0

        for x in arr[1:]:
            if cur > x:
                wins += 1
            else:
                cur = x
                wins = 1
            if wins == k:
                return cur

        return cur
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
- [1275. Find Winner on a Tic Tac Toe Game](../../1001-1500/1400-find-winner-on-a-tic-tac-toe-game/)
- [1823. Find the Winner of the Circular Game](../../1501-2000/1951-find-the-winner-of-the-circular-game/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-winner-of-an-array-game/)
