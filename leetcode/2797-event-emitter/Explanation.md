# Event Emitter

## Problem Explanation
Implement an EventEmitter class with `subscribe(event, callback)` and `emit(event, args)`.

## How the Code Works
Uses a Map where keys are event names and values are arrays of callbacks. `subscribe` adds a callback and returns an object with `unsubscribe`. `emit` calls all registered callbacks for the event with the provided args and returns their results.
