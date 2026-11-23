# LeetCode 575: Distribute Candies

**LeetCode Problem #575 — Distribute Candies**
Solve LeetCode Distribute Candies using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distribute Candies |
| LeetCode | #575 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice has `n` candies, where the `i^th` candy is of type `candyType[i]`. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat `n / 2` of the candies she has (`n` is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array `candyType` of length `n`, return *the **maximum** number of different types of candies she can eat if she only eats *`n / 2`* of them*.

## Constraints
- `n == candyType.length`
- `2 <= n <= 10^4`
- `n` is even.
- `-10^5 <= candyType[i] <= 10^5`

## Examples
### Example 1
- **Input:** `candyType = [1,1,2,2,3,3]`
- **Output:** `3`
- **Explanation:** Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

### Example 2
- **Input:** `candyType = [1,1,2,3]`
- **Output:** `2`
- **Explanation:** Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.

### Example 3
- **Input:** `candyType = [6,6,6,6]`
- **Output:** `1`
- **Explanation:** Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Distribute Candies**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `candyType = [1,1,2,2,3,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

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
    def distributeCandies(self, candyType):
        unique_types = len(set(candyType))

        return min(unique_types, len(candyType) // 2)
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
- [1103. Distribute Candies to People](../../1001-1500/1195-distribute-candies-to-people/)
- [2928. Distribute Candies Among Children I](../../3001-3500/3199-distribute-candies-among-children-i/)
- [2929. Distribute Candies Among Children II](../../3001-3500/3201-distribute-candies-among-children-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distribute-candies/)
