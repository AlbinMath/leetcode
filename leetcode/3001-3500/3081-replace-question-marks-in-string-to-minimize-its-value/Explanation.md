# LeetCode 3081: Replace Question Marks in String to Minimize Its Value

**LeetCode Problem #3081 — Replace Question Marks in String to Minimize Its Value**
Solve LeetCode Replace Question Marks in String to Minimize Its Value using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Replace Question Marks in String to Minimize Its Value |
| LeetCode | #3081 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s`. `s[i]` is either a lowercase English letter or `'?'`.

For a string `t` having length `m` containing **only** lowercase English letters, we define the function `cost(i)` for an index `i` as the number of characters **equal** to `t[i]` that appeared before it, i.e. in the range `[0, i - 1]`.

The **value** of `t` is the **sum** of `cost(i)` for all indices `i`.

For example, for the string `t = "aab"`:

`cost(0) = 0` 
 `cost(1) = 1` 
 `cost(2) = 0` 
 Hence, the value of `"aab"` is `0 + 1 + 0 = 1`.

Your task is to **replace all** occurrences of `'?'` in `s` with any lowercase English letter so that the **value** of `s` is **minimized**.

Return *a string denoting the modified string with replaced occurrences of *`'?'`*. If there are multiple strings resulting in the **minimum value**, return the lexicographically smallest one.*

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either a lowercase English letter or `'?'`.

## Examples
### Example 1
- **Input:** `s = "???"`
- **Output:** `"abc"`
- **Explanation:** In this example, we can replace the occurrences of `'?'` to make `s` equal to `"abc"`. 

 For `"abc"`, `cost(0) = 0`, `cost(1) = 0`, and `cost(2) = 0`. 

 The value of `"abc"` is `0`. 

 Some other modifications of `s` that have a value of `0` are `"cba"`, `"abz"`, and, `"hey"`. 

 Among all of them, we choose the lexicographically smallest.

### Example 2
- **Input:** `s = "a?a?"`
- **Output:** `"abac"`
- **Explanation:** In this example, the occurrences of `'?'` can be replaced to make `s` equal to `"abac"`. 

 For `"abac"`, `cost(0) = 0`, `cost(1) = 0`, `cost(2) = 1`, and `cost(3) = 0`. 

 The value of `"abac"` is `1`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Replace Question Marks in String to Minimize Its Value**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "???"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abc"`.
4. **Verification:** In this example, we can replace the occurrences of `'?'` to make `s` equal to `"abc"`. 

 For `"abc"`, `cost(0) = 0`, `cost(1) = 0`, and `cost(2) = 0`. 

 The value of `"abc"` is `0`. 

 Some other modifications of `s` that have a value of `0` are `"cba"`, `"abz"`, and, `"hey"`. 

 Among all of them, we choose the lexicographically smallest.

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
import heapq
from collections import Counter

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        freq = Counter(ch for ch in s if ch != '?')
        q_count = s.count('?')
        
        heap = [(freq[chr(ord('a') + i)], chr(ord('a') + i)) for i in range(26)]
        heapq.heapify(heap)
        
        replacements = []
        for _ in range(q_count):
            count, ch = heapq.heappop(heap)
            replacements.append(ch)
            heapq.heappush(heap, (count + 1, ch))
            
        replacements.sort()
        
        res = list(s)
        idx = 0
        for i, ch in enumerate(res):
            if ch == '?':
                res[i] = replacements[idx]
                idx += 1
                
        return "".join(res)
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
- [833. Find And Replace in String](../../0501-1000/0833-find-and-replace-in-string/)
- [1234. Replace the Substring for Balanced String](../../1001-1500/1234-replace-the-substring-for-balanced-string/)
- [1663. Smallest String With A Given Numeric Value](../../1501-2000/1663-smallest-string-with-a-given-numeric-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/)
