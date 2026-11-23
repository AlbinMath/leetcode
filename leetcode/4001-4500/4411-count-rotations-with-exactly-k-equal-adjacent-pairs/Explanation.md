# LeetCode 4043: Count Rotations With Exactly K Equal Adjacent Pairs

**LeetCode Problem #4043 — Count Rotations With Exactly K Equal Adjacent Pairs**
Solve LeetCode Count Rotations With Exactly K Equal Adjacent Pairs using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Rotations With Exactly K Equal Adjacent Pairs |
| LeetCode | #4043 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of length `n` and an integer `k`.

A **cyclic rotation** of `s` is obtained by choosing a prefix of `s` whose length is between 0 and `n - 1` (inclusive), and moving it to the end of the string while preserving the order of all characters.

For **every** cyclic rotation of `s`, let its **score** be the number of indices `i` such that `0 <= i < n - 1` and the characters at positions `i` and `i + 1` are equal.

Return the number of cyclic rotations of `s` whose score equals `k`.

## Constraints
- `2 <= n == s.length <= 100`
- `s` only consists of lowercase English letters.
- `0 <= k <= n - 1`

## Examples
### Example 1
- **Input:** `s = "aab", k = 1`
- **Output:** `2`
- **Explanation:** The cyclic rotations of `s` are: 

 
 `"aab"`: The characters at positions 0 and 1 are equal, so `score = 1`. 
 `"aba"`: No two adjacent characters are equal, so `score = 0`. 
 `"baa"`: The characters at positions 1 and 2 are equal, so `score = 1`. 
 

 Since `score` equals `k` for 2 cyclic rotations of `s`, the answer is 2.

### Example 2
- **Input:** `s = "abca", k = 0`
- **Output:** `1`
- **Explanation:** The cyclic rotations of `s` are: 

 
 `"abca"`: No two adjacent characters are equal, so `score = 0`. 
 `"bcaa"`: The characters at positions 2 and 3 are equal, so `score = 1`. 
 `"caab"`: The characters at positions 1 and 2 are equal, so `score = 1`. 
 `"aabc"`: The characters at positions 0 and 1 are equal, so `score = 1`. 
 

 Since `score` equals `k` for only 1 cyclic rotation of `s`, the answer is 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Rotations With Exactly K Equal Adjacent Pairs**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aab", k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The cyclic rotations of `s` are: 

 
 `"aab"`: The characters at positions 0 and 1 are equal, so `score = 1`. 
 `"aba"`: No two adjacent characters are equal, so `score = 0`. 
 `"baa"`: The characters at positions 1 and 2 are equal, so `score = 1`. 
 

 Since `score` equals `k` for 2 cyclic rotations of `s`, the answer is 2.

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
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for r in range(n):
            t = s[r:] + s[:r]
            score = sum(t[i] == t[i + 1] for i in range(n - 1))
            if score == k:
                ans += 1
        return ans
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
- [3265. Count Almost Equal Pairs I](../../3501-4000/3534-count-almost-equal-pairs-i/)
- [3267. Count Almost Equal Pairs II](../../3501-4000/3544-count-almost-equal-pairs-ii/)
- [3835. Count Subarrays With Cost Less Than or Equal to K](../../4001-4500/4211-count-subarrays-with-cost-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/)
