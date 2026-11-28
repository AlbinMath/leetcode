# LeetCode 2383: Minimum Hours of Training to Win a Competition

**LeetCode Problem #2383 — Minimum Hours of Training to Win a Competition**
Solve LeetCode Minimum Hours of Training to Win a Competition using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Hours of Training to Win a Competition |
| LeetCode | #2383 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are entering a competition, and are given two **positive** integers `initialEnergy` and `initialExperience` denoting your initial energy and initial experience respectively.

You are also given two **0-indexed** integer arrays `energy` and `experience`, both of length `n`.

You will face `n` opponents **in order**. The energy and experience of the `i^th` opponent is denoted by `energy[i]` and `experience[i]` respectively. When you face an opponent, you need to have both **strictly** greater experience and energy to defeat them and move to the next opponent if available.

Defeating the `i^th` opponent **increases** your experience by `experience[i]`, but **decreases** your energy by `energy[i]`.

Before starting the competition, you can train for some number of hours. After each hour of training, you can **either** choose to increase your initial experience by one, or increase your initial energy by one.

Return *the **minimum** number of training hours required to defeat all *`n`* opponents*.

## Constraints
- `n == energy.length == experience.length`
- `1 <= n <= 100`
- `1 <= initialEnergy, initialExperience, energy[i], experience[i] <= 100`

## Examples
### Example 1
- **Input:** `initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]`
- **Output:** `8`
- **Explanation:** You can increase your energy to 11 after 6 hours of training, and your experience to 5 after 2 hours of training.
You face the opponents in the following order:
- You have more energy and experience than the 0^th opponent so you win.
 Your energy becomes 11 - 1 = 10, and your experience becomes 5 + 2 = 7.
- You have more energy and experience than the 1^st opponent so you win.
 Your energy becomes 10 - 4 = 6, and your experience becomes 7 + 6 = 13.
- You have more energy and experience than the 2^nd opponent so you win.
 Your energy becomes 6 - 3 = 3, and your experience becomes 13 + 3 = 16.
- You have more energy and experience than the 3^rd opponent so you win.
 Your energy becomes 3 - 2 = 1, and your experience becomes 16 + 1 = 17.
You did a total of 6 + 2 = 8 hours of training before the competition, so we return 8.
It can be proven that no smaller answer exists.

### Example 2
- **Input:** `initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]`
- **Output:** `0`
- **Explanation:** You do not need any additional energy or experience to win the competition, so we return 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Hours of Training to Win a Competition**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** You can increase your energy to 11 after 6 hours of training, and your experience to 5 after 2 hours of training.
You face the opponents in the following order:
- You have more energy and experience than the 0^th opponent so you win.
 Your energy becomes 11 - 1 = 10, and your experience becomes 5 + 2 = 7.
- You have more energy and experience than the 1^st opponent so you win.
 Your energy becomes 10 - 4 = 6, and your experience becomes 7 + 6 = 13.
- You have more energy and experience than the 2^nd opponent so you win.
 Your energy becomes 6 - 3 = 3, and your experience becomes 13 + 3 = 16.
- You have more energy and experience than the 3^rd opponent so you win.
 Your energy becomes 3 - 2 = 1, and your experience becomes 16 + 1 = 17.
You did a total of 6 + 2 = 8 hours of training before the competition, so we return 8.
It can be proven that no smaller answer exists.

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
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: List[int], experience: List[int]) -> int:
        hours = max(0, sum(energy) + 1 - initialEnergy)
        exp = initialExperience
        for e in experience:
            if exp <= e:
                need = e + 1 - exp
                hours += need
                exp += need
            exp += e
        return hours
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
- [2212. Maximum Points in an Archery Competition](../../2001-2500/2212-maximum-points-in-an-archery-competition/)
- [2358. Maximum Number of Groups Entering a Competition](../../2001-2500/2358-maximum-number-of-groups-entering-a-competition/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/)
