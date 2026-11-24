# LeetCode 854: K-Similar Strings

**LeetCode Problem #854 — K-Similar Strings**
Solve LeetCode K-Similar Strings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-Similar Strings |
| LeetCode | #854 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Strings `s1` and `s2` are `k`**-similar** (for some non-negative integer `k`) if we can swap the positions of two letters in `s1` exactly `k` times so that the resulting string equals `s2`.

Given two anagrams `s1` and `s2`, return the smallest `k` for which `s1` and `s2` are `k`**-similar**.

## Constraints
- `1 <= s1.length <= 20`
- `s2.length == s1.length`
- `s1` and `s2` contain only lowercase letters from the set `{'a', 'b', 'c', 'd', 'e', 'f'}`.
- `s2` is an anagram of `s1`.

## Examples
### Example 1
- **Input:** `s1 = "ab", s2 = "ba"`
- **Output:** `1`
- **Explanation:** The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".

### Example 2
- **Input:** `s1 = "abc", s2 = "bca"`
- **Output:** `2`
- **Explanation:** The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **K-Similar Strings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "ab", s2 = "ba"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".

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
from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        pairs = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        if not pairs:
            return 0

        start = "".join(c1 for c1, _ in pairs)
        target = "".join(c2 for _, c2 in pairs)
        n = len(start)

        queue = deque([start])
        visited = {start}
        steps = 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                i = 0
                while curr[i] == target[i]:
                    i += 1

                # Check for an optimal 2-cycle swap first
                candidates = []
                for j in range(i + 1, n):
                    if curr[j] == target[i] and curr[j] != target[j]:
                        if curr[i] == target[j]:
                            candidates = [j]
                            break
                        candidates.append(j)

                lst = list(curr)
                for j in candidates:
                    lst[i], lst[j] = lst[j], lst[i]
                    nxt = "".join(lst)
                    if nxt == target:
                        return steps
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
                    lst[i], lst[j] = lst[j], lst[i]

        return steps
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
- [1400. Construct K Palindrome Strings](../../1501-2000/1502-construct-k-palindrome-strings/)
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../../1501-2000/1516-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
- [2506. Count Pairs Of Similar Strings](../../2501-3000/2594-count-pairs-of-similar-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-similar-strings/)
