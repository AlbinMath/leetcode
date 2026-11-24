# LeetCode 1640: Check Array Formation Through Concatenation

**LeetCode Problem #1640 — Check Array Formation Through Concatenation**
Solve LeetCode Check Array Formation Through Concatenation using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check Array Formation Through Concatenation |
| LeetCode | #1640 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of **distinct** integers `arr` and an array of integer arrays `pieces`, where the integers in `pieces` are **distinct**. Your goal is to form `arr` by concatenating the arrays in `pieces` **in any order**. However, you are **not** allowed to reorder the integers in each array `pieces[i]`.

Return `true` *if it is possible **to form the array *`arr`* from *`pieces`. Otherwise, return `false`.

## Constraints
- `1 <= pieces.length <= arr.length <= 100`
- `sum(pieces[i].length) == arr.length`
- `1 <= pieces[i].length <= arr.length`
- `1 <= arr[i], pieces[i][j] <= 100`
- The integers in `arr` are **distinct**.
- The integers in `pieces` are **distinct** (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).

## Examples
### Example 1
- **Input:** `arr = [15,88], pieces = [[88],[15]]`
- **Output:** `true`
- **Explanation:** Concatenate [15] then [88]

### Example 2
- **Input:** `arr = [49,18,16], pieces = [[16,18,49]]`
- **Output:** `false`
- **Explanation:** Even though the numbers match, we cannot reorder pieces[0].

### Example 3
- **Input:** `arr = [91,4,64,78], pieces = [[78],[4,64],[91]]`
- **Output:** `true`
- **Explanation:** Concatenate [91] then [4,64] then [78]

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Check Array Formation Through Concatenation**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [15,88], pieces = [[88],[15]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Concatenate [15] then [88]

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
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        unordered_map<int, int> mp;

        // Map each piece's first element to its index
        for (int i = 0; i < pieces.size(); i++) {
            mp[pieces[i][0]] = i;
        }

        int i = 0;

        while (i < arr.size()) {
            // No piece starts with this element
            if (mp.find(arr[i]) == mp.end()) {
                return false;
            }

            vector<int>& piece = pieces[mp[arr[i]]];

            // Match all elements of the piece
            for (int num : piece) {
                if (i >= arr.size() || arr[i] != num) {
                    return false;
                }
                i++;
            }
        }

        return true;
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
- [1929. Concatenation of Array](../../1501-2000/1929-concatenation-of-array/)
- [2562. Find the Array Concatenation Value](../../2501-3000/2562-find-the-array-concatenation-value/)
- [1250. Check If It Is a Good Array](../../1001-1500/1250-check-if-it-is-a-good-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-array-formation-through-concatenation/)
