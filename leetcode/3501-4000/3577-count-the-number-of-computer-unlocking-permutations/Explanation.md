# LeetCode 3577: Count the Number of Computer Unlocking Permutations

**LeetCode Problem #3577 — Count the Number of Computer Unlocking Permutations**
Solve LeetCode Count the Number of Computer Unlocking Permutations using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Computer Unlocking Permutations |
| LeetCode | #3577 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `complexity` of length `n`.

There are `n` **locked** computers in a room with labels from 0 to `n - 1`, each with its own **unique** password. The password of the computer `i` has a complexity `complexity[i]`.

The password for the computer labeled 0 is **already** decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:

You can decrypt the password for the computer `i` using the password for computer `j`, where `j` is **any** integer less than `i` with a lower complexity. (i.e. `j < i` and `complexity[j] < complexity[i]`) 
 To decrypt the password for computer `i`, you must have already unlocked a computer `j` such that `j < i` and `complexity[j] < complexity[i]`.

Find the number of permutations of `[0, 1, 2, ..., (n - 1)]` that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.

Since the answer may be large, return it **modulo** 10^9 + 7.

**Note** that the password for the computer **with label** 0 is decrypted, and *not* the computer with the first position in the permutation.

## Constraints
- `2 <= complexity.length <= 10^5`
- `1 <= complexity[i] <= 10^9`

## Examples
### Example 1
- **Input:** `complexity = [1,2,3]`
- **Output:** `2`
- **Explanation:** The valid permutations are: 

 
 [0, 1, 2]
 
 Unlock computer 0 first with root password. 
 Unlock computer 1 with password of computer 0 since `complexity[0] < complexity[1]`. 
 Unlock computer 2 with password of computer 1 since `complexity[1] < complexity[2]`. 
 
 
 [0, 2, 1]
 
 Unlock computer 0 first with root password. 
 Unlock computer 2 with password of computer 0 since `complexity[0] < complexity[2]`. 
 Unlock computer 1 with password of computer 0 since `complexity[0] < complexity[1]`.

### Example 2
- **Input:** `complexity = [3,3,3,4,4,4]`
- **Output:** `0`
- **Explanation:** There are no possible permutations which can unlock all computers.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count the Number of Computer Unlocking Permutations**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `complexity = [1,2,3]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The valid permutations are: 

 
 [0, 1, 2]
 
 Unlock computer 0 first with root password. 
 Unlock computer 1 with password of computer 0 since `complexity[0] < complexity[1]`. 
 Unlock computer 2 with password of computer 1 since `complexity[1] < complexity[2]`. 
 
 
 [0, 2, 1]
 
 Unlock computer 0 first with root password. 
 Unlock computer 2 with password of computer 0 since `complexity[0] < complexity[2]`. 
 Unlock computer 1 with password of computer 0 since `complexity[0] < complexity[1]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        c0 = complexity[0]
        for v in complexity[1:]:
            if v <= c0:
                return 0
        ans = 1
        for i in range(2, len(complexity)):
            ans = ans * i % MOD
        return ans
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3343. Count Number of Balanced Permutations](../../3001-3500/3343-count-number-of-balanced-permutations/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)
- [1395. Count Number of Teams](../../1001-1500/1395-count-number-of-teams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/)
