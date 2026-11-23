# LeetCode 3093: Longest Common Suffix Queries

**LeetCode Problem #3093 — Longest Common Suffix Queries**
Solve LeetCode Longest Common Suffix Queries using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Common Suffix Queries |
| LeetCode | #3093 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two arrays of strings `wordsContainer` and `wordsQuery`.

For each `wordsQuery[i]`, you need to find a string from `wordsContainer` that has the **longest common suffix** with `wordsQuery[i]`. If there are two or more strings in `wordsContainer` that share the longest common suffix, find the string that is the **smallest** in length. If there are two or more such strings that have the **same** smallest length, find the one that occurred **earlier** in `wordsContainer`.

Return *an array of integers *`ans`*, where *`ans[i]`* is the index of the string in *`wordsContainer`* that has the **longest common suffix** with *`wordsQuery[i]`*.*

## Constraints
- `1 <= wordsContainer.length, wordsQuery.length <= 10^4`
- `1 <= wordsContainer[i].length <= 5 * 10^3`
- `1 <= wordsQuery[i].length <= 5 * 10^3`
- `wordsContainer[i]` consists only of lowercase English letters.
- `wordsQuery[i]` consists only of lowercase English letters.
- Sum of `wordsContainer[i].length` is at most `5 * 10^5`.
- Sum of `wordsQuery[i].length` is at most `5 * 10^5`.

## Examples
### Example 1
- **Input:** `wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]`
- **Output:** `[1,1,1]`
- **Explanation:** Let's look at each `wordsQuery[i]` separately: 

 
 For `wordsQuery[0] = "cd"`, strings from `wordsContainer` that share the longest common suffix `"cd"` are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3. 
 For `wordsQuery[1] = "bcd"`, strings from `wordsContainer` that share the longest common suffix `"bcd"` are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3. 
 For `wordsQuery[2] = "xyz"`, there is no string from `wordsContainer` that shares a common suffix. Hence the longest common suffix is `""`, that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.

### Example 2
- **Input:** `wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]`
- **Output:** `[2,0,2]`
- **Explanation:** Let's look at each `wordsQuery[i]` separately: 

 
 For `wordsQuery[0] = "gh"`, strings from `wordsContainer` that share the longest common suffix `"gh"` are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6. 
 For `wordsQuery[1] = "acbfgh"`, only the string at index 0 shares the longest common suffix `"fgh"`. Hence it is the answer, even though the string at index 2 is shorter. 
 For `wordsQuery[2] = "acbfegh"`, strings from `wordsContainer` that share the longest common suffix `"gh"` are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Common Suffix Queries**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,1,1]`.
4. **Verification:** Let's look at each `wordsQuery[i]` separately: 

 
 For `wordsQuery[0] = "cd"`, strings from `wordsContainer` that share the longest common suffix `"cd"` are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3. 
 For `wordsQuery[1] = "bcd"`, strings from `wordsContainer` that share the longest common suffix `"bcd"` are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3. 
 For `wordsQuery[2] = "xyz"`, there is no string from `wordsContainer` that shares a common suffix. Hence the longest common suffix is `""`, that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.

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
class Solution(object):

    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """

        # Trie represented using dictionaries.
        # Each node:
        # [children, best_index]
        trie = [
            [{}, -1]
        ]

        # Find the best container index according to:
        # 1. shortest length
        # 2. smallest index
        def better(i, j):
            if j == -1:
                return i

            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return i

            if len(wordsContainer[i]) > len(wordsContainer[j]):
                return j

            return min(i, j)

        # --------------------------------------------------
        # Build Trie using reversed container strings
        # --------------------------------------------------

        for idx, word in enumerate(wordsContainer):

            node = 0

            # Root represents empty suffix.
            trie[node][1] = better(idx, trie[node][1])

            for ch in reversed(word):

                children = trie[node][0]

                if ch not in children:
                    children[ch] = len(trie)
                    trie.append([{}, -1])

                node = children[ch]

                trie[node][1] = better(idx, trie[node][1])

        # --------------------------------------------------
        # Answer queries
        # --------------------------------------------------

        answer = []

        for word in wordsQuery:

            node = 0

            # At least the empty suffix is always shared.
            best = trie[0][1]

            for ch in reversed(word):

                children = trie[node][0]

                if ch not in children:
                    break

                node = children[ch]

                # This node represents a longer common suffix.
                best = trie[node][1]

            answer.append(best)

        return answer
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
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [1143. Longest Common Subsequence](../../1001-1500/1250-longest-common-subsequence/)
- [1923. Longest Common Subpath](../../2001-2500/2051-longest-common-subpath/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-common-suffix-queries/)
