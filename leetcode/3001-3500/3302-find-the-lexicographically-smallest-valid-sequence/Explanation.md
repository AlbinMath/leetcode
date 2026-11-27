# LeetCode 3302: Find the Lexicographically Smallest Valid Sequence

**LeetCode Problem #3302 — Find the Lexicographically Smallest Valid Sequence**
Solve LeetCode Find the Lexicographically Smallest Valid Sequence using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Lexicographically Smallest Valid Sequence |
| LeetCode | #3302 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two strings `word1` and `word2`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it *identical* to `y`.

A sequence of indices `seq` is called **valid** if:

The indices are sorted in **ascending** order. 
 *Concatenating* the characters at these indices in `word1` in **the same** order results in a string that is **almost equal** to `word2`.

Return an array of size `word2.length` representing the lexicographically smallest **valid** sequence of indices. If no such sequence of indices exists, return an **empty** array.

**Note** that the answer must represent the *lexicographically smallest array*, **not** the corresponding string formed by those indices.

## Constraints
- `1 <= word2.length < word1.length <= 3 * 10^5`
- `word1` and `word2` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word1 = "vbcca", word2 = "abc"`
- **Output:** `[0,1,2]`
- **Explanation:** The lexicographically smallest valid sequence of indices is `[0, 1, 2]`: 

 
 Change `word1[0]` to `'a'`. 
 `word1[1]` is already `'b'`. 
 `word1[2]` is already `'c'`.

### Example 2
- **Input:** `word1 = "bacdc", word2 = "abc"`
- **Output:** `[1,2,4]`
- **Explanation:** The lexicographically smallest valid sequence of indices is `[1, 2, 4]`: 

 
 `word1[1]` is already `'a'`. 
 Change `word1[2]` to `'b'`. 
 `word1[4]` is already `'c'`.

### Example 3
- **Input:** `word1 = "aaaaaa", word2 = "aaabc"`
- **Output:** `[]`
- **Explanation:** There is no valid sequence of indices.

### Example 4
- **Input:** `word1 = "abc", word2 = "ab"`
- **Output:** `[0,1]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find the Lexicographically Smallest Valid Sequence**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "vbcca", word2 = "abc"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,2]`.
4. **Verification:** The lexicographically smallest valid sequence of indices is `[0, 1, 2]`: 

 
 Change `word1[0]` to `'a'`. 
 `word1[1]` is already `'b'`. 
 `word1[2]` is already `'c'`.

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
    vector<int> validSequence(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();

        // suf[i] = first unmatched position in word2
        // after matching word1[i...n-1] from right to left.
        vector<int> suf(n + 1);
        suf[n] = m;

        int j = m - 1;

        for (int i = n - 1; i >= 0; i--) {
            if (j >= 0 && word1[i] == word2[j]) {
                j--;
            }

            suf[i] = j + 1;
        }

        vector<int> ans;

        bool changed = false;
        j = 0;

        for (int i = 0; i < n; i++) {
            if (j == m)
                break;

            // Normal matching
            if (word1[i] == word2[j]) {
                ans.push_back(i);
                j++;
            }
            // Use the one allowed mismatch
            else if (!changed && suf[i + 1] <= j + 1) {
                ans.push_back(i);
                j++;
                changed = true;
            }
        }

        if (j == m)
            return ans;

        return {};
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
- [1718. Construct the Lexicographically Largest Valid Sequence](../../1501-2000/1718-construct-the-lexicographically-largest-valid-sequence/)
- [903. Valid Permutations for DI Sequence](../../0501-1000/0903-valid-permutations-for-di-sequence/)
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/)
