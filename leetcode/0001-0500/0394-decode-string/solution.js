
var decodeString = function(s) {
    const stack = [];
    let currentNum = 0;
    let currentStr = "";

    for (const char of s) {
        if (char >= '0' && char <= '9') {
            // Build the repetition number
            currentNum = currentNum * 10 + Number(char);
        } else if (char === '[') {
            // Save the current state before entering brackets
            stack.push([currentStr, currentNum]);
            currentStr = "";
            currentNum = 0;
        } else if (char === ']') {
            // Restore the previous state and repeat the inner string
            const [previousStr, repeatCount] = stack.pop();
            currentStr = previousStr + currentStr.repeat(repeatCount);
        } else {
            // Append ordinary letters
            currentStr += char;
        }
    }

    return currentStr;
};

