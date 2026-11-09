
var validateStackSequences = function(pushed, popped) {
    const stack = [];
    let j = 0;

    for (let num of pushed) {
        // Push element onto stack
        stack.push(num);

        // Pop while stack top matches popped sequence
        while (
            stack.length > 0 &&
            stack[stack.length - 1] === popped[j]
        ) {
            stack.pop();
            j++;
        }
    }

    // All elements must be popped
    return j === popped.length;
};

