# LeetCode 1405: Longest Happy String

**LeetCode Problem #1405 — Longest Happy String**
Solve LeetCode Longest Happy String using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Happy String |
| LeetCode | #1405 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A string `s` is called **happy** if it satisfies the following conditions:

`s` only contains the letters `'a'`, `'b'`, and `'c'`. 
 `s` does not contain any of `"aaa"`, `"bbb"`, or `"ccc"` as a substring. 
 `s` contains **at most** `a` occurrences of the letter `'a'`. 
 `s` contains **at most** `b` occurrences of the letter `'b'`. 
 `s` contains **at most** `c` occurrences of the letter `'c'`.

Given three integers `a`, `b`, and `c`, return *the **longest possible happy **string*. If there are multiple longest happy strings, return *any of them*. If there is no such string, return *the empty string *`""`.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `0 <= a, b, c <= 100`
- `a + b + c > 0`

## Examples
### Example 1
- **Input:** `a = 1, b = 1, c = 7`
- **Output:** `"ccaccbcc"`
- **Explanation:** "ccbccacc" would also be a correct answer.

### Example 2
- **Input:** `a = 7, b = 1, c = 0`
- **Output:** `"aabaa"`
- **Explanation:** It is the only correct answer in this case.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Happy String**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 1, b = 1, c = 7`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ccaccbcc"`.
4. **Verification:** "ccbccacc" would also be a correct answer.

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
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-cnt, ch) for cnt, ch in ((a, 'a'), (b, 'b'), (c, 'c')) if cnt > 0]
        heapq.heapify(heap)
        res = []

        while heap:
            cnt, ch = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                # can't place a third in a row: use the next best letter
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                if cnt2 + 1 < 0:
                    heapq.heappush(heap, (cnt2 + 1, ch2))
                heapq.heappush(heap, (cnt, ch))  # put the blocked letter back
            else:
                res.append(ch)
                if cnt + 1 < 0:
                    heapq.heappush(heap, (cnt + 1, ch))

        return ''.join(res)
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
- [1048. Longest String Chain](../../1001-1500/1048-longest-string-chain/)
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../../1001-1500/1415-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
- [2745. Construct the Longest New String](../../2501-3000/2745-construct-the-longest-new-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-happy-string/)
