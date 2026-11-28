# LeetCode 3981: Count Distinct Ways to Form Target from Two Strings

**LeetCode Problem #3981 — Count Distinct Ways to Form Target from Two Strings**
Solve LeetCode Count Distinct Ways to Form Target from Two Strings using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Distinct Ways to Form Target from Two Strings |
| LeetCode | #3981 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given three strings `word1`, `word2`, and `target`.

Your task is to count the number of ways to form `target` by choosing characters from `word1` and `word2` under the following conditions:

For each character of `target`, choose one matching character from either `word1` or `word2`. 
 The chosen indices from `word1` must be **strictly** increasing. 
 The chosen indices from `word2` must be **strictly** increasing. 
 **At least** one character must be chosen from **both** `word1` and `word2`.

Two ways are considered different if, for **at least** one position in `target`, the chosen character comes from a different string or a different index.

Return the number of ways. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= word1.length, word2.length, target.length <= 100`
- `word1`, `word2`, and `target` consist of lowercase English letters only.

## Examples
### Example 1
- **Input:** `word1 = "abc", word2 = "bac", target = "abc"`
- **Output:** `5`
- **Explanation:** There are 5 ways to form `target`: 

 
 `word1[0] = 'a'`, `word1[1] = 'b'`, `word2[2] = 'c'` 
 `word1[0] = 'a'`, `word2[0] = 'b'`, `word1[2] = 'c'` 
 `word1[0] = 'a'`, `word2[0] = 'b'`, `word2[2] = 'c'` 
 `word2[1] = 'a'`, `word1[1] = 'b'`, `word1[2] = 'c'` 
 `word2[1] = 'a'`, `word1[1] = 'b'`, `word2[2] = 'c'` 
 

 All ways preserve the increasing index order inside each string and choose at least one character from each string.

### Example 2
- **Input:** `word1 = "cd", word2 = "cd", target = "ccd"`
- **Output:** `4`
- **Explanation:** There are 4 ways to form `target`: 

 
 `word1[0] = 'c'`, `word2[0] = 'c'`, `word1[1] = 'd'` 
 `word1[0] = 'c'`, `word2[0] = 'c'`, `word2[1] = 'd'` 
 `word2[0] = 'c'`, `word1[0] = 'c'`, `word1[1] = 'd'` 
 `word2[0] = 'c'`, `word1[0] = 'c'`, `word2[1] = 'd'` 
 

 The first two `'c'` characters in `target` must come one from each string. The final `'d'` can be chosen from either string.

### Example 3
- **Input:** `word1 = "xy", word2 = "xy", target = "xyxy"`
- **Output:** `2`
- **Explanation:** There are 2 ways to form `target`: 

 
 `word1[0] = 'x'`, `word1[1] = 'y'`, `word2[0] = 'x'`, `word2[1] = 'y'` 
 `word2[0] = 'x'`, `word2[1] = 'y'`, `word1[0] = 'x'`, `word1[1] = 'y'` 
 

 Each `"xy"` part in `target` comes entirely from one string.

### Example 4
- **Input:** `word1 = "ab", word2 = "cde", target = "ace"`
- **Output:** `1`
- **Explanation:** The only way is to choose `word1[0] = 'a'`, `word2[0] = 'c'`, and `word2[2] = 'e'`. Thus, the answer is 1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Distinct Ways to Form Target from Two Strings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "abc", word2 = "bac", target = "abc"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** There are 5 ways to form `target`: 

 
 `word1[0] = 'a'`, `word1[1] = 'b'`, `word2[2] = 'c'` 
 `word1[0] = 'a'`, `word2[0] = 'b'`, `word1[2] = 'c'` 
 `word1[0] = 'a'`, `word2[0] = 'b'`, `word2[2] = 'c'` 
 `word2[1] = 'a'`, `word1[1] = 'b'`, `word1[2] = 'c'` 
 `word2[1] = 'a'`, `word1[1] = 'b'`, `word2[2] = 'c'` 
 

 All ways preserve the increasing index order inside each string and choose at least one character from each string.

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
class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        MOD = 10**9 + 7
        n, m = len(word1), len(word2)

        cur = [[0] * (m + 1) for _ in range(n + 1)]
        cur[0][0] = 1

        for c in target:
            R = [[0] * (m + 1) for _ in range(n + 1)]
            C = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                for j in range(m + 1):
                    R[i][j] = (cur[i][j] + (R[i - 1][j] if i else 0)) % MOD
                    C[i][j] = (cur[i][j] + (C[i][j - 1] if j else 0)) % MOD

            new = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                for j in range(m + 1):
                    v = 0
                    if i >= 1 and word1[i - 1] == c:
                        v += R[i - 1][j]
                    if j >= 1 and word2[j - 1] == c:
                        v += C[i][j - 1]
                    new[i][j] = v % MOD
            cur = new

        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                res += cur[i][j]
        return res % MOD
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
- [2605. Form Smallest Number From Two Digit Arrays](../../2501-3000/2605-form-smallest-number-from-two-digit-arrays/)
- [3725. Count Ways to Choose Coprime Integers from Rows](../../3501-4000/3725-count-ways-to-choose-coprime-integers-from-rows/)
- [1639. Number of Ways to Form a Target String Given a Dictionary](../../1501-2000/1639-number-of-ways-to-form-a-target-string-given-a-dictionary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/)
