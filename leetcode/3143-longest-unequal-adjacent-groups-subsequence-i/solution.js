var getLongestSubsequence = function(words, groups) {
    let ans = [];

    ans.push(words[0]);

    for (let i = 1; i < words.length; i++) {
        if (groups[i] !== groups[i - 1]) {
            ans.push(words[i]);
        }
    }

    return ans;
};
