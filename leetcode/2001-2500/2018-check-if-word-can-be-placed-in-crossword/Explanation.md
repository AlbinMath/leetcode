# LeetCode 2018: Check if Word Can Be Placed In Crossword

**LeetCode Problem #2018 — Check if Word Can Be Placed In Crossword**
Solve LeetCode Check if Word Can Be Placed In Crossword using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Word Can Be Placed In Crossword |
| LeetCode | #2018 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` matrix `board`, representing the** current **state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), `' '` to represent any **empty **cells, and `'#'` to represent any **blocked** cells.

A word can be placed** horizontally** (left to right **or** right to left) or **vertically** (top to bottom **or** bottom to top) in the board if:

It does not occupy a cell containing the character `'#'`. 
 The cell each letter is placed in must either be `' '` (empty) or **match** the letter already on the `board`. 
 There must not be any empty cells `' '` or other lowercase letters **directly left or right**** **of the word if the word was placed **horizontally**. 
 There must not be any empty cells `' '` or other lowercase letters **directly above or below** the word if the word was placed **vertically**.

Given a string `word`, return `true`* if *`word`* can be placed in *`board`*, or *`false`* **otherwise***.

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m * n <= 2 * 10^5`
- `board[i][j]` will be `' '`, `'#'`, or a lowercase English letter.
- `1 <= word.length <= max(m, n)`
- `word` will contain only lowercase English letters.

## Examples
### Example 1
- **Input:** `board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"`
- **Output:** `true`
- **Explanation:** The word "abc" can be placed as shown above (top to bottom).

### Example 2
- **Input:** `board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"`
- **Output:** `false`
- **Explanation:** It is impossible to place the word because there will always be a space/letter above or below it.

### Example 3
- **Input:** `board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"`
- **Output:** `true`
- **Explanation:** The word "ca" can be placed as shown above (right to left).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Word Can Be Placed In Crossword**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The word "abc" can be placed as shown above (top to bottom).

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
    def placeWordInCrossword(self, board, word):
        n = len(word)
        rev = word[::-1]

        def can_fit(line):
            for slot in "".join(line).split("#"):
                if len(slot) == n:
                    if all(c == " " or c == w for c, w in zip(slot, word)):
                        return True
                    if all(c == " " or c == w for c, w in zip(slot, rev)):
                        return True
            return False

        for row in board:
            if can_fit(row):
                return True

        for col in zip(*board):
            if can_fit(col):
                return True

        return False
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
- [2116. Check if a Parentheses String Can Be Valid](../../2001-2500/2116-check-if-a-parentheses-string-can-be-valid/)
- [2840. Check if Strings Can be Made Equal With Operations II](../../2501-3000/2840-check-if-strings-can-be-made-equal-with-operations-ii/)
- [3394. Check if Grid can be Cut into Sections](../../3001-3500/3394-check-if-grid-can-be-cut-into-sections/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/)
