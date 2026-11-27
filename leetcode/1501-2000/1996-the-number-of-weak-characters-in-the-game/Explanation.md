# LeetCode 1996: The Number of Weak Characters in the Game

**LeetCode Problem #1996 — The Number of Weak Characters in the Game**
Solve LeetCode The Number of Weak Characters in the Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Number of Weak Characters in the Game |
| LeetCode | #1996 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are playing a game that contains multiple characters, and each of the characters has **two** main properties: **attack** and **defense**. You are given a 2D integer array `properties` where `properties[i] = [attack_i, defense_i]` represents the properties of the `i^th` character in the game.

A character is said to be **weak** if any other character has **both** attack and defense levels **strictly greater** than this character's attack and defense levels. More formally, a character `i` is said to be **weak** if there exists another character `j` where `attack_j > attack_i` and `defense_j > defense_i`.

Return *the number of **weak** characters*.

## Constraints
- `2 <= properties.length <= 10^5`
- `properties[i].length == 2`
- `1 <= attack_i, defense_i <= 10^5`

## Examples
### Example 1
- **Input:** `properties = [[5,5],[6,3],[3,6]]`
- **Output:** `0`
- **Explanation:** No character has strictly greater attack and defense than the other.

### Example 2
- **Input:** `properties = [[2,2],[3,3]]`
- **Output:** `1`
- **Explanation:** The first character is weak because the second character has a strictly greater attack and defense.

### Example 3
- **Input:** `properties = [[1,5],[10,4],[4,3]]`
- **Output:** `1`
- **Explanation:** The third character is weak because the second character has a strictly greater attack and defense.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **The Number of Weak Characters in the Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `properties = [[5,5],[6,3],[3,6]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** No character has strictly greater attack and defense than the other.

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
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_def = 0
        weak = 0
        for _, d in properties:
            if d < max_def:
                weak += 1
            else:
                max_def = d
        return weak
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
- [2974. Minimum Number Game](../../2501-3000/2974-minimum-number-game/)
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1358-number-of-substrings-containing-all-three-characters/)
- [1898. Maximum Number of Removable Characters](../../1501-2000/1898-maximum-number-of-removable-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/)
