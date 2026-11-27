
var removeAnagrams = function(words) {
    const result = [];
    let previousSignature = "";

    for (const word of words) {
        const signature = word.split("").sort().join("");
        if (signature !== previousSignature) {
            result.push(word);
            previousSignature = signature;
        }
    }

    return result;
};

