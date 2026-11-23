# LeetCode 3597: Partition String 

**LeetCode Problem #3597 — Partition String **
Solve LeetCode Partition String  using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition String  |
| LeetCode | #3597 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, partition it into **unique segments** according to the following procedure:

Start building a segment beginning at index 0. 
 Continue extending the current segment character by character until the current segment has not been seen before. 
 Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index. 
 Repeat until you reach the end of `s`.

Return an array of strings `segments`, where `segments[i]` is the `i^th` segment created.

## Constraints
- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abbccccd"`
- **Output:** `["a","b","bc","c","cc","d"]`
- **Explanation:** Index 
 Segment After Adding 
 Seen Segments 
 Current Segment Seen Before? 
 New Segment 
 Updated Seen Segments 
 
 
 0 
 "a" 
 [] 
 No 
 "" 
 ["a"] 
 
 
 1 
 "b" 
 ["a"] 
 No 
 "" 
 ["a", "b"] 
 
 
 2 
 "b" 
 ["a", "b"] 
 Yes 
 "b" 
 ["a", "b"] 
 
 
 3 
 "bc" 
 ["a", "b"] 
 No 
 "" 
 ["a", "b", "bc"] 
 
 
 4 
 "c" 
 ["a", "b", "bc"] 
 No 
 "" 
 ["a", "b", "bc", "c"] 
 
 
 5 
 "c" 
 ["a", "b", "bc", "c"] 
 Yes 
 "c" 
 ["a", "b", "bc", "c"] 
 
 
 6 
 "cc" 
 ["a", "b", "bc", "c"] 
 No 
 "" 
 ["a", "b", "bc", "c", "cc"] 
 
 
 7 
 "d" 
 ["a", "b", "bc", "c", "cc"] 
 No 
 "" 
 ["a", "b", "bc", "c", "cc", "d"] 
 
 
 

 Hence, the final output is `["a", "b", "bc", "c", "cc", "d"]`.

### Example 2
- **Input:** `s = "aaaa"`
- **Output:** `["a","aa"]`
- **Explanation:** Index 
 Segment After Adding 
 Seen Segments 
 Current Segment Seen Before? 
 New Segment 
 Updated Seen Segments 
 
 
 0 
 "a" 
 [] 
 No 
 "" 
 ["a"] 
 
 
 1 
 "a" 
 ["a"] 
 Yes 
 "a" 
 ["a"] 
 
 
 2 
 "aa" 
 ["a"] 
 No 
 "" 
 ["a", "aa"] 
 
 
 3 
 "a" 
 ["a", "aa"] 
 Yes 
 "a" 
 ["a", "aa"] 
 
 
 

 Hence, the final output is `["a", "aa"]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Partition String **, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abbccccd"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["a","b","bc","c","cc","d"]`.
4. **Verification:** Index 
 Segment After Adding 
 Seen Segments 
 Current Segment Seen Before? 
 New Segment 
 Updated Seen Segments 
 
 
 0 
 "a" 
 [] 
 No 
 "" 
 ["a"] 
 
 
 1 
 "b" 
 ["a"] 
 No 
 "" 
 ["a", "b"] 
 
 
 2 
 "b" 
 ["a", "b"] 
 Yes 
 "b" 
 ["a", "b"] 
 
 
 3 
 "bc" 
 ["a", "b"] 
 No 
 "" 
 ["a", "b", "bc"] 
 
 
 4 
 "c" 
 ["a", "b", "bc"] 
 No 
 "" 
 ["a", "b", "bc", "c"] 
 
 
 5 
 "c" 
 ["a", "b", "bc", "c"] 
 Yes 
 "c" 
 ["a", "b", "bc", "c"] 
 
 
 6 
 "cc" 
 ["a", "b", "bc", "c"] 
 No 
 "" 
 ["a", "b", "bc", "c", "cc"] 
 
 
 7 
 "d" 
 ["a", "b", "bc", "c", "cc"] 
 No 
 "" 
 ["a", "b", "bc", "c", "cc", "d"] 
 
 
 

 Hence, the final output is `["a", "b", "bc", "c", "cc", "d"]`.

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

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        cur = []
        for ch in s:
            cur.append(ch)
            seg = ''.join(cur)
            if seg not in seen:
                seen.add(seg)
                res.append(seg)
                cur = []
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
- [2767. Partition String Into Minimum Beautiful Substrings](../../2501-3000/2883-partition-string-into-minimum-beautiful-substrings/)
- [3864. Minimum Cost to Partition a Binary String](../../4001-4500/4192-minimum-cost-to-partition-a-binary-string/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-string/)
