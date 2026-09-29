function memoize(fn: (...args: number[]) => number) {
    const cache = new Map<string, number>();
    let callCount = 0;

    const memoized = (...args: number[]): number => {
        const key = JSON.stringify(args);

        if (cache.has(key)) {
            return cache.get(key)!;
        }

        const result = fn(...args);

        cache.set(key, result);
        callCount++;

        return result;
    };

    return memoized;
}
