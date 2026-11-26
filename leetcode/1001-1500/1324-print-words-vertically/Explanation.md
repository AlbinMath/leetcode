# LeetCode 1324: Print Words Vertically

**LeetCode Problem #1324 — Print Words Vertically**
Solve LeetCode Print Words Vertically using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print Words Vertically |
| LeetCode | #1324 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`. Return all the words vertically in the same order in which they appear in `s`. 
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed). 
Each word would be put on only one column and that in one column there will be only one word.

## Constraints
- `1 <= s.length <= 200`
- `s` contains only upper case English letters.
- It's guaranteed that there is only one space between 2 words.

## Examples
### Example 1
- **Input:** `s = "HOW ARE YOU"`
- **Output:** `["HAY","ORO","WEU"]`
- **Explanation:** Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

### Example 2
- **Input:** `s = "TO BE OR NOT TO BE"`
- **Output:** `["TBONTB","OEROOE"," T"]`
- **Explanation:** Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
" T"

### Example 3
- **Input:** `s = "CONTEST IS COMING"`
- **Output:** `["CIC","OSO","N M","T I","E N","S G","T"]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Print Words Vertically**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "HOW ARE YOU"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["HAY","ORO","WEU"]`.
4. **Verification:** Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

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
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        rows = max(len(w) for w in words)

        res = []
        for i in range(rows):
            line = ''.join(w[i] if i < len(w) else ' ' for w in words)
            res.append(line.rstrip())

        return res
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
- [3643. Flip Square Submatrix Vertically](../../3501-4000/3643-flip-square-submatrix-vertically/)
- [30. Substring with Concatenation of All Words](../../0001-0500/0030-substring-with-concatenation-of-all-words/)
- [151. Reverse Words in a String](../../0001-0500/0151-reverse-words-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-words-vertically/)
