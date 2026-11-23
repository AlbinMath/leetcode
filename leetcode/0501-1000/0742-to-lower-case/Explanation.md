# LeetCode 709: To Lower Case

**LeetCode Problem #709 — To Lower Case**
Solve LeetCode To Lower Case using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | To Lower Case |
| LeetCode | #709 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return *the string after replacing every uppercase letter with the same lowercase letter*.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of printable ASCII characters.

## Examples
### Example 1
- **Input:** `s = "Hello"`
- **Output:** `"hello"`

### Example 2
- **Input:** `s = "here"`
- **Output:** `"here"`

### Example 3
- **Input:** `s = "LOVELY"`
- **Output:** `"lovely"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **To Lower Case**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "Hello"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"hello"`.

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
    def toLowerCase(self, s: str) -> str:
        return s.lower()
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
- [2309. Greatest English Letter in Upper and Lower Case](../../1001-1500/1363-greatest-english-letter-in-upper-and-lower-case/)
- [784. Letter Case Permutation](../../0501-1000/0800-letter-case-permutation/)
- [374. Guess Number Higher or Lower](../../0001-0500/0374-guess-number-higher-or-lower/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/to-lower-case/)
