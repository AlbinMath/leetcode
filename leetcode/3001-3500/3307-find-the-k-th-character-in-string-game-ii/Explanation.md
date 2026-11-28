# LeetCode 3307: Find the K-th Character in String Game II

**LeetCode Problem #3307 — Find the K-th Character in String Game II**
Solve LeetCode Find the K-th Character in String Game II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the K-th Character in String Game II |
| LeetCode | #3307 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a **positive** integer `k`. You are also given an integer array `operations`, where `operations[i]` represents the **type** of the `i^th` operation.

Now Bob will ask Alice to perform **all** operations in sequence:

If `operations[i] == 0`, **append** a copy of `word` to itself. 
 If `operations[i] == 1`, generate a new string by **changing** each character in `word` to its **next** character in the English alphabet, and **append** it to the *original* `word`. For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the `k^th` character in `word` after performing all the operations.

**Note** that the character `'z'` can be changed to `'a'` in the second type of operation.

## Constraints
- `1 <= k <= 10^14`
- `1 <= operations.length <= 100`
- `operations[i]` is either 0 or 1.
- The input is generated such that `word` has **at least** `k` characters after all operations.

## Examples
### Example 1
- **Input:** `k = 5, operations = [0,0,0]`
- **Output:** `"a"`
- **Explanation:** Initially, `word == "a"`. Alice performs the three operations as follows: 

 
 Appends `"a"` to `"a"`, `word` becomes `"aa"`. 
 Appends `"aa"` to `"aa"`, `word` becomes `"aaaa"`. 
 Appends `"aaaa"` to `"aaaa"`, `word` becomes `"aaaaaaaa"`.

### Example 2
- **Input:** `k = 10, operations = [0,1,0,1]`
- **Output:** `"b"`
- **Explanation:** Initially, `word == "a"`. Alice performs the four operations as follows: 

 
 Appends `"a"` to `"a"`, `word` becomes `"aa"`. 
 Appends `"bb"` to `"aa"`, `word` becomes `"aabb"`. 
 Appends `"aabb"` to `"aabb"`, `word` becomes `"aabbaabb"`. 
 Appends `"bbccbbcc"` to `"aabbaabb"`, `word` becomes `"aabbaabbbbccbbcc"`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the K-th Character in String Game II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 5, operations = [0,0,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"a"`.
4. **Verification:** Initially, `word == "a"`. Alice performs the three operations as follows: 

 
 Appends `"a"` to `"a"`, `word` becomes `"aa"`. 
 Appends `"aa"` to `"aa"`, `word` becomes `"aaaa"`. 
 Appends `"aaaa"` to `"aaaa"`, `word` becomes `"aaaaaaaa"`.

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
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        p = k - 1
        shift = 0
        for i, op in enumerate(operations):
            if (p >> i) & 1:
                shift += op
        return chr(ord('a') + shift % 26)
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
- [3304. Find the K-th Character in String Game I](../../3001-3500/3304-find-the-k-th-character-in-string-game-i/)
- [719. Find K-th Smallest Pair Distance](../../0501-1000/0719-find-k-th-smallest-pair-distance/)
- [3154. Find Number of Ways to Reach the K-th Stair](../../3001-3500/3154-find-number-of-ways-to-reach-the-k-th-stair/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/)
