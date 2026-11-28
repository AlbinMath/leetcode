# LeetCode 1366: Rank Teams by Votes

**LeetCode Problem #1366 — Rank Teams by Votes**
Solve LeetCode Rank Teams by Votes using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rank Teams by Votes |
| LeetCode | #1366 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

You are given an array of strings `votes` which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return *a string of all teams **sorted** by the ranking system*.

## Constraints
- `1 <= votes.length <= 1000`
- `1 <= votes[i].length <= 26`
- `votes[i].length == votes[j].length` for `0 <= i, j < votes.length`.
- `votes[i][j]` is an English **uppercase** letter.
- All characters of `votes[i]` are unique.
- All the characters that occur in `votes[0]` **also occur** in `votes[j]` where `1 <= j < votes.length`.

## Examples
### Example 1
- **Input:** `votes = ["ABC","ACB","ABC","ACB","ACB"]`
- **Output:** `"ACB"`
- **Explanation:** Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.

### Example 2
- **Input:** `votes = ["WXYZ","XYZW"]`
- **Output:** `"XWYZ"`
- **Explanation:** X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in the second position, while W does not have any votes in the second position.

### Example 3
- **Input:** `votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]`
- **Output:** `"ZMNAGUEDSJYLBOPHRQICWFXTVK"`
- **Explanation:** Only one voter, so their votes are used for the ranking.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rank Teams by Votes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `votes = ["ABC","ACB","ABC","ACB","ACB"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ACB"`.
4. **Verification:** Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.

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
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        count = {ch: [0] * n for ch in votes[0]}

        for vote in votes:
            for pos, ch in enumerate(vote):
                count[ch][pos] += 1

        teams = sorted(count, key=lambda ch: ([-c for c in count[ch]], ch))
        return ''.join(teams)
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
- [178. Rank Scores](../../0001-0500/0178-rank-scores/)
- [1331. Rank Transform of an Array](../../1001-1500/1331-rank-transform-of-an-array/)
- [1615. Maximal Network Rank](../../1501-2000/1615-maximal-network-rank/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rank-teams-by-votes/)
