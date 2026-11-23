# LeetCode 2075: Decode the Slanted Ciphertext

**LeetCode Problem #2075 — Decode the Slanted Ciphertext**
Solve LeetCode Decode the Slanted Ciphertext using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decode the Slanted Ciphertext |
| LeetCode | #2075 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A string `originalText` is encoded using a **slanted transposition cipher** to a string `encodedText` with the help of a matrix having a **fixed number of rows** `rows`.

`originalText` is placed first in a top-left to bottom-right manner.

The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of `originalText`. The arrow indicates the order in which the cells are filled. All empty cells are filled with `' '`. The number of columns is chosen such that the rightmost column will **not be empty** after filling in `originalText`.

`encodedText` is then formed by appending all characters of the matrix in a row-wise fashion.

The characters in the blue cells are appended first to `encodedText`, then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed.

For example, if `originalText = "cipher"` and `rows = 3`, then we encode it in the following manner:

The blue arrows depict how `originalText` is placed in the matrix, and the red arrows denote the order in which `encodedText` is formed. In the above example, `encodedText = "ch ie pr"`.

Given the encoded string `encodedText` and number of rows `rows`, return *the original string* `originalText`.

**Note:** `originalText` **does not** have any trailing spaces `' '`. The test cases are generated such that there is only one possible `originalText`.

## Constraints
- `0 <= encodedText.length <= 10^6`
- `encodedText` consists of lowercase English letters and `' '` only.
- `encodedText` is a valid encoding of some `originalText` that **does not** have trailing spaces.
- `1 <= rows <= 1000`
- The testcases are generated such that there is **only one** possible `originalText`.

## Examples
### Example 1
- **Input:** `encodedText = "ch ie pr", rows = 3`
- **Output:** `"cipher"`
- **Explanation:** This is the same example described in the problem description.

### Example 2
- **Input:** `encodedText = "iveo eed l te olc", rows = 4`
- **Output:** `"i love leetcode"`
- **Explanation:** The figure above denotes the matrix that was used to encode originalText. 
The blue arrows show how we can find originalText from encodedText.

### Example 3
- **Input:** `encodedText = "coding", rows = 1`
- **Output:** `"coding"`
- **Explanation:** Since there is only 1 row, both originalText and encodedText are the same.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Decode the Slanted Ciphertext**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `encodedText = "ch ie pr", rows = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"cipher"`.
4. **Verification:** This is the same example described in the problem description.

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
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        cols = len(encodedText) // rows
        res = []
        for start in range(cols):
            r, c = 0, start
            while r < rows and c < cols:
                res.append(encodedText[r * cols + c])
                r += 1
                c += 1
        return "".join(res).rstrip()
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
- [91. Decode Ways](../../0001-0500/0091-decode-ways/)
- [394. Decode String](../../0001-0500/0394-decode-string/)
- [535. Encode and Decode TinyURL](../../0501-1000/0535-encode-and-decode-tinyurl/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/decode-the-slanted-ciphertext/)
