# LeetCode 1307: Verbal Arithmetic Puzzle

**LeetCode Problem #1307 — Verbal Arithmetic Puzzle**
Solve LeetCode Verbal Arithmetic Puzzle using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Verbal Arithmetic Puzzle |
| LeetCode | #1307 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an equation, represented by `words` on the left side and the `result` on the right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9). 
 No two characters can map to the same digit. 
 Each `words[i]` and `result` are decoded as one number **without** leading zeros. 
 Sum of numbers on the left side (`words`) will equal to the number on the right side (`result`).

Return `true` *if the equation is solvable, otherwise return* `false`.

## Constraints
- `2 <= words.length <= 5`
- `1 <= words[i].length, result.length <= 7`
- `words[i], result` contain only uppercase English letters.
- The number of different characters used in the expression is at most `10`.

## Examples
### Example 1
- **Input:** `words = ["SEND","MORE"], result = "MONEY"`
- **Output:** `true`
- **Explanation:** Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" , 9567 + 1085 = 10652

### Example 2
- **Input:** `words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"`
- **Output:** `true`
- **Explanation:** Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" , 650 + 68782 + 68782 = 138214

### Example 3
- **Input:** `words = ["LEET","CODE"], result = "POINT"`
- **Output:** `false`
- **Explanation:** There is no possible mapping to satisfy the equation, so we return false.
Note that two different characters cannot map to the same digit.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Verbal Arithmetic Puzzle**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["SEND","MORE"], result = "MONEY"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" , 9567 + 1085 = 10652

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if max(len(w) for w in words) > len(result):
            return False

        L = len(result)
        leading = set()
        for w in words + [result]:
            if len(w) > 1:
                leading.add(w[0])

        # reversed strings so index = column from the right
        rev_words = [w[::-1] for w in words]
        rev_res = result[::-1]

        assign = {}          # letter -> digit
        used = [False] * 10

        def solve(col: int, wi: int, carry: int, total: int) -> bool:
            # col: current column, wi: next word index to process in this column
            # total: running sum of word digits in this column (plus carry)
            if col == L:
                return carry == 0

            if wi < len(rev_words):
                w = rev_words[wi]
                if col >= len(w):
                    return solve(col, wi + 1, carry, total)
                ch = w[col]
                if ch in assign:
                    return solve(col, wi + 1, carry, total + assign[ch])
                for d in range(10):
                    if used[d] or (d == 0 and ch in leading):
                        continue
                    used[d] = True
                    assign[ch] = d
                    if solve(col, wi + 1, carry, total + d):
                        return True
                    del assign[ch]
                    used[d] = False
                return False

            # all words handled for this column: check the result digit
            s = total + carry
            ch = rev_res[col]
            need = s % 10
            if ch in assign:
                if assign[ch] != need:
                    return False
                return solve(col + 1, 0, s // 10, 0)
            if used[need] or (need == 0 and ch in leading):
                return False
            used[need] = True
            assign[ch] = need
            if solve(col + 1, 0, s // 10, 0):
                return True
            del assign[ch]
            used[need] = False
            return False

        return solve(0, 0, 0, 0)
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [413. Arithmetic Slices](../../0001-0500/0413-arithmetic-slices/)
- [446. Arithmetic Slices II - Subsequence](../../0001-0500/0446-arithmetic-slices-ii---subsequence/)
- [1502. Can Make Arithmetic Progression From Sequence](../../1501-2000/1626-can-make-arithmetic-progression-from-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/verbal-arithmetic-puzzle/)
