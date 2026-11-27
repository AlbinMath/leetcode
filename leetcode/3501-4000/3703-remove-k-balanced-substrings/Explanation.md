# LeetCode 3703: Remove K-Balanced Substrings

**LeetCode Problem #3703 — Remove K-Balanced Substrings**
Solve LeetCode Remove K-Balanced Substrings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove K-Balanced Substrings |
| LeetCode | #3703 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of `'('` and `')'`, and an integer `k`.

A **string** is **k-balanced** if it is **exactly** `k` **consecutive** `'('` followed by `k` **consecutive** `')'`, i.e., `'(' * k + ')' * k`.

For example, if `k = 3`, k-balanced is `"((()))"`.

You must **repeatedly** remove all **non-overlapping k-balanced substrings ** from `s`, and then join the remaining parts. Continue this process until no k-balanced **substring** exists.

Return the final string after all possible removals.

​​​​​​​

## Constraints
- `2 <= s.length <= 10^5`
- `s` consists only of `'('` and `')'`.
- `1 <= k <= s.length / 2`

## Examples
### Example 1
- **Input:** `s = "(())", k = 1`
- **Output:** `""`
- **Explanation:** k-balanced substring is `"()"` 

 
 
 
 Step 
 Current `s` 
 `k-balanced` 
 Result `s` 
 
 
 
 
 1 
 `(())` 
 (

### Example 2
- **Input:** `s = "(()(", k = 1`
- **Output:** `"(("`
- **Explanation:** k-balanced substring is `"()"` 

 
 
 
 Step 
 Current `s` 
 `k-balanced` 
 Result `s` 
 
 
 
 
 1 
 `(()(` 
 (

### Example 3
- **Input:** `s = "((()))()()()", k = 3`
- **Output:** `"()()()"`
- **Explanation:** k-balanced substring is `"((()))"` 

 
 
 
 Step 
 Current `s` 
 `k-balanced` 
 Result `s` 
 
 
 
 
 1 
 `((()))()()()`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove K-Balanced Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "(())", k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `""`.
4. **Verification:** k-balanced substring is `"()"` 

 
 
 
 Step 
 Current `s` 
 `k-balanced` 
 Result `s` 
 
 
 
 
 1 
 `(())` 
 (

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
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []  # list of [char, count]
        
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
                
            if stk[-1][0] == ')' and stk[-1][1] == k:
                if len(stk) >= 2 and stk[-2][0] == '(' and stk[-2][1] >= k:
                    stk.pop()
                    stk[-1][1] -= k
                    if stk[-1][1] == 0:
                        stk.pop()
                        
        return "".join(ch * cnt for ch, cnt in stk)
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
- [3669. Balanced K-Factor Decomposition](../../3501-4000/3669-balanced-k-factor-decomposition/)
- [3258. Count Substrings That Satisfy K-Constraint I](../../3001-3500/3258-count-substrings-that-satisfy-k-constraint-i/)
- [3261. Count Substrings That Satisfy K-Constraint II](../../3001-3500/3261-count-substrings-that-satisfy-k-constraint-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-k-balanced-substrings/)
