var decodeString = function(s) {
    const stack = [];
    let currentNum = 0;
    let currentStr = "";

    for (const ch of s) {
        if (ch >= '0' && ch <= '9') {
            currentNum = currentNum * 10 + Number(ch);
        } else if (ch === '[') {
            stack.push([currentStr, currentNum]);
            currentStr = "";
            currentNum = 0;
        } else if (ch === ']') {
            const [prevStr, repeat] = stack.pop();
            currentStr = prevStr + currentStr.repeat(repeat);
        } else {
            currentStr += ch;
        }
    }

    return currentStr;
};
