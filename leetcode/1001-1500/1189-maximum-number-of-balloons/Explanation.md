# LeetCode 1189: Maximum Number of Balloons

**LeetCode Problem #1189 — Maximum Number of Balloons**
Solve LeetCode Maximum Number of Balloons using Kotlin and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Balloons |
| LeetCode | #1189 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

## Constraints
- `1 <= text.length <= 10^4`
- `text` consists of lower case English letters only.

## Examples
### Example 1
- **Input:** `text = "nlaebolko"`
- **Output:** `1`

### Example 2
- **Input:** `text = "loonbalxballpoon"`
- **Output:** `2`

### Example 3
- **Input:** `text = "leetcode"`
- **Output:** `0`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
1. **Count Characters:** Count the frequency of every character in the text.
2. **Check Required Characters:** The word "balloon" needs: `b`×1, `a`×1, `l`×2, `o`×2, `n`×1.
3. **Bottleneck:** The answer is the minimum of: count of `b`, count of `a`, count of `l` divided by 2, count of `o` divided by 2, and count of `n`. The character with the smallest available count determines how many complete "balloon"s can be formed.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `text = "nlaebolko"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

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
Kotlin

## Source Code
- [solution.kt](./solution.kt)


```kotlin
class Solution {
    fun maxNumberOfBalloons(text: String): Int {
        val count = IntArray(26)

        for (c in text) {
            count[c - 'a']++
        }

        val b = count['b' - 'a']
        val a = count['a' - 'a']
        val l = count['l' - 'a'] / 2
        val o = count['o' - 'a'] / 2
        val n = count['n' - 'a']

        return minOf(a, b, l, o, n)
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
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)
- [414. Third Maximum Number](../../0001-0500/0414-third-maximum-number/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1072-flip-columns-for-maximum-number-of-equal-rows/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)
