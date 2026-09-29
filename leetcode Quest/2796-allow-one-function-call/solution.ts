function once(fn: Function): Function {
    let called = false;

    return function(...args: any[]) {
        if (called) {
            return undefined;
        }

        called = true;
        return fn(...args);
    };
}
