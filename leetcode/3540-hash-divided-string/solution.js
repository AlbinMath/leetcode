var stringHash = function(s, k) {
    const result = [];

    for (let i = 0; i < s.length; i += k) {
        let total = 0;
        for (let j = i; j < i + k; j++) {
            total += s.charCodeAt(j) - 97;
        }
        result.push(String.fromCharCode(97 + (total % 26)));
    }

    return result.join('');
};
