# LeetCode 2491: Divide Players Into Teams of Equal Skill

**LeetCode Problem #2491 — Divide Players Into Teams of Equal Skill**
Solve LeetCode Divide Players Into Teams of Equal Skill using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divide Players Into Teams of Equal Skill |
| LeetCode | #2491 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer array `skill` of **even** length `n` where `skill[i]` denotes the skill of the `i^th` player. Divide the players into `n / 2` teams of size `2` such that the total skill of each team is **equal**.

The **chemistry** of a team is equal to the **product** of the skills of the players on that team.

Return *the sum of the **chemistry** of all the teams, or return *`-1`* if there is no way to divide the players into teams such that the total skill of each team is equal.*

## Constraints
- `2 <= skill.length <= 10^5`
- `skill.length` is even.
- `1 <= skill[i] <= 1000`

## Examples
### Example 1
- **Input:** `skill = [3,2,5,1,3,4]`
- **Output:** `22`
- **Explanation:** Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

### Example 2
- **Input:** `skill = [3,4]`
- **Output:** `12`
- **Explanation:** The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.

### Example 3
- **Input:** `skill = [1,1,2,3]`
- **Output:** `-1`
- **Explanation:** There is no way to divide the players into teams such that the total skill of each team is equal.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Divide Players Into Teams of Equal Skill**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `skill = [3,2,5,1,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `22`.
4. **Verification:** Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var dividePlayers = function(skill) {
    skill.sort((a, b) => a - b);

    const n = skill.length;

    const total = skill.reduce((sum, value) => sum + value, 0);
    const target = total / (n / 2);

    let left = 0;
    let right = n - 1;

    let chemistry = 0;

    while (left < right) {
        const teamSkill = skill[left] + skill[right];
        if (teamSkill !== target) {
            return -1;
        }

        chemistry += skill[left] * skill[right];

        left++;
        right--;
    }

    return chemistry;
};
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
- [2206. Divide Array Into Equal Pairs](../../2001-2500/2206-divide-array-into-equal-pairs/)
- [2138. Divide a String Into Groups of Size k](../../2001-2500/2138-divide-a-string-into-groups-of-size-k/)
- [2406. Divide Intervals Into Minimum Number of Groups](../../2001-2500/2406-divide-intervals-into-minimum-number-of-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/)
