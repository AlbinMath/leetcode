# LeetCode 2468: Split Message Based on Limit

**LeetCode Problem #2468 — Split Message Based on Limit**
Solve LeetCode Split Message Based on Limit using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Message Based on Limit |
| LeetCode | #2468 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string, `message`, and a positive integer, `limit`.

You must **split** `message` into one or more **parts** based on `limit`. Each resulting part should have the suffix `"<a/b>"`, where `"b"` is to be **replaced** with the total number of parts and `"a"` is to be **replaced** with the index of the part, starting from `1` and going up to `b`. Additionally, the length of each resulting part (including its suffix) should be **equal** to `limit`, except for the last part whose length can be **at most** `limit`.

The resulting parts should be formed such that when their suffixes are removed and they are all concatenated **in order**, they should be equal to `message`. Also, the result should contain as few parts as possible.

Return* the parts *`message`* would be split into as an array of strings*. If it is impossible to split `message` as required, return* an empty array*.

## Constraints
- `1 <= message.length <= 10^4`
- `message` consists only of lowercase English letters and `' '`.
- `1 <= limit <= 10^4`

## Examples
### Example 1
- **Input:** `message = "this is really a very awesome message", limit = 9`
- **Output:** `["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]`
- **Explanation:** The first 9 parts take 3 characters each from the beginning of message.
The next 5 parts take 2 characters each to finish splitting message. 
In this example, each part, including the last, has length 9. 
It can be shown it is not possible to split message into less than 14 parts.

### Example 2
- **Input:** `message = "short message", limit = 15`
- **Output:** `["short mess<1/2>","age<2/2>"]`
- **Explanation:** Under the given

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Split Message Based on Limit**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `message = "this is really a very awesome message", limit = 9`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]`.
4. **Verification:** The first 9 parts take 3 characters each from the beginning of message.
The next 5 parts take 2 characters each to finish splitting message. 
In this example, each part, including the last, has length 9. 
It can be shown it is not possible to split message into less than 14 parts.

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
class Solution(object):
    def splitMessage(self, message, limit):
        n = len(message)
        b = 0
        prefix_a_digits = 0

        while True:
            b += 1
            len_b = len(str(b))
            # Even the final part "<b/b>" must leave at least 1 character for message
            if 3 + 2 * len_b >= limit:
                return []

            prefix_a_digits += len_b
            total_suffix = 3 * b + prefix_a_digits + b * len_b
            if b * limit - total_suffix >= n:
                break

        res = []
        idx = 0
        for a in range(1, b + 1):
            suffix = "<{}/{}>".format(a, b)
            take = limit - len(suffix)
            res.append(message[idx:idx + take] + suffix)
            idx += take

        return res
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
- [981. Time Based Key-Value Store](../../1001-1500/1023-time-based-key-value-store/)
- [2151. Maximum Good People Based on Statements](../../2001-2500/2272-maximum-good-people-based-on-statements/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1501-2000/1549-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-message-based-on-limit/)
