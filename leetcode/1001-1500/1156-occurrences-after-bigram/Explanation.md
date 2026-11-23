# LeetCode 1078: Occurrences After Bigram

**LeetCode Problem #1078 — Occurrences After Bigram**
Solve LeetCode Occurrences After Bigram using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Occurrences After Bigram |
| LeetCode | #1078 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `first` and `second`, consider occurrences in some text of the form `"first second third"`, where `second` comes immediately after `first`, and `third` comes immediately after `second`.

Return *an array of all the words* `third` *for each occurrence of* `"first second third"`.

## Constraints
- `1 <= text.length <= 1000`
- `text` consists of lowercase English letters and spaces.
- All the words in `text` are separated by **a single space**.
- `1 <= first.length, second.length <= 10`
- `first` and `second` consist of lowercase English letters.
- `text` will not have any leading or trailing spaces.

## Examples
### Example 1
- **Input:** `text = "alice is a good girl she is a good student", first = "a", second = "good"`
- **Output:** `["girl","student"]`

### Example 2
- **Input:** `text = "we will we will rock you", first = "we", second = "will"`
- **Output:** `["we","rock"]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Occurrences After Bigram**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = "alice is a good girl she is a good student", first = "a", second = "good"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["girl","student"]`.

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
    def findOcurrences(
        self, text: str, first: str, second: str
    ) -> List[str]:
        words = text.split()
        result = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])

        return result
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
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3501-4000/3688-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)
- [1207. Unique Number of Occurrences](../../1001-1500/1319-unique-number-of-occurrences/)
- [1297. Maximum Number of Occurrences of a Substring](../../1001-1500/1423-maximum-number-of-occurrences-of-a-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/occurrences-after-bigram/)
