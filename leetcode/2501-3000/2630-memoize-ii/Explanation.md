# LeetCode 2630: Memoize II

**LeetCode Problem #2630 — Memoize II**
Solve LeetCode Memoize II using TypeScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Memoize II |
| LeetCode | #2630 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a function `fn`, return a **memoized** version of that function.

A **memoized **function is a function that will never be called twice with the same inputs. Instead it will return a cached value.

`fn` can be any function and there are no constraints on what type of values it accepts. Inputs are considered identical if they are `===` to each other.

## Constraints
- `1 <= inputs.length <= 10^5`
- `0 <= inputs.flat().length <= 10^5`
- `inputs[i][j] != NaN`

## Examples
### Example 1
- **Input:** `getInputs = () => [[2,2],[2,2],[1,2]]
fn = function (a, b) { return a + b; }`
- **Output:** `[{"val":4,"calls":1},{"val":4,"calls":1},{"val":3,"calls":2}]`
- **Explanation:** const inputs = getInputs();
const memoized = memoize(fn);
for (const arr of inputs) {
 memoized(...arr);
}

For the inputs of (2, 2): 2 + 2 = 4, and it required a call to fn().
For the inputs of (2, 2): 2 + 2 = 4, but those inputs were seen before so no call to fn() was required.
For the inputs of (1, 2): 1 + 2 = 3, and it required another call to fn() for a total of 2.

### Example 2
- **Input:** `getInputs = () => [[{},{}],[{},{}],[{},{}]] 
fn = function (a, b) { return ({...a, ...b}); }`
- **Output:** `[{"val":{},"calls":1},{"val":{},"calls":2},{"val":{},"calls":3}]`
- **Explanation:** Merging two empty objects will always result in an empty object. It may seem like there should only be 1 call to fn() because of cache-hits, however none of those objects are === to each other.

### Example 3
- **Input:** `getInputs = () => { const o = {}; return [[o,o],[o,o],[o,o]]; }
fn = function (a, b) { return ({...a, ...b}); }`
- **Output:** `[{"val":{},"calls":1},{"val":{},"calls":1},{"val":{},"calls":1}]`
- **Explanation:** Merging two empty objects will always result in an empty object. The 2nd and 3rd third function calls result in a cache-hit. This is because every object passed in is identical.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Uses a **trie-like cache** or `WeakMap`/`Map` structure keyed by argument references. For each call, traverses the cache structure using each argument as a key, creating new nodes as needed. At the final node, stores the computed result for future lookups.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `getInputs = () => [[2,2],[2,2],[1,2]]
fn = function (a, b) { return a + b; }`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[{"val":4,"calls":1},{"val":4,"calls":1},{"val":3,"calls":2}]`.
4. **Verification:** const inputs = getInputs();
const memoized = memoize(fn);
for (const arr of inputs) {
 memoized(...arr);
}

For the inputs of (2, 2): 2 + 2 = 4, and it required a call to fn().
For the inputs of (2, 2): 2 + 2 = 4, but those inputs were seen before so no call to fn() was required.
For the inputs of (1, 2): 1 + 2 = 3, and it required another call to fn() for a total of 2.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function memoize(fn: Function): Function {
    const cache = new Map<any, any>();

    return function (...args: any[]) {
        let current = cache;

        for (const arg of args) {
            if (!current.has(arg)) {
                current.set(arg, new Map());
            }

            current = current.get(arg);
        }

        if (current.has("result")) {
            return current.get("result");
        }

        const result = fn(...args);
        current.set("result", result);

        return result;
    };
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
- [2623. Memoize](../../2501-3000/2623-memoize/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [49. Group Anagrams](../../0001-0500/0049-group-anagrams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/memoize-ii/)
