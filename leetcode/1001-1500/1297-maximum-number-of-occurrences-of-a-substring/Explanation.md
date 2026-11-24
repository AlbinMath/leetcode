# LeetCode 1297: Maximum Number of Occurrences of a Substring

**LeetCode Problem #1297 — Maximum Number of Occurrences of a Substring**
Solve LeetCode Maximum Number of Occurrences of a Substring using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Occurrences of a Substring |
| LeetCode | #1297 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s`, return the maximum number of occurrences of **any** substring under the following rules:

The number of unique characters in the substring must be less than or equal to `maxLetters`. 
 The substring size must be between `minSize` and `maxSize` inclusive.

## Constraints
- `1 <= s.length <= 10^5`
- `1 <= maxLetters <= 26`
- `1 <= minSize <= maxSize <= min(26, s.length)`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4`
- **Output:** `2`
- **Explanation:** Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

### Example 2
- **Input:** `s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3`
- **Output:** `2`
- **Explanation:** Substring "aaa" occur 2 times in the string. It can overlap.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Number of Occurrences of a Substring**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

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
#include <string>
#include <string_view>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        int n = s.length();
        int freq[26] = {0};
        int distinct = 0;
        int max_occ = 0;
        
        unordered_map<string_view, int> counts;
        counts.reserve(n);
        string_view sv(s);
        
        for (int i = 0; i < n; ++i) {
            if (freq[s[i] - 'a']++ == 0) {
                distinct++;
            }
            
            if (i >= minSize) {
                if (--freq[s[i - minSize] - 'a'] == 0) {
                    distinct--;
                }
            }
            
            if (i >= minSize - 1 && distinct <= maxLetters) {
                string_view sub = sv.substr(i - minSize + 1, minSize);
                max_occ = max(max_occ, ++counts[sub]);
            }
        }
        
        return max_occ;
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
- [1456. Maximum Number of Vowels in a Substring of Given Length](../../1001-1500/1456-maximum-number-of-vowels-in-a-substring-of-given-length/)
- [3090. Maximum Length Substring With Two Occurrences](../../3001-3500/3090-maximum-length-substring-with-two-occurrences/)
- [1668. Maximum Repeating Substring](../../1501-2000/1668-maximum-repeating-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/)
