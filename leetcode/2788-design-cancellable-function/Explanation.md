# Design Cancellable Function

## Problem Explanation
Create a wrapper that makes an async generator function cancellable. When cancelled, throw an error into the generator.

## How the Code Works
Wraps the generator execution in a promise. Maintains a reference to allow cancellation. When `cancel()` is called, it throws an error into the generator via `generator.throw()`, causing the generator to reject.
