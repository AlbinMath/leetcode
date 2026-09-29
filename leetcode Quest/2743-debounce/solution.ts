function debounce(
    fn: (...args: any[]) => any,
    t: number
): (...args: any[]) => void {
    let timer: ReturnType<typeof setTimeout>;

    return function (...args: any[]) {
        // Cancel the previous scheduled call
        clearTimeout(timer);

        // Schedule the latest call
        timer = setTimeout(() => {
            fn(...args);
        }, t);
    };
}
