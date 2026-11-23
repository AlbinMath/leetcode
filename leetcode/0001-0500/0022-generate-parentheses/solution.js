var generateParenthesis = function(n) {
    const result = [];

    function backtrack(current, open, close) {
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }

        // Add an opening parenthesis if available
        if (open < n) {
            backtrack(current + "(", open + 1, close);
        }

        // Add a closing parenthesis only if it stays valid
        if (close < open) {
            backtrack(current + ")", open, close + 1);
        }
    }

    backtrack("", 0, 0);
    return result;
};
