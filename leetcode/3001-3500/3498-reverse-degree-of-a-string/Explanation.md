# LeetCode 3498: Reverse Degree of a String

**LeetCode Problem #3498 — Reverse Degree of a String**
Solve LeetCode Reverse Degree of a String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Degree of a String |
| LeetCode | #3498 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, calculate its **reverse degree**.

The **reverse degree** is calculated as follows:

For each character, multiply its position in the *reversed* alphabet (`'a'` = 26, `'b'` = 25, ..., `'z'` = 1) with its position in the string **(1-indexed)**. 
 Sum these products for all characters in the string.

Return the **reverse degree** of `s`.

## Constraints
- `1 <= s.length <= 1000`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abc"`
- **Output:** `148`
- **Explanation:** Letter 
 Index in Reversed Alphabet 
 Index in String 
 Product 
 
 
 `'a'` 
 26 
 1 
 26 
 
 
 `'b'` 
 25 
 2 
 50 
 
 
 `'c'` 
 24 
 3 
 72 
 
 
 

 The reversed degree is `26 + 50 + 72 = 148`.

### Example 2
- **Input:** `s = "zaza"`
- **Output:** `160`
- **Explanation:** Letter 
 Index in Reversed Alphabet 
 Index in String 
 Product 
 
 
 `'z'` 
 1 
 1 
 1 
 
 
 `'a'` 
 26 
 2 
 52 
 
 
 `'z'` 
 1 
 3 
 3 
 
 
 `'a'` 
 26 
 4 
 104 
 
 
 

 The reverse degree is `1 + 52 + 3 + 104 = 160`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code simply iterates through the string, computing the required product for each character and adding it to a running total.
1. It initializes `total = 0`.
2. It loops through the string using `enumerate(s)`, which gives both the zero-based index `i` and the character `ch`.
3. To calculate the character's value in the reversed alphabet:
   - `ord(ch) - ord('a')` gives the 0-based index in the normal alphabet (e.g., `'a'` is 0, `'z'` is 25).
   - Subtracting this from 26 gives the 1-based index in the reversed alphabet (e.g., `26 - 0 = 26` for `'a'`).
4. The 1-based position in the string is simply `i + 1`.
5. It multiplies the `value` and `position`, adding the result to `total`.
6. After processing all characters, it returns the final `total`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `148`.
4. **Verification:** Letter 
 Index in Reversed Alphabet 
 Index in String 
 Product 
 
 
 `'a'` 
 26 
 1 
 26 
 
 
 `'b'` 
 25 
 2 
 50 
 
 
 `'c'` 
 24 
 3 
 72 
 
 
 

 The reversed degree is `26 + 50 + 72 = 148`.

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
class Solution(object):
    def reverseDegree(self, s):
        total = 0

        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))
            position = i + 1
            total += value * position

        return total
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
[View problem on LeetCode](https://leetcode.com/problems/reverse-degree-of-a-string/)
