# LeetCode 2273: Find Resultant Array After Removing Anagrams

**LeetCode Problem #2273 — Find Resultant Array After Removing Anagrams**
Solve LeetCode Find Resultant Array After Removing Anagrams using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Resultant Array After Removing Anagrams |
| LeetCode | #2273 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** string array `words`, where `words[i]` consists of lowercase English letters.

In one operation, select any index `i` such that `0 < i < words.length` and `words[i - 1]` and `words[i]` are **anagrams**, and **delete** `words[i]` from `words`. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return `words` *after performing all operations*. It can be shown that selecting the indices for each operation in **any** arbitrary order will lead to the same result.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, `"dacb"` is an anagram of `"abdc"`.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["abba","baba","bbaa","cd","cd"]`
- **Output:** `["abba","cd"]`
- **Explanation:** One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
 Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
 Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
 Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.

### Example 2
- **Input:** `words = ["a","b","c","d","e"]`
- **Output:** `["a","b","c","d","e"]`
- **Explanation:** No two adjacent strings in words are anagrams of each other, so no operations are performed.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Resultant Array After Removing Anagrams**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["abba","baba","bbaa","cd","cd"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["abba","cd"]`.
4. **Verification:** One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
 Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
 Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
 Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var removeAnagrams = function(words) {
    const result = [];
    let previousSignature = "";

    for (const word of words) {
        const signature = word.split("").sort().join("");
        if (signature !== previousSignature) {
            result.push(word);
            previousSignature = signature;
        }
    }

    return result;
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
- [1619. Mean of Array After Removing Some Elements](../../1501-2000/1619-mean-of-array-after-removing-some-elements/)
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2089-find-target-indices-after-sorting-array/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2593-find-score-of-an-array-after-marking-all-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/)
