
var deserialize = function(s) {
    // If input is a single integer
    if (s[0] !== '[') {
        let ni = new NestedInteger();
        ni.setInteger(Number(s));
        return ni;
    }

    const stack = [];
    let num = 0;
    let sign = 1;
    let readingNumber = false;

    for (let i = 0; i < s.length; i++) {
        const ch = s[i];

        if (ch === '[') {
            const ni = new NestedInteger();
            stack.push(ni);

        } else if (ch === '-' ) {
            sign = -1;
            readingNumber = true;

        } else if (ch >= '0' && ch <= '9') {
            num = num * 10 + Number(ch);
            readingNumber = true;

        } else if (ch === ',' || ch === ']') {

            // Add the completed integer to current list
            if (readingNumber) {
                const ni = new NestedInteger();
                ni.setInteger(num * sign);

                stack[stack.length - 1].add(ni);

                num = 0;
                sign = 1;
                readingNumber = false;
            }

            // Close current list
            if (ch === ']') {
                const current = stack.pop();

                // Attach nested list to its parent
                if (stack.length > 0) {
                    stack[stack.length - 1].add(current);
                } else {
                    return current;
                }
            }
        }
    }
};

