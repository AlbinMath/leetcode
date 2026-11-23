var stringSequence = function(target) {
    const result = [];
    let prefix = "";

    for (const ch of target) {
        const targetCode = ch.charCodeAt(0);
        for (let code = 97; code <= targetCode; code++) {
            result.push(prefix + String.fromCharCode(code));
        }
        prefix += ch;
    }

    return result;
};
