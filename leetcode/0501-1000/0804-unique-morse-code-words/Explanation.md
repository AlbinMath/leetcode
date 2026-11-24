# LeetCode 804: Unique Morse Code Words

**LeetCode Problem #804 — Unique Morse Code Words**
Solve LeetCode Unique Morse Code Words using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Morse Code Words |
| LeetCode | #804 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

`'a'` maps to `".-"`, 
 `'b'` maps to `"-..."`, 
 `'c'` maps to `"-.-."`, and so on.

For convenience, the full table for the `26` letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter.

For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and `"-..."`. We will call such a concatenation the **transformation** of a word.

Return *the number of different **transformations** among all words we have*.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 12`
- `words[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["gin","zen","gig","msg"]`
- **Output:** `2`
- **Explanation:** The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

### Example 2
- **Input:** `words = ["a"]`
- **Output:** `1`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Unique Morse Code Words**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["gin","zen","gig","msg"]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        transformations = set()

        for word in words:
            code = ""

            for ch in word:
                code += morse[ord(ch) - ord('a')]

            transformations.add(code)

        return len(transformations)
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [89. Gray Code](../../0001-0500/0089-gray-code/)
- [62. Unique Paths](../../0001-0500/0062-unique-paths/)
- [63. Unique Paths II](../../0001-0500/0063-unique-paths-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-morse-code-words/)
