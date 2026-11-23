# LeetCode 1684: Count the Number of Consistent Strings

**LeetCode Problem #1684 — Count the Number of Consistent Strings**
Solve LeetCode Count the Number of Consistent Strings using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Consistent Strings |
| LeetCode | #1684 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `allowed` consisting of **distinct** characters and an array of strings `words`. A string is **consistent **if all characters in the string appear in the string `allowed`.

Return* the number of **consistent** strings in the array *`words`.

## Constraints
- `1 <= words.length <= 10^4`
- `1 <= allowed.length <=^ 26`
- `1 <= words[i].length <= 10`
- The characters in `allowed` are **distinct**.
- `words[i]` and `allowed` contain only lowercase English letters.

## Examples
### Example 1
- **Input:** `allowed = "ab", words = ["ad","bd","aaab","baa","badab"]`
- **Output:** `2`
- **Explanation:** Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

### Example 2
- **Input:** `allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]`
- **Output:** `7`
- **Explanation:** All strings are consistent.

### Example 3
- **Input:** `allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]`
- **Output:** `4`
- **Explanation:** Strings "cc", "acd", "ac", and "d" are consistent.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count the Number of Consistent Strings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `allowed = "ab", words = ["ad","bd","aaab","baa","badab"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        bool present[26] = {false};

        // Mark allowed characters
        for (char c : allowed) {
            present[c - 'a'] = true;
        }

        int count = 0;

        // Check each word
        for (string word : words) {
            bool consistent = true;

            for (char c : word) {
                if (!present[c - 'a']) {
                    consistent = false;
                    break;
                }
            }

            if (consistent) {
                count++;
            }
        }

        return count;
    }
};
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
- [2586. Count the Number of Vowel Strings in Range](../../2501-3000/2654-count-the-number-of-vowel-strings-in-range/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [1395. Count Number of Teams](../../1501-2000/1511-count-number-of-teams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-consistent-strings/)
