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
