# LeetCode 2693: Call Function with Custom Context

**LeetCode Problem #2693 — Call Function with Custom Context**
Solve LeetCode Call Function with Custom Context using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Call Function with Custom Context |
| LeetCode | #2693 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Enhance all functions to have the `callPolyfill` method. The method accepts an object `obj` as its first parameter and any number of additional arguments. The `obj` becomes the `this` context for the function. The additional arguments are passed to the function (that the `callPolyfill` method belongs on).

For example if you had the function:

function tax(price, taxRate) {
 const totalCost = price * (1 + taxRate);
 console.log(`The cost of ${this.item} is ${totalCost}`);
}

Calling this function like `tax(10, 0.1)` will log `"The cost of undefined is 11"`. This is because the `this` context was not defined.

However, calling the function like `tax.callPolyfill({item: "salad"}, 10, 0.1)` will log `"The cost of salad is 11"`. The `this` context was appropriately set, and the function logged an appropriate output.

Please solve this without using the built-in `Function.call` method.

## Constraints
- ` typeof args[0] == 'object' and args[0] != null `
- `1 <= args.length <= 100`
- `2 <= JSON.stringify(args[0]).length <= 10^5`

## Examples
### Example 1
- **Input:** `fn = function add(b) {
 return this.a + b;
}
args = [{"a": 5}, 7]`
- **Output:** `12`
- **Explanation:** fn.callPolyfill({"a": 5}, 7); // 12
callPolyfill sets the "this" context to {"a": 5}. 7 is passed as an argument.

### Example 2
- **Input:** `fn = function tax(price, taxRate) { 
 return `The cost of the ${this.item} is ${price * taxRate}`; 
}
args = [{"item": "burger"}, 10, 1.1]`
- **Output:** `"The cost of the burger is 11"`
- **Explanation:** callPolyfill sets the "this" context to {"item": "burger"}. 10 and 1.1 are passed as additional arguments.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Temporarily assigns the function as a property of the `context` object, calls it with the provided arguments, then deletes the temporary property. Uses a Symbol to avoid property name collisions.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `fn = function add(b) {
 return this.a + b;
}
args = [{"a": 5}, 7]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** fn.callPolyfill({"a": 5}, 7); // 12
callPolyfill sets the "this" context to {"a": 5}. 7 is passed as an argument.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
type JSONValue =
    | null
    | boolean
    | number
    | string
    | JSONValue[]
    | { [key: string]: JSONValue };

Function.prototype.callPolyfill = function(
    context: any,
    ...args: any[]
): any {
    const key = Symbol();

    context[key] = this;

    const result = context[key](...args);

    delete context[key];

    return result;
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
- [2666. Allow One Function Call](../../2501-3000/2796-allow-one-function-call/)
- [396. Rotate Function](../../0001-0500/0396-rotate-function/)
- [1521. Find a Value of a Mysterious Function Closest to Target](../../1501-2000/1645-find-a-value-of-a-mysterious-function-closest-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/call-function-with-custom-context/)
