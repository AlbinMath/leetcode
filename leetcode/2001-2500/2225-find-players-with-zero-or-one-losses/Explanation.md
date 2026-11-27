# LeetCode 2225: Find Players With Zero or One Losses

**LeetCode Problem #2225 — Find Players With Zero or One Losses**
Solve LeetCode Find Players With Zero or One Losses using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Players With Zero or One Losses |
| LeetCode | #2225 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `matches` where `matches[i] = [winner_i, loser_i]` indicates that the player `winner_i` defeated player `loser_i` in a match.

Return *a list *`answer`* of size *`2`* where:*

`answer[0]` is a list of all players that have **not** lost any matches. 
 `answer[1]` is a list of all players that have lost exactly **one** match.

The values in the two lists should be returned in **increasing** order.

**Note:**

You should only consider the players that have played **at least one** match. 
 The testcases will be generated such that **no** two matches will have the **same** outcome.

## Constraints
- `1 <= matches.length <= 10^5`
- `matches[i].length == 2`
- `1 <= winner_i, loser_i <= 10^5`
- `winner_i != loser_i`
- All `matches[i]` are **unique**.

## Examples
### Example 1
- **Input:** `matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]`
- **Output:** `[[1,2,10],[4,5,7,8]]`
- **Explanation:** Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

### Example 2
- **Input:** `matches = [[2,3],[1,3],[5,4],[6,4]]`
- **Output:** `[[1,2,5,6],[]]`
- **Explanation:** Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Players With Zero or One Losses**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2,10],[4,5,7,8]]`.
4. **Verification:** Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}
        
        for winner, loser in matches:
            losses.setdefault(winner, 0)
            losses[loser] = losses.get(loser, 0) + 1
            
        zero_losses = [player for player, count in losses.items() if count == 0]
        one_loss = [player for player, count in losses.items() if count == 1]
        
        return [sorted(zero_losses), sorted(one_loss)]
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1304. Find N Unique Integers Sum up to Zero](../../1001-1500/1304-find-n-unique-integers-sum-up-to-zero/)
- [1611. Minimum One Bit Operations to Make Integers Zero](../../1501-2000/1611-minimum-one-bit-operations-to-make-integers-zero/)
- [3238. Find the Number of Winning Players](../../3001-3500/3238-find-the-number-of-winning-players/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-players-with-zero-or-one-losses/)
