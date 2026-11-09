
var countOfAtoms = function(formula) {
    const stack = [new Map()];
    let i = 0;

    while (i < formula.length) {
        const ch = formula[i];

        if (ch === '(') {
            stack.push(new Map());
            i++;
        }

        else if (ch === ')') {
            const top = stack.pop();
            i++;

            // Read multiplier after closing parenthesis
            let num = 0;

            while (i < formula.length && 
                   formula[i] >= '0' && formula[i] <= '9') {
                num = num * 10 + Number(formula[i]);
                i++;
            }

            if (num === 0) num = 1;

            // Multiply all elements inside parentheses
            const current = stack[stack.length - 1];

            for (const [element, count] of top) {
                current.set(
                    element,
                    (current.get(element) || 0) + count * num
                );
            }
        }

        else {
            // Read element name
            let element = formula[i];
            i++;

            while (i < formula.length &&
                   formula[i] >= 'a' && formula[i] <= 'z') {
                element += formula[i];
                i++;
            }

            // Read element count
            let num = 0;

            while (i < formula.length &&
                   formula[i] >= '0' && formula[i] <= '9') {
                num = num * 10 + Number(formula[i]);
                i++;
            }

            if (num === 0) num = 1;

            const current = stack[stack.length - 1];

            current.set(
                element,
                (current.get(element) || 0) + num
            );
        }
    }

    // Sort elements alphabetically
    const result = stack[0];
    const elements = [...result.keys()].sort();

    let answer = '';

    for (const element of elements) {
        answer += element;

        const count = result.get(element);

        if (count > 1) {
            answer += count;
        }
    }

    return answer;
};

