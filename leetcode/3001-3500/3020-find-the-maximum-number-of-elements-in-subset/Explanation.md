# LeetCode 3020: Find the Maximum Number of Elements in Subset

**LeetCode Problem #3020 — Find the Maximum Number of Elements in Subset**
Solve LeetCode Find the Maximum Number of Elements in Subset using Java and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Maximum Number of Elements in Subset |
| LeetCode | #3020 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of **positive** integers `nums`.

You need to select a subset of `nums` which satisfies the following condition:

You can place the selected elements in a **0-indexed** array such that it follows the pattern: `[x, x^2, x^4, ..., x^k/2, x^k, x^k/2, ..., x^4, x^2, x]` (**Note** that `k` can be any **non-negative** power of `2`). For example, `[2, 4, 16, 4, 2]` and `[3, 9, 3]` follow the pattern while `[2, 4, 8, 4, 2]` does not.

Return *the **maximum** number of elements in a subset that satisfies these conditions.*

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,4,1,2,2]`
- **Output:** `3`
- **Explanation:** We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 2^2 == 4. Hence the answer is 3.

### Example 2
- **Input:** `nums = [1,3,2,4]`
- **Output:** `1`
- **Explanation:** We can select the subset {1}, which can be placed in the array as [1] which follows the pattern. Hence the answer is 1. Note that we could have also selected the subsets {2}, {3}, or {4}, there may be multiple subsets which provide the same answer.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find the Maximum Number of Elements in Subset**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,4,1,2,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 2^2 == 4. Hence the answer is 3.

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
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.*;

class Solution {
    public int maximumLength(int[] nums) {
        Map<Long, Integer> freq = new HashMap<>();

        for (int num : nums) {
            long x = num;
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }

        int ans = 1;

        for (long x : freq.keySet()) {

            // Special case: all elements are 1
            if (x == 1) {
                int count = freq.get(1L);

                // Length must be odd
                if (count % 2 == 0) {
                    count--;
                }

                ans = Math.max(ans, count);
                continue;
            }

            // x must appear at least twice
            if (freq.get(x) < 2) {
                continue;
            }

            int len = 1;
            long cur = x;

            while (true) {
                // Prevent overflow
                if (cur > 1_000_000_000L / cur) {
                    break;
                }

                long next = cur * cur;

                Integer count = freq.get(next);

                // next doesn't exist
                if (count == null) {
                    break;
                }

                // One copy is enough for the center
                len += 2;

                // Only one copy -> this is the center
                if (count < 2) {
                    break;
                }

                // Two copies -> can continue
                cur = next;
            }

            ans = Math.max(ans, len);
        }

        return ans;
    }
}
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
- [3113. Find the Number of Subarrays Where Boundary Elements Are Maximum](../../3001-3500/3113-find-the-number-of-subarrays-where-boundary-elements-are-maximum/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2744. Find Maximum Number of String Pairs](../../2501-3000/2744-find-maximum-number-of-string-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/)
