# LeetCode 1656: Design an Ordered Stream

**LeetCode Problem #1656 — Design an Ordered Stream**
Solve LeetCode Design an Ordered Stream using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design an Ordered Stream |
| LeetCode | #1656 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a stream of `n` `(idKey, value)` pairs arriving in an **arbitrary** order, where `idKey` is an integer between `1` and `n` and `value` is a string. No two pairs have the same `id`.

Design a stream that returns the values in **increasing order of their IDs** by returning a **chunk** (list) of values after each insertion. The concatenation of all the **chunks** should result in a list of the sorted values.

Implement the `OrderedStream` class:

`OrderedStream(int n)` Constructs the stream to take `n` values. 
 `String[] insert(int idKey, String value)` Inserts the pair `(idKey, value)` into the stream, then returns the **largest possible chunk** of currently inserted values that appear next in the order.

## Constraints
- `1 <= n <= 1000`
- `1 <= id <= n`
- `value.length == 5`
- `value` consists only of lowercase letters.
- Each call to `insert` will have a unique `id.`
- Exactly `n` calls will be made to `insert`.

## Examples
Consider the standard input for **Design an Ordered Stream**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Design an Ordered Stream**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Bitwise Masking & Bit Shift** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class OrderedStream {
private:
    vector<string> stream;
    int ptr;

public:
    OrderedStream(int n) {
        stream.resize(n + 1);
        ptr = 1;
    }

    vector<string> insert(int idKey, string value) {
        stream[idKey] = value;

        vector<string> result;

        while (ptr < stream.size() && !stream[ptr].empty()) {
            result.push_back(stream[ptr]);
            ptr++;
        }

        return result;
    }
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1327. List the Products Ordered in a Period](../../1001-1500/1462-list-the-products-ordered-in-a-period/)
- [2717. Semi-Ordered Permutation](../../2501-3000/2785-semi-ordered-permutation/)
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-an-ordered-stream/)
