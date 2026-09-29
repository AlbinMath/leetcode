function cancellable(
    fn: (...args: any[]) => any,
    args: any[],
    t: number
): Function {
    // Call immediately
    fn(...args);

    // Call repeatedly every t milliseconds
    const intervalId = setInterval(() => {
        fn(...args);
    }, t);

    // Return cancellation function
    return () => {
        clearInterval(intervalId);
    };
}
