function sortBy<T>(arr: T[], fn: (x: T) => number): T[] {
    return arr.sort((a, b) => fn(a) - fn(b));
}
