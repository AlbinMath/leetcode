# LeetCode 2182: Construct String With Repeat Limit

**LeetCode Problem #2182 — Construct String With Repeat Limit**
Solve LeetCode Construct String With Repeat Limit using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct String With Repeat Limit |
| LeetCode | #2182 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and an integer `repeatLimit`. Construct a new string `repeatLimitedString` using the characters of `s` such that no letter appears **more than** `repeatLimit` times **in a row**. You do **not** have to use all characters from `s`.

Return *the **lexicographically largest** *`repeatLimitedString` *possible*.

A string `a` is **lexicographically larger** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`. If the first `min(a.length, b.length)` characters do not differ, then the longer string is the lexicographically larger one.

## Constraints
- `1 <= repeatLimit <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "cczazcc", repeatLimit = 3`
- **Output:** `"zzcccac"`
- **Explanation:** We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

### Example 2
- **Input:** `s = "aababab", repeatLimit = 2`
- **Output:** `"bbabaa"`
- **Explanation:** We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Construct String With Repeat Limit**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "cczazcc", repeatLimit = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"zzcccac"`.
4. **Verification:** We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

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
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
            
        ans = []
        curr = 25       # Largest available character ('z')
        next_char = 24  # Next largest available separator character
        
        while curr >= 0:
            if freq[curr] == 0:
                curr -= 1
                continue
                
            use = min(freq[curr], repeatLimit)
            ans.append(chr(curr + ord('a')) * use)
            freq[curr] -= use
            
            if freq[curr] > 0:
                next_char = min(next_char, curr - 1)
                while next_char >= 0 and freq[next_char] == 0:
                    next_char -= 1
                    
                if next_char < 0:
                    break
                    
                ans.append(chr(next_char + ord('a')))
                freq[next_char] -= 1
                
        return "".join(ans)
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
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)
- [2375. Construct Smallest Number From DI String](../../2001-2500/2456-construct-smallest-number-from-di-string/)
- [2745. Construct the Longest New String](../../2501-3000/2850-construct-the-longest-new-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-string-with-repeat-limit/)
