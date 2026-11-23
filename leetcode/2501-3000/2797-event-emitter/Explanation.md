# LeetCode 2694: Event Emitter

**LeetCode Problem #2694 — Event Emitter**
Solve LeetCode Event Emitter using TypeScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Event Emitter |
| LeetCode | #2694 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design an `EventEmitter` class. This interface is similar (but with some differences) to the one found in Node.js or the Event Target interface of the DOM. The `EventEmitter` should allow for subscribing to events and emitting them.

Your `EventEmitter` class should have the following two methods:

**subscribe** - This method takes in two arguments: the name of an event as a string and a callback function. This callback function will later be called when the event is emitted. 
 An event should be able to have multiple listeners for the same event. When emitting an event with multiple callbacks, each should be called in the order in which they were subscribed. An array of results should be returned. You can assume no callbacks passed to `subscribe` are referentially identical. 
 The `subscribe` method should also return an object with an `unsubscribe` method that enables the user to unsubscribe. When it is called, the callback should be removed from the list of subscriptions and `undefined` should be returned. 
 **emit** - This method takes in two arguments: the name of an event as a string and an optional array of arguments that will be passed to the callback(s). If there are no callbacks subscribed to the given event, return an empty array. Otherwise, return an array of the results of all callback calls in the order they were subscribed.

## Constraints
- `1 <= actions.length <= 10`
- `values.length === actions.length`
- All test cases are valid, e.g. you don't need to handle scenarios when unsubscribing from a non-existing subscription.
- There are only 4 different actions: `EventEmitter`, `emit`, `subscribe`, and `unsubscribe`.
- The `EventEmitter` action doesn't take any arguments.
- The `emit` action takes between either 1 or 2 arguments. The first argument is the name of the event we want to emit, and the 2nd argument is passed to the callback functions.
- The `subscribe` action takes 2 arguments, where the first one is the event name and the second is the callback function.
- The `unsubscribe` action takes one argument, which is the 0-indexed order of the subscription made before.

## Examples
### Example 1
- **Input:** `actions = ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], 
values = [[], ["firstEvent"], ["firstEvent", "function cb1() { return 5; }"], ["firstEvent", "function cb1() { return 6; }"], ["firstEvent"]]`
- **Output:** `[[],["emitted",[]],["subscribed"],["subscribed"],["emitted",[5,6]]]`
- **Explanation:** const emitter = new EventEmitter();
emitter.emit("firstEvent"); // [], no callback are subscribed yet
emitter.subscribe("firstEvent", function cb1() { return 5; });
emitter.subscribe("firstEvent", function cb2() { return 6; });
emitter.emit("firstEvent"); // [5, 6], returns the output of cb1 and cb2

### Example 2
- **Input:** `actions = ["EventEmitter", "subscribe", "emit", "emit"], 
values = [[], ["firstEvent", "function cb1(...args) { return args.join(','); }"], ["firstEvent", [1,2,3]], ["firstEvent", [3,4,6]]]`
- **Output:** `[[],["subscribed"],["emitted",["1,2,3"]],["emitted",["3,4,6"]]]`
- **Explanation:** Note that the emit method should be able to accept an OPTIONAL array of arguments.

const emitter = new EventEmitter();
emitter.subscribe("firstEvent, function cb1(...args) { return args.join(','); });
emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]
emitter.emit("firstEvent", [3, 4, 6]); // ["3,4,6"]

### Example 3
- **Input:** `actions = ["EventEmitter", "subscribe", "emit", "unsubscribe", "emit"], 
values = [[], ["firstEvent", "(...args) => args.join(',')"], ["firstEvent", [1,2,3]], [0], ["firstEvent", [4,5,6]]]`
- **Output:** `[[],["subscribed"],["emitted",["1,2,3"]],["unsubscribed",0],["emitted",[]]]`
- **Explanation:** const emitter = new EventEmitter();
const sub = emitter.subscribe("firstEvent", (...args) => args.join(','));
emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]
sub.unsubscribe(); // undefined
emitter.emit("firstEvent", [4, 5, 6]); // [], there are no subscriptions

### Example 4
- **Input:** `actions = ["EventEmitter", "subscribe", "subscribe", "unsubscribe", "emit"], 
values = [[], ["firstEvent", "x => x + 1"], ["firstEvent", "x => x + 2"], [0], ["firstEvent", [5]]]`
- **Output:** `[[],["subscribed"],["subscribed"],["unsubscribed",0],["emitted",[7]]]`
- **Explanation:** const emitter = new EventEmitter();
const sub1 = emitter.subscribe("firstEvent", x => x + 1);
const sub2 = emitter.subscribe("firstEvent", x => x + 2);
sub1.unsubscribe(); // undefined
emitter.emit("firstEvent", [5]); // [7]

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a Map where keys are event names and values are arrays of callbacks. `subscribe` adds a callback and returns an object with `unsubscribe`. `emit` calls all registered callbacks for the event with the provided args and returns their results.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `actions = ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], 
values = [[], ["firstEvent"], ["firstEvent", "function cb1() { return 5; }"], ["firstEvent", "function cb1() { return 6; }"], ["firstEvent"]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[],["emitted",[]],["subscribed"],["subscribed"],["emitted",[5,6]]]`.
4. **Verification:** const emitter = new EventEmitter();
emitter.emit("firstEvent"); // [], no callback are subscribed yet
emitter.subscribe("firstEvent", function cb1() { return 5; });
emitter.subscribe("firstEvent", function cb2() { return 6; });
emitter.emit("firstEvent"); // [5, 6], returns the output of cb1 and cb2

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
class EventEmitter {
    events: Map<string, Function[]>;

    constructor() {
        this.events = new Map();
    }

    subscribe(event: string, cb: Function): { unsubscribe: () => void } {
        if (!this.events.has(event)) {
            this.events.set(event, []);
        }

        const callbacks = this.events.get(event)!;
        callbacks.push(cb);

        return {
            unsubscribe: () => {
                const index = callbacks.indexOf(cb);

                if (index !== -1) {
                    callbacks.splice(index, 1);
                }
            }
        };
    }

    emit(event: string, args: any[] = []): any[] {
        if (!this.events.has(event)) {
            return [];
        }

        const callbacks = this.events.get(event)!;

        return callbacks.map(cb => cb(...args));
    }
}
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
- [675. Cut Off Trees for Golf Event](../../0501-1000/0675-cut-off-trees-for-golf-event/)
- [3317. Find the Number of Possible Ways for an Event](../../3501-4000/3604-find-the-number-of-possible-ways-for-an-event/)
- [3885. Design Event Manager](../../4001-4500/4267-design-event-manager/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/event-emitter/)
