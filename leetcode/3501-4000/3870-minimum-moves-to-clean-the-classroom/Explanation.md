# LeetCode 3568: Minimum Moves to Clean the Classroom

**LeetCode Problem #3568 — Minimum Moves to Clean the Classroom**
Solve LeetCode Minimum Moves to Clean the Classroom using C++ and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Clean the Classroom |
| LeetCode | #3568 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` grid `classroom` where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

`'S'`: Starting position of the student 
 `'L'`: Litter that must be collected (once collected, the cell becomes empty) 
 `'R'`: Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times) 
 `'X'`: Obstacle the student cannot pass through 
 `'.'`: Empty space

You are also given an integer `energy`, representing the student's maximum energy capacity. The student starts with this energy from the starting position `'S'`.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area `'R'`, which resets the energy to its **maximum** capacity `energy`.

Return the **minimum** number of moves required to collect all litter items, or `-1` if it's impossible.

## Constraints
- `1 <= m == classroom.length <= 20`
- `1 <= n == classroom[i].length <= 20`
- `classroom[i][j]` is one of `'S'`, `'L'`, `'R'`, `'X'`, or `'.'`
- `1 <= energy <= 50`
- There is exactly **one** `'S'` in the grid.
- There are **at most** 10 `'L'` cells in the grid.

## Examples
### Example 1
- **Input:** `classroom = ["S.", "XL"], energy = 2`
- **Output:** `2`
- **Explanation:** The student starts at cell (0, 0) with 2 units of energy. 
 Since cell `(1, 0)` contains an obstacle 'X', the student cannot move directly downward. 
 A valid sequence of moves to collect all litter is as follows:
 
 Move 1: From `(0, 0)` &rarr; `(0, 1)` with 1 unit of energy and 1 unit remaining. 
 Move 2: From `(0, 1)` &rarr; `(1, 1)` to collect the litter `'L'`. 
 
 
 The student collects all the litter using 2 moves. Thus, the output is 2.

### Example 2
- **Input:** `classroom = ["LS", "RL"], energy = 4`
- **Output:** `3`
- **Explanation:** The student starts at cell (0, 1) with 4 units of energy. 
 A valid sequence of moves to collect all litter is as follows:
 
 Move 1: From `(0, 1)` &rarr; `(0, 0)` to collect the first litter `'L'` with 1 unit of energy used and 3 units remaining. 
 Move 2: From `(0, 0)` &rarr; `(1, 0)` to `'R'` to reset and restore energy back to 4. 
 Move 3: From `(1, 0)` &rarr; `(1, 1)` to collect the second litter 'L' . 
 
 
 The student collects all the litter using 3 moves. Thus, the output is 3.

### Example 3
- **Input:** `classroom = ["L.S", "RXL"], energy = 3`
- **Output:** `-1`
- **Explanation:** No valid path collects all `'L'`.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Moves to Clean the Classroom**, we observe the problem requirements and utilize the **Sliding Window** technique. We maintain a contiguous window defined by `left` and `right` pointers. The right pointer expands the window by adding incoming elements, while the left pointer advances to restore window invariants whenever duplicates or constraint limits are exceeded.

## Algorithm
1. Initialize `left = 0` and window tracking data structures.
2. Expand `right` pointer over input elements.
3. Contract `left` pointer when window invariants are breached.
4. Update global best metric for valid window intervals.
5. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `classroom = ["S.", "XL"], energy = 2`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The student starts at cell (0, 0) with 2 units of energy. 
 Since cell `(1, 0)` contains an obstacle 'X', the student cannot move directly downward. 
 A valid sequence of moves to collect all litter is as follows:
 
 Move 1: From `(0, 0)` &rarr; `(0, 1)` with 1 unit of energy and 1 unit remaining. 
 Move 2: From `(0, 1)` &rarr; `(1, 1)` to collect the litter `'L'`. 
 
 
 The student collects all the litter using 2 moves. Thus, the output is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size();
        int n = classroom[0].size();

        int sr, sc;
        vector<vector<int>> id(m, vector<int>(n, -1));

        int k = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (classroom[r][c] == 'S') {
                    sr = r;
                    sc = c;
                }
                else if (classroom[r][c] == 'L') {
                    id[r][c] = k++;
                }
            }
        }

        int fullMask = (1 << k) - 1;

        // state = position * (maskCount * (energy + 1))
        int masks = 1 << k;
        int E = energy + 1;

        int totalStates = m * n * masks * E;

        vector<char> visited(totalStates, 0);

        auto encode = [&](int r, int c, int mask, int e) {
            return (((r * n + c) * masks + mask) * E + e);
        };

        // Store r, c, mask, energy
        queue<array<int, 4>> q;

        q.push({sr, sc, 0, energy});
        visited[encode(sr, sc, 0, energy)] = 1;

        int dr[4] = {1, -1, 0, 0};
        int dc[4] = {0, 0, 1, -1};

        int moves = 0;

        while (!q.empty()) {
            int sz = q.size();

            while (sz--) {
                auto [r, c, mask, e] = q.front();
                q.pop();

                if (mask == fullMask)
                    return moves;

                if (e == 0)
                    continue;

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr < 0 || nr >= m ||
                        nc < 0 || nc >= n)
                        continue;

                    if (classroom[nr][nc] == 'X')
                        continue;

                    int ne = e - 1;
                    int nmask = mask;

                    // Collect litter
                    if (classroom[nr][nc] == 'L') {
                        nmask |= (1 << id[nr][nc]);
                    }

                    // Reset energy
                    if (classroom[nr][nc] == 'R') {
                        ne = energy;
                    }

                    int state = encode(nr, nc, nmask, ne);

                    if (!visited[state]) {
                        visited[state] = 1;
                        q.push({nr, nc, nmask, ne});
                    }
                }
            }

            moves++;
        }

        return -1;
    }
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)
- [1210. Minimum Moves to Reach Target with Rotations](../../1001-1500/1322-minimum-moves-to-reach-target-with-rotations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/)
