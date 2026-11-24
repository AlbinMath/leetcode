# LeetCode 1941: Check if All Characters Have Equal Number of Occurrences

**LeetCode Problem #1941 — Check if All Characters Have Equal Number of Occurrences**
Solve LeetCode Check if All Characters Have Equal Number of Occurrences using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if All Characters Have Equal Number of Occurrences |
| LeetCode | #1941 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s`, return `true`* if *`s`* is a **good** string, or *`false`* otherwise*.

A string `s` is **good** if **all** the characters that appear in `s` have the **same** number of occurrences (i.e., the same frequency).

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abacbc"`
- **Output:** `true`
- **Explanation:** The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

### Example 2
- **Input:** `s = "aaabb"`
- **Output:** `false`
- **Explanation:** The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Check if All Characters Have Equal Number of Occurrences**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abacbc"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool areOccurrencesEqual(string s) {
        int freq[26] = {0};

        for (char c : s) {
            freq[c - 'a']++;
        }

        int expected = 0;

        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                if (expected == 0) {
                    expected = freq[i];
                } else if (freq[i] != expected) {
                    return false;
                }
            }
        }

        return true;
    }
};
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
- [2283. Check if Number Has Equal Digit Count and Digit Value](../../2001-2500/2283-check-if-number-has-equal-digit-count-and-digit-value/)
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1358-number-of-substrings-containing-all-three-characters/)
- [1437. Check If All 1's Are at Least Length K Places Away](../../1001-1500/1437-check-if-all-1s-are-at-least-length-k-places-away/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/)
