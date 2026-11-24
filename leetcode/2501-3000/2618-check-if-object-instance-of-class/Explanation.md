# LeetCode 2618: Check if Object Instance of Class

**LeetCode Problem #2618 — Check if Object Instance of Class**
Solve LeetCode Check if Object Instance of Class using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Object Instance of Class |
| LeetCode | #2618 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class's methods.

There are no constraints on the data types that can be passed to the function. For example, the value or the class could be `undefined`.

## Examples
### Example 1
- **Input:** `func = () => checkIfInstanceOf(new Date(), Date)`
- **Output:** `true`
- **Explanation:** The object returned by the Date constructor is, by definition, an instance of Date.

### Example 2
- **Input:** `func = () => { class Animal {}; class Dog extends Animal {}; return checkIfInstanceOf(new Dog(), Animal); }`
- **Output:** `true`
- **Explanation:** class Animal {};
class Dog extends Animal {};
checkIfInstanceOf(new Dog(), Animal); // true

Dog is a subclass of Animal. Therefore, a Dog object is an instance of both Dog and Animal.

### Example 3
- **Input:** `func = () => checkIfInstanceOf(Date, Date)`
- **Output:** `false`
- **Explanation:** A date constructor cannot logically be an instance of itself.

### Example 4
- **Input:** `func = () => checkIfInstanceOf(5, Number)`
- **Output:** `true`
- **Explanation:** 5 is a Number. Note that the "instanceof" keyword would return false. However, it is still considered an instance of Number because it accesses the Number methods. For example "toFixed()".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Walk up the prototype chain of `obj` using `Object.getPrototypeOf()`. At each step, check if the prototype matches `classFunction.prototype`. Return true if found, false if the chain ends (null).

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `func = () => checkIfInstanceOf(new Date(), Date)`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The object returned by the Date constructor is, by definition, an instance of Date.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined) {
        return false;
    }

    if (typeof classFunction !== "function") {
        return false;
    }

    let proto = Object.getPrototypeOf(obj);

    while (proto !== null) {
        if (proto === classFunction.prototype) {
            return true;
        }
        proto = Object.getPrototypeOf(proto);
    }

    return false;
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
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1003-check-if-word-is-valid-after-substitutions/)
- [1232. Check If It Is a Straight Line](../../1001-1500/1232-check-if-it-is-a-straight-line/)
- [1250. Check If It Is a Good Array](../../1001-1500/1250-check-if-it-is-a-good-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-object-instance-of-class/)
