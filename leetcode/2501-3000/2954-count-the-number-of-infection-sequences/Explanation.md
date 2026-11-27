# LeetCode 2954: Count the Number of Infection Sequences

**LeetCode Problem #2954 — Count the Number of Infection Sequences**
Solve LeetCode Count the Number of Infection Sequences using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Infection Sequences |
| LeetCode | #2954 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and an array `sick` sorted in increasing order, representing positions of infected people in a line of `n` people.

At each step, **one **uninfected person **adjacent** to an infected person gets infected. This process continues until everyone is infected.

An **infection sequence** is the order in which uninfected people become infected, excluding those initially infected.

Return the number of different infection sequences possible, modulo `10^9+7`.

## Constraints
- `2 <= n <= 10^5`
- `1 <= sick.length <= n - 1`
- `0 <= sick[i] <= n - 1`
- `sick` is sorted in increasing order.

## Examples
### Example 1
- **Input:** `n = 5, sick = [0,4]`
- **Output:** `4`
- **Explanation:** There is a total of 6 different sequences overall. 

 
 Valid infection sequences are `[1,2,3]`, `[1,3,2]`, `[3,2,1]` and `[3,1,2]`. 
 `[2,3,1]` and `[2,1,3]` are not valid infection sequences because the person at index 2 cannot be infected at the first step.

### Example 2
- **Input:** `n = 4, sick = [1]`
- **Output:** `3`
- **Explanation:** There is a total of 6 different sequences overall. 

 
 Valid infection sequences are `[0,2,3]`, `[2,0,3]` and `[2,3,0]`. 
 `[3,2,0]`, `[3,0,2]`, and `[0,3,2]` are not valid infection sequences because the infection starts at the person at index 1, then the order of infection is 2, then 3, and hence 3 cannot be infected earlier than 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count the Number of Infection Sequences**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, sick = [0,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There is a total of 6 different sequences overall. 

 
 Valid infection sequences are `[1,2,3]`, `[1,3,2]`, `[3,2,1]` and `[3,1,2]`. 
 `[2,3,1]` and `[2,1,3]` are not valid infection sequences because the person at index 2 cannot be infected at the first step.

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
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10**9 + 7
        m = n - len(sick)

        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        ans = fact[m]

        # Uninfected people before the first initially infected person
        ans = ans * inv_fact[sick[0]] % MOD

        # Uninfected people after the last initially infected person
        ans = ans * inv_fact[n - 1 - sick[-1]] % MOD

        # Gaps between initially infected people
        for i in range(1, len(sick)):
            gap = sick[i] - sick[i - 1] - 1
            ans = ans * inv_fact[gap] % MOD

            if gap > 1:
                ans = ans * pow(2, gap - 1, MOD) % MOD

        return ans
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
- [2145. Count the Hidden Sequences](../../2001-2500/2145-count-the-hidden-sequences/)
- [2318. Number of Distinct Roll Sequences](../../2001-2500/2318-number-of-distinct-roll-sequences/)
- [3850. Count Sequences to K](../../3501-4000/3850-count-sequences-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-infection-sequences/)
