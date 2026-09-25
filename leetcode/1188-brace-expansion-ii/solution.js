/**
 * @param {string} expression
 * @return {string[]}
 */
var braceExpansionII = function(expression) {
    let i = 0;

    // Parse an expression: union of terms
    function parseExpression() {
        let result = new Set();
        result = parseTerm();

        while (i < expression.length && expression[i] === ',') {
            i++; // skip comma
            let next = parseTerm();

            for (let word of next) {
                result.add(word);
            }
        }

        return result;
    }

    // Parse a term: concatenation of factors
    function parseTerm() {
        let result = new Set([""]);

        while (
            i < expression.length &&
            expression[i] !== '}' &&
            expression[i] !== ','
        ) {
            let factor = parseFactor();
            let next = new Set();

            for (let a of result) {
                for (let b of factor) {
                    next.add(a + b);
                }
            }

            result = next;
        }

        return result;
    }

    // Parse a single letter or {...}
    function parseFactor() {
        if (expression[i] >= 'a' && expression[i] <= 'z') {
            return new Set([expression[i++]]);
        }

        // '{'
        i++;

        let result = parseExpression();

        // '}'
        i++;

        return result;
    }

    let result = [...parseExpression()];

    // Lexicographical sorting
    result.sort();

    return result;
};
