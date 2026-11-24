# LeetCode 1345: Jump Game IV

**LeetCode Problem #1345 — Jump Game IV**
Solve LeetCode Jump Game IV using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game IV |
| LeetCode | #1345 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step you can jump from index `i` to index:

`i + 1` where: `i + 1 < arr.length`. 
 `i - 1` where: `i - 1 >= 0`. 
 `j` where: `arr[i] == arr[j]` and `i != j`.

Return *the minimum number of steps* to reach the **last index** of the array.

Notice that you can not jump outside of the array at any time.

## Constraints
- `1 <= arr.length <= 5 * 10^4`
- `-10^8 <= arr[i] <= 10^8`

## Examples
### Example 1
- **Input:** `arr = [100,-23,-23,404,100,23,23,23,3,404]`
- **Output:** `3`
- **Explanation:** You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

### Example 2
- **Input:** `arr = [7]`
- **Output:** `0`
- **Explanation:** Start index is the last index. You do not need to jump.

### Example 3
- **Input:** `arr = [7,6,9,6,9,6,9,7]`
- **Output:** `1`
- **Explanation:** You can jump directly from index 0 to index 7 which is last index of the array.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses **BFS** for shortest path.

1. **Group by Value:** Build a map from each value to all indices containing it.
2. **BFS:** Start from index `0`. Each level of BFS represents one jump. For each index, explore three types of neighbors: `i-1`, `i+1`, and all indices with the same value.
3. **Optimization:** After processing all indices of a value, erase that value from the map. This prevents revisiting the same group and ensures $O(N)$ total work.
4. Return the number of BFS levels when reaching index `n-1`.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [100,-23,-23,404,100,23,23,23,3,404]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

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
    int minJumps(vector<int>& arr) {
        int n = arr.size();

        if (n == 1)
            return 0;

        // Store all indices having the same value
        unordered_map<int, vector<int>> mp;

        for (int i = 0; i < n; i++) {
            mp[arr[i]].push_back(i);
        }

        queue<int> q;
        vector<bool> visited(n, false);

        q.push(0);
        visited[0] = true;

        int steps = 0;

        while (!q.empty()) {
            int size = q.size();

            while (size--) {
                int i = q.front();
                q.pop();

                if (i == n - 1)
                    return steps;

                // Jump to i - 1
                if (i - 1 >= 0 && !visited[i - 1]) {
                    visited[i - 1] = true;
                    q.push(i - 1);
                }

                // Jump to i + 1
                if (i + 1 < n && !visited[i + 1]) {
                    visited[i + 1] = true;
                    q.push(i + 1);
                }

                // Jump to every index with the same value
                if (mp.count(arr[i])) {
                    for (int j : mp[arr[i]]) {
                        if (!visited[j]) {
                            visited[j] = true;
                            q.push(j);
                        }
                    }

                    // Important: process each value only once
                    mp.erase(arr[i]);
                }
            }

            steps++;
        }

        return -1;
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
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)
- [1306. Jump Game III](../../1001-1500/1306-jump-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-iv/)
