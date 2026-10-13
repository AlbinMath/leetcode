
var addSpaces = function(s, spaces) {
    let result = "";
    let j = 0;

    for (let i = 0; i < s.length; i++) {
        if (j < spaces.length && i === spaces[j]) {
            result += " ";
            j++;
        }

        result += s[i];
    }

    return result;
};

