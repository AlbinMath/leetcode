# LeetCode 2284: Sender With Largest Word Count

**LeetCode Problem #2284 — Sender With Largest Word Count**
Solve LeetCode Sender With Largest Word Count using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sender With Largest Word Count |
| LeetCode | #2284 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have a chat log of `n` messages. You are given two string arrays `messages` and `senders` where `messages[i]` is a **message** sent by `senders[i]`.

A **message** is list of **words** that are separated by a single space with no leading or trailing spaces. The **word count** of a sender is the total number of **words** sent by the sender. Note that a sender may send more than one message.

Return *the sender with the **largest** word count*. If there is more than one sender with the largest word count, return *the one with the **lexicographically largest** name*.

**Note:**

Uppercase letters come before lowercase letters in lexicographical order. 
 `"Alice"` and `"alice"` are distinct.

## Constraints
- `n == messages.length == senders.length`
- `1 <= n <= 10^4`
- `1 <= messages[i].length <= 100`
- `1 <= senders[i].length <= 10`
- `messages[i]` consists of uppercase and lowercase English letters and `' '`.
- All the words in `messages[i]` are separated by **a single space**.
- `messages[i]` does not have leading or trailing spaces.
- `senders[i]` consists of uppercase and lowercase English letters only.

## Examples
### Example 1
- **Input:** `messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]`
- **Output:** `"Alice"`
- **Explanation:** Alice sends a total of 2 + 3 = 5 words.
userTwo sends a total of 2 words.
userThree sends a total of 3 words.
Since Alice has the largest word count, we return "Alice".

### Example 2
- **Input:** `messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]`
- **Output:** `"Charlie"`
- **Explanation:** Bob sends a total of 5 words.
Charlie sends a total of 5 words.
Since there is a tie for the largest word count, we return the sender with the lexicographically larger name, Charlie.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sender With Largest Word Count**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Alice"`.
4. **Verification:** Alice sends a total of 2 + 3 = 5 words.
userTwo sends a total of 2 words.
userThree sends a total of 3 words.
Since Alice has the largest word count, we return "Alice".

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
from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        word_counts = defaultdict(int)
        max_words = 0
        best_sender = ""
        
        for sender, msg in zip(senders, messages):
            word_counts[sender] += msg.count(' ') + 1
            if (word_counts[sender], sender) > (max_words, best_sender):
                max_words = word_counts[sender]
                best_sender = sender
                
        return best_sender
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
- [1399. Count Largest Group](../../1001-1500/1500-count-largest-group/)
- [3926. Count Valid Word Occurrences](../../4001-4500/4293-count-valid-word-occurrences/)
- [84. Largest Rectangle in Histogram](../../0001-0500/0084-largest-rectangle-in-histogram/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sender-with-largest-word-count/)
