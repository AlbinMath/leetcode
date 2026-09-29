# Call Function With Custom Context

## Problem Explanation
Implement `Function.prototype.callPolyfill(context, ...args)` that calls the function with the given `this` context.

## How the Code Works
Temporarily assigns the function as a property of the `context` object, calls it with the provided arguments, then deletes the temporary property. Uses a Symbol to avoid property name collisions.
