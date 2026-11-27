# LeetCode 1061: Lexicographically Smallest Equivalent String

**LeetCode Problem #1061 — Lexicographically Smallest Equivalent String**
Solve LeetCode Lexicographically Smallest Equivalent String using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest Equivalent String |
| LeetCode | #1061 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings of the same length `s1` and `s2` and a string `baseStr`.

We say `s1[i]` and `s2[i]` are equivalent characters.

For example, if `s1 = "abc"` and `s2 = "cde"`, then we have `'a' == 'c'`, `'b' == 'd'`, and `'c' == 'e'`.

Equivalent characters follow the usual rules of any equivalence relation:

**Reflexivity:** `'a' == 'a'`. 
 **Symmetry:** `'a' == 'b'` implies `'b' == 'a'`. 
 **Transitivity:** `'a' == 'b'` and `'b' == 'c'` implies `'a' == 'c'`.

For example, given the equivalency information from `s1 = "abc"` and `s2 = "cde"`, `"acd"` and `"aab"` are equivalent strings of `baseStr = "eed"`, and `"aab"` is the lexicographically smallest equivalent string of `baseStr`.

Return *the lexicographically smallest equivalent string of *`baseStr`* by using the equivalency information from *`s1`* and *`s2`.

## Constraints
- `1 <= s1.length, s2.length, baseStr <= 1000`
- `s1.length == s2.length`
- `s1`, `s2`, and `baseStr` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s1 = "parker", s2 = "morris", baseStr = "parser"`
- **Output:** `"makkek"`
- **Explanation:** Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".

### Example 2
- **Input:** `s1 = "hello", s2 = "world", baseStr = "hold"`
- **Output:** `"hdld"`
- **Explanation:** Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".

### Example 3
- **Input:** `s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"`
- **Output:** `"aauaaaaada"`
- **Explanation:** We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Lexicographically Smallest Equivalent String**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "parker", s2 = "morris", baseStr = "parser"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"makkek"`.
4. **Verification:** Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".

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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            rx, ry = find(x), find(y)
            if rx != ry:
                # Always attach the lexicographically larger root to the smaller one
                if rx < ry:
                    parent[ry] = rx
                else:
                    parent[rx] = ry

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        res = []
        for ch in baseStr:
            root_char = chr(find(ord(ch) - ord('a')) + ord('a'))
            res.append(root_char)

        return "".join(res)
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
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)
- [2434. Using a Robot to Print the Lexicographically Smallest String](../../2001-2500/2434-using-a-robot-to-print-the-lexicographically-smallest-string/)
- [2663. Lexicographically Smallest Beautiful String](../../2501-3000/2663-lexicographically-smallest-beautiful-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/)
