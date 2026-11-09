
var isValid = function(s) {
    const stack = [];

    for (let ch of s) {
        stack.push(ch);

        // Check whether the last three characters are "abc"
        const n = stack.length;

        if (
            n >= 3 &&
            stack[n - 3] === 'a' &&
            stack[n - 2] === 'b' &&
            stack[n - 1] === 'c'
        ) {
            // Remove "abc"
            stack.pop();
            stack.pop();
            stack.pop();
        }
    }

    return stack.length === 0;
};

