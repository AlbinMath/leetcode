function evalRPN(tokens: string[]): number {
    const stack: number[] = [];

    for (const token of tokens) {
        if (token === "+" || token === "-" || token === "*" || token === "/") {
            const b = stack.pop()!;
            const a = stack.pop()!;

            let result: number;

            if (token === "+") {
                result = a + b;
            } else if (token === "-") {
                result = a - b;
            } else if (token === "*") {
                result = a * b;
            } else {
                // Truncate toward zero
                result = Math.trunc(a / b);
            }

            stack.push(result);
        } else {
            stack.push(Number(token));
        }
    }

    return stack[0];
}
