# LeetCode 3039: Apply Operations to Make String Empty

**LeetCode Problem #3039 — Apply Operations to Make String Empty**
Solve LeetCode Apply Operations to Make String Empty using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Operations to Make String Empty |
| LeetCode | #3039 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s`.

Consider performing the following operation until `s` becomes **empty**:

For **every** alphabet character from `'a'` to `'z'`, remove the **first** occurrence of that character in `s` (if it exists).

For example, let initially `s = "aabcbbca"`. We do the following operations:

Remove the underlined characters `s = " **a** a** bc **bbca"`. The resulting string is `s = "abbca"`. 
 Remove the underlined characters `s = " **ab** b **c** a"`. The resulting string is `s = "ba"`. 
 Remove the underlined characters `s = " **ba** "`. The resulting string is `s = ""`.

Return *the value of the string *`s`* right **before** applying the **last** operation*. In the example above, answer is `"ba"`.

## Constraints
- `1 <= s.length <= 5 * 10^5`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aabcbbca"`
- **Output:** `"ba"`
- **Explanation:** Explained in the statement.

### Example 2
- **Input:** `s = "abcd"`
- **Output:** `"abcd"`
- **Explanation:** We do the following operation:
- Remove the underlined characters s = "

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Apply Operations to Make String Empty**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aabcbbca"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ba"`.
4. **Verification:** Explained in the statement.

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
from collections import Counter

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = Counter(s)
        max_freq = max(freq.values())
        
        seen = set()
        result = []
        
        for ch in reversed(s):
            if freq[ch] == max_freq and ch not in seen:
                seen.add(ch)
                result.append(ch)
                
        return "".join(reversed(result))
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
- [2870. Minimum Number of Operations to Make Array Empty](../../3001-3500/3094-minimum-number-of-operations-to-make-array-empty/)
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1941-minimum-number-of-operations-to-make-string-sorted/)
- [2546. Apply Bitwise Operations to Make Strings Equal](../../2501-3000/2632-apply-bitwise-operations-to-make-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-operations-to-make-string-empty/)
