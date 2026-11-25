# LeetCode 1309: Decrypt String from Alphabet to Integer Mapping

**LeetCode Problem #1309 — Decrypt String from Alphabet to Integer Mapping**
Solve LeetCode Decrypt String from Alphabet to Integer Mapping using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decrypt String from Alphabet to Integer Mapping |
| LeetCode | #1309 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` formed by digits and `'#'`. We want to map `s` to English lowercase characters as follows:

Characters (`'a'` to `'i'`) are represented by (`'1'` to `'9'`) respectively. 
 Characters (`'j'` to `'z'`) are represented by (`'10#'` to `'26#'`) respectively.

Return *the string formed after mapping*.

The test cases are generated so that a unique mapping will always exist.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of digits and the `'#'` letter.
- `s` will be a valid string such that mapping is always possible.

## Examples
### Example 1
- **Input:** `s = "10#11#12"`
- **Output:** `"jkab"`
- **Explanation:** "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

### Example 2
- **Input:** `s = "1326#"`
- **Output:** `"acz"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Decrypt String from Alphabet to Integer Mapping**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "10#11#12"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"jkab"`.
4. **Verification:** "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i + 2])
                i += 3
            else:
                num = int(s[i])
                i += 1

            result.append(chr(num + 96))

        return ''.join(result)
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)
- [988. Smallest String Starting From Leaf](../../0501-1000/0988-smallest-string-starting-from-leaf/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/)
