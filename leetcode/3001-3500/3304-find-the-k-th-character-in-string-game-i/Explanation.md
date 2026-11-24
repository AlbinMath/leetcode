# LeetCode 3304: Find the K-th Character in String Game I

**LeetCode Problem #3304 — Find the K-th Character in String Game I**
Solve LeetCode Find the K-th Character in String Game I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the K-th Character in String Game I |
| LeetCode | #3304 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a **positive** integer `k`.

Now Bob will ask Alice to perform the following operation **forever**:

Generate a new string by **changing** each character in `word` to its **next** character in the English alphabet, and **append** it to the *original* `word`.

For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the `k^th` character in `word`, after enough operations have been done for `word` to have **at least** `k` characters.

## Constraints
- `1 <= k <= 500`

## Examples
### Example 1
- **Input:** `k = 5`
- **Output:** `"b"`
- **Explanation:** Initially, `word = "a"`. We need to do the operation three times: 

 
 Generated string is `"b"`, `word` becomes `"ab"`. 
 Generated string is `"bc"`, `word` becomes `"abbc"`. 
 Generated string is `"bccd"`, `word` becomes `"abbcbccd"`.

### Example 2
- **Input:** `k = 10`
- **Output:** `"c"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the K-th Character in String Game I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"b"`.
4. **Verification:** Initially, `word = "a"`. We need to do the operation three times: 

 
 Generated string is `"b"`, `word` becomes `"ab"`. 
 Generated string is `"bc"`, `word` becomes `"abbc"`. 
 Generated string is `"bccd"`, `word` becomes `"abbcbccd"`.

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
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + bin(k - 1).count('1'))
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
- [3307. Find the K-th Character in String Game II](../../3001-3500/3307-find-the-k-th-character-in-string-game-ii/)
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../../1001-1500/1415-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
- [3154. Find Number of Ways to Reach the K-th Stair](../../3001-3500/3154-find-number-of-ways-to-reach-the-k-th-stair/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/)
