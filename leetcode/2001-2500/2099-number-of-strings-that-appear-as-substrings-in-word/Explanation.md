# LeetCode 1967: Number of Strings That Appear as Substrings in Word

**LeetCode Problem #1967 — Number of Strings That Appear as Substrings in Word**
Solve LeetCode Number of Strings That Appear as Substrings in Word using Kotlin and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Strings That Appear as Substrings in Word |
| LeetCode | #1967 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of strings `patterns` and a string `word`, return *the **number** of strings in *`patterns`* that exist as a **substring** in *`word`.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= patterns.length <= 100`
- `1 <= patterns[i].length <= 100`
- `1 <= word.length <= 100`
- `patterns[i]` and `word` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `patterns = ["a","abc","bc","d"], word = "abc"`
- **Output:** `3`
- **Explanation:** - "a" appears as a substring in " a bc".
- "abc" appears as a substring in " abc ".
- "bc" appears as a substring in "a bc ".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

### Example 2
- **Input:** `patterns = ["a","b","c"], word = "aaaaabbbbb"`
- **Output:** `2`
- **Explanation:** - "a" appears as a substring in "a a aaabbbbb".
- "b" appears as a substring in "aaaaabbbb b ".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.

### Example 3
- **Input:** `patterns = ["a","a","a"], word = "ab"`
- **Output:** `3`
- **Explanation:** Each of the patterns appears as a substring in word " a b".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
The code iterates through each pattern and checks if it exists as a substring of `word` using the built-in `contains`/`indexOf` method. Count and return the matches.

Time complexity is $O(P \times W)$ where $P$ is total pattern length and $W$ is word length, and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `patterns = ["a","abc","bc","d"], word = "abc"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** - "a" appears as a substring in " a bc".
- "abc" appears as a substring in " abc ".
- "bc" appears as a substring in "a bc ".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

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
Kotlin

## Source Code
- [solution.kt](./solution.kt)


```kotlin
class Solution {
    fun numOfStrings(patterns: Array<String>, word: String): Int {
        var count = 0

        for (pattern in patterns) {
            if (word.contains(pattern)) {
                count++
            }
        }

        return count
    }
}
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
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1469-minimum-number-of-steps-to-make-two-strings-anagram/)
- [1684. Count the Number of Consistent Strings](../../1501-2000/1786-count-the-number-of-consistent-strings/)
- [2023. Number of Pairs of Strings With Concatenation Equal to Target](../../2001-2500/2133-number-of-pairs-of-strings-with-concatenation-equal-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)
