# LeetCode 3035: Maximum Palindromes After Operations

**LeetCode Problem #3035 — Maximum Palindromes After Operations**
Solve LeetCode Maximum Palindromes After Operations using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Palindromes After Operations |
| LeetCode | #3035 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string array `words` having length `n` and containing **0-indexed** strings.

You are allowed to perform the following operation **any** number of times (**including** **zero**):

Choose integers `i`, `j`, `x`, and `y` such that `0 <= i, j < n`, `0 <= x < words[i].length`, `0 <= y < words[j].length`, and **swap** the characters `words[i][x]` and `words[j][y]`.

Return *an integer denoting the **maximum** number of palindromes *`words`* can contain, after performing some operations.*

**Note:** `i` and `j` may be equal during an operation.

## Constraints
- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 100`
- `words[i]` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["abbb","ba","aa"]`
- **Output:** `3`
- **Explanation:** In this example, one way to get the maximum number of palindromes is:
Choose i = 0, j = 1, x = 0, y = 0, so we swap words[0][0] and words[1][0]. words becomes ["bbbb","aa","aa"].
All strings in words are now palindromes.
Hence, the maximum number of palindromes achievable is 3.

### Example 2
- **Input:** `words = ["abc","ab"]`
- **Output:** `2`
- **Explanation:** In this example, one way to get the maximum number of palindromes is: 
Choose i = 0, j = 1, x = 1, y = 0, so we swap words[0][1] and words[1][0]. words becomes ["aac","bb"].
Choose i = 0, j = 0, x = 1, y = 2, so we swap words[0][1] and words[0][2]. words becomes ["aca","bb"].
Both strings are now palindromes.
Hence, the maximum number of palindromes achievable is 2.

### Example 3
- **Input:** `words = ["cd","ef","a"]`
- **Output:** `1`
- **Explanation:** In this example, there is no need to perform any operation.
There is one palindrome in words "a".
It can be shown that it is not possible to get more than one palindrome after any number of operations.
Hence, the answer is 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Palindromes After Operations**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["abbb","ba","aa"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** In this example, one way to get the maximum number of palindromes is:
Choose i = 0, j = 1, x = 0, y = 0, so we swap words[0][0] and words[1][0]. words becomes ["bbbb","aa","aa"].
All strings in words are now palindromes.
Hence, the maximum number of palindromes achievable is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        freq = Counter(ch for word in words for ch in word)
        total_pairs = sum(count // 2 for count in freq.values())
        
        lengths = sorted(len(word) for word in words)
        palindromes = 0
        
        for length in lengths:
            needed_pairs = length // 2
            if total_pairs >= needed_pairs:
                total_pairs -= needed_pairs
                palindromes += 1
            else:
                break
                
        return palindromes
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2317. Maximum XOR After Operations ](../../2001-2500/2402-maximum-xor-after-operations-/)
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3501-4000/3622-maximum-frequency-of-an-element-after-performing-operations-i/)
- [3347. Maximum Frequency of an Element After Performing Operations II](../../3501-4000/3640-maximum-frequency-of-an-element-after-performing-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-palindromes-after-operations/)
