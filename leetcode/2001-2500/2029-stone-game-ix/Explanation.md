# LeetCode 2029: Stone Game IX

**LeetCode Problem #2029 — Stone Game IX**
Solve LeetCode Stone Game IX using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game IX |
| LeetCode | #2029 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array `stones`, where `stones[i]` is the **value** of the `i^th` stone.

Alice and Bob take turns, with **Alice** starting first. On each turn, the player may remove any stone from `stones`. The player who removes a stone **loses** if the **sum** of the values of **all removed stones** is divisible by `3`. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play **optimally**, return `true` *if Alice wins and* `false` *if Bob wins*.

## Constraints
- `1 <= stones.length <= 10^5`
- `1 <= stones[i] <= 10^4`

## Examples
### Example 1
- **Input:** `stones = [2,1]`
- **Output:** `true`
- **Explanation:** The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.

### Example 2
- **Input:** `stones = [2]`
- **Output:** `false`
- **Explanation:** Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.

### Example 3
- **Input:** `stones = [5,1,2,4,3]`
- **Output:** `false`
- **Explanation:** Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code counts stones by their value mod 3 (groups 0, 1, 2). The key insights are:
- Mod-0 stones flip the game state (like a "pass" that changes who benefits).
- Alice needs to choose a starting stone (mod 1 or mod 2) that forces Bob into a losing position.
- The solution analyzes both possible starting moves and checks if either leads to a win for Alice based on the counts.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `stones = [2,1]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        int cnt[3] = {0, 0, 0};

        for (int x : stones) {
            cnt[x % 3]++;
        }

        // Stones divisible by 3 do not change the sum's remainder.
        // If there are an even number of them, they can effectively
        // be ignored for the main strategy.
        if (cnt[0] % 2 == 0) {
            return cnt[1] > 0 && cnt[2] > 0;
        }

        // Odd number of 0-mod-3 stones
        return abs(cnt[1] - cnt[2]) > 2;
    }
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [877. Stone Game](../../0501-1000/0877-stone-game/)
- [1140. Stone Game II](../../1001-1500/1140-stone-game-ii/)
- [1406. Stone Game III](../../1001-1500/1406-stone-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-ix/)
