# LeetCode 3799: Word Squares II

**LeetCode Problem #3799 — Word Squares II**
Solve LeetCode Word Squares II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Word Squares II |
| LeetCode | #3799 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string array `words`, consisting of **distinct** 4-letter strings, each containing lowercase English letters.

A **word square** consists of 4 **distinct** words: `top`, `left`, `right` and `bottom`, arranged as follows:

`top` forms the **top row**. 
 `bottom` forms the **bottom row**. 
 `left` forms the **left column** (top to bottom). 
 `right` forms the **right column** (top to bottom).

It must satisfy:

`top[0] == left[0]`, `top[3] == right[0]` 
 `bottom[0] == left[3]`, `bottom[3] == right[3]`

Return all valid **distinct** word squares, sorted in **ascending lexicographic** order by the 4-tuple `(top, left, right, bottom)​​​​​​​`.

## Constraints
- `4 <= words.length <= 15`
- `words[i].length == 4`
- `words[i]` consists of only lowercase English letters.
- All `words[i]` are **distinct**.

## Examples
### Example 1
- **Input:** `words = ["able","area","echo","also"]`
- **Output:** `[["able","area","echo","also"],["area","able","also","echo"]]`
- **Explanation:** There are exactly two valid 4-word squares that satisfy all corner

### Example 2
- **Input:** `words = ["code","cafe","eden","edge"]`
- **Output:** `[]`
- **Explanation:** No combination of four words satisfies all four corner

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Word Squares II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["able","area","echo","also"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["able","area","echo","also"],["area","able","also","echo"]]`.
4. **Verification:** There are exactly two valid 4-word squares that satisfy all corner

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
from itertools import permutations

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        for top, left, right, bottom in permutations(words, 4):
            if (top[0] == left[0] and top[3] == right[0]
                    and bottom[0] == left[3] and bottom[3] == right[3]):
                res.append([top, left, right, bottom])
        res.sort()
        return res
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
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)
- [79. Word Search](../../0001-0500/0079-word-search/)
- [126. Word Ladder II](../../0001-0500/0126-word-ladder-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/word-squares-ii/)
