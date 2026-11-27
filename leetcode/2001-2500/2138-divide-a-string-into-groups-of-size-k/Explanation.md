# LeetCode 2138: Divide a String Into Groups of Size k

**LeetCode Problem #2138 — Divide a String Into Groups of Size k**
Solve LeetCode Divide a String Into Groups of Size k using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divide a String Into Groups of Size k |
| LeetCode | #2138 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A string `s` can be partitioned into groups of size `k` using the following procedure:

The first group consists of the first `k` characters of the string, the second group consists of the next `k` characters of the string, and so on. Each element can be a part of **exactly one** group. 
 For the last group, if the string **does not** have `k` characters remaining, a character `fill` is used to complete the group.

Note that the partition is done so that after removing the `fill` character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be `s`.

Given the string `s`, the size of each group `k` and the character `fill`, return *a string array denoting the **composition of every group** *`s`* has been divided into, using the above procedure*.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters only.
- `1 <= k <= 100`
- `fill` is a lowercase English letter.

## Examples
### Example 1
- **Input:** `s = "abcdefghi", k = 3, fill = "x"`
- **Output:** `["abc","def","ghi"]`
- **Explanation:** The first 3 characters "abc" form the first group.
The next 3 characters "def" form the second group.
The last 3 characters "ghi" form the third group.
Since all groups can be completely filled by characters from the string, we do not need to use fill.
Thus, the groups formed are "abc", "def", and "ghi".

### Example 2
- **Input:** `s = "abcdefghij", k = 3, fill = "x"`
- **Output:** `["abc","def","ghi","jxx"]`
- **Explanation:** Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Divide a String Into Groups of Size k**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcdefghi", k = 3, fill = "x"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["abc","def","ghi"]`.
4. **Verification:** The first 3 characters "abc" form the first group.
The next 3 characters "def" form the second group.
The last 3 characters "ghi" form the third group.
Since all groups can be completely filled by characters from the string, we do not need to use fill.
Thus, the groups formed are "abc", "def", and "ghi".

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
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s += fill * (-len(s) % k)
        return [s[i:i + k] for i in range(0, len(s), k)]
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
- [1461. Check If a String Contains All Binary Codes of Size K](../../1001-1500/1461-check-if-a-string-contains-all-binary-codes-of-size-k/)
- [2406. Divide Intervals Into Minimum Number of Groups](../../2001-2500/2406-divide-intervals-into-minimum-number-of-groups/)
- [2493. Divide Nodes Into the Maximum Number of Groups](../../2001-2500/2493-divide-nodes-into-the-maximum-number-of-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/)
