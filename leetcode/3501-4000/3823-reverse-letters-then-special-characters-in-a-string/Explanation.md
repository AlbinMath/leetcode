# LeetCode 3823: Reverse Letters Then Special Characters in a String

**LeetCode Problem #3823 — Reverse Letters Then Special Characters in a String**
Solve LeetCode Reverse Letters Then Special Characters in a String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Letters Then Special Characters in a String |
| LeetCode | #3823 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters and special characters.

Your task is to perform these **in order**:

**Reverse** the **lowercase letters** and place them back into the positions originally occupied by letters. 
 **Reverse** the **special characters** and place them back into the positions originally occupied by special characters.

Return the resulting string after performing the reversals.

## Constraints
- `1 <= s.length <= 100`
- `s` consists only of lowercase English letters and the special characters in `"!@#$%^&*()"`.

## Examples
### Example 1
- **Input:** `s = " )ebc#da@f( "`
- **Output:** `" (fad@cb#e) "`
- **Explanation:** The letters in the string are `['e', 'b', 'c', 'd', 'a', 'f']`:

 
 Reversing them gives `['f', 'a', 'd', 'c', 'b', 'e']` 
 `s` becomes `")fad#cb@e("` 
 
 
 ​​​​​​​The special characters in the string are `[')', '#', '@', '(']`:
 
 Reversing them gives `['(', '@', '#', ')']` 
 `s` becomes ` " (fad@cb#e) " `

### Example 2
- **Input:** `s = "z"`
- **Output:** `"z"`
- **Explanation:** The string contains only one letter, and reversing it does not change the string. There are no special characters.

### Example 3
- **Input:** `s = "!@#$%^&*()"`
- **Output:** `" )(*&^%$#@! "`
- **Explanation:** The string contains no letters. The string contains all special characters, so reversing the special characters reverses the whole string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reverse Letters Then Special Characters in a String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = " )ebc#da@f( "`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `" (fad@cb#e) "`.
4. **Verification:** The letters in the string are `['e', 'b', 'c', 'd', 'a', 'f']`:

 
 Reversing them gives `['f', 'a', 'd', 'c', 'b', 'e']` 
 `s` becomes `")fad#cb@e("` 
 
 
 ​​​​​​​The special characters in the string are `[')', '#', '@', '(']`:
 
 Reversing them gives `['(', '@', '#', ')']` 
 `s` becomes ` " (fad@cb#e) " `

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
    def reverseByType(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        specials = [c for c in s if not c.isalpha()]
        letters.reverse()
        specials.reverse()

        res = []
        li = si = 0
        for c in s:
            if c.isalpha():
                res.append(letters[li])
                li += 1
            else:
                res.append(specials[si])
                si += 1
        return ''.join(res)
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
- [151. Reverse Words in a String](../../0001-0500/0151-reverse-words-in-a-string/)
- [344. Reverse String](../../0001-0500/0344-reverse-string/)
- [345. Reverse Vowels of a String](../../0001-0500/0345-reverse-vowels-of-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/)
