var licenseKeyFormatting = function(s, k) {
    s = s.replace(/-/g, "").toUpperCase();

    let result = [];

    for (let i = s.length; i > 0; i -= k) {
        result.push(s.substring(Math.max(0, i - k), i));
    }

    return result.reverse().join("-");
};
