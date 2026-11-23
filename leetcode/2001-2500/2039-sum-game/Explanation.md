# LeetCode 1927: Sum Game

**LeetCode Problem #1927 — Sum Game**
Solve LeetCode Sum Game using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum Game |
| LeetCode | #1927 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob take turns playing a game, with **Alice**** starting first**.

You are given a string `num` of **even length** consisting of digits and `'?'` characters. On each turn, a player will do the following if there is still at least one `'?'` in `num`:

Choose an index `i` where `num[i] == '?'`. 
 Replace `num[i]` with any digit between `'0'` and `'9'`.

The game ends when there are no more `'?'` characters in `num`.

For Bob to win, the sum of the digits in the first half of `num` must be **equal** to the sum of the digits in the second half. For Alice to win, the sums must **not be equal**.

For example, if the game ended with `num = "243801"`, then Bob wins because `2+4+3 = 8+0+1`. If the game ended with `num = "243803"`, then Alice wins because `2+4+3 != 8+0+3`.

Assuming Alice and Bob play **optimally**, return `true` *if Alice will win and *`false` *if Bob will win*.

## Constraints
- `2 <= num.length <= 10^5`
- `num.length` is **even**.
- `num` consists of only digits and `'?'`.

## Examples
### Example 1
- **Input:** `num = "5023"`
- **Output:** `false`
- **Explanation:** There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.

### Example 2
- **Input:** `num = "25??"`
- **Output:** `true`
- **Explanation:** Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.

### Example 3
- **Input:** `num = "?3295???"`
- **Output:** `false`
- **Explanation:** It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first '?' with '9'. num = "93295???".
- Bob replaces one of the '?' in the right half with '9'. num = "932959??".
- Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
- Bob replaces the last '?' in the right half with '7'. num = "93295927".
Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code counts the number of `?` marks and digit sums in each half. If the total `?` count is odd, Alice always wins (she has the last move). If even, Bob wins only if he can balance the sums, which requires the sum difference to be exactly `9 * (question marks difference / 2)`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `num = "5023"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();
        int diff = 0;
        int q = 0;

        for (int i = 0; i < n / 2; i++) {
            if (num[i] == '?')
                q++;
            else
                diff += num[i] - '0';
        }

        for (int i = n / 2; i < n; i++) {
            if (num[i] == '?')
                q--;
            else
                diff -= num[i] - '0';
        }

        if (q == 0)
            return diff != 0;

        // Each unmatched pair of ? can change the difference
        // by at most 9.
        return abs(q) % 2 == 1 ||
               diff * 2 != -9 * q;
    }
};
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
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [39. Combination Sum](../../0001-0500/0039-combination-sum/)
- [40. Combination Sum II](../../0001-0500/0040-combination-sum-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-game/)
