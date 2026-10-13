
var WordDictionary = function() {
    this.root = {};
};

WordDictionary.prototype.addWord = function(word) {
    let node = this.root;

    for (const char of word) {
        if (!node[char]) {
            node[char] = {};
        }
        node = node[char];
    }

    node.isEnd = true;
};

WordDictionary.prototype.search = function(word) {
    function dfs(node, index) {
        if (index === word.length) {
            return node.isEnd === true;
        }

        const char = word[index];

        if (char === ".") {
            for (const key of Object.keys(node)) {
                if (key !== "isEnd" && dfs(node[key], index + 1)) {
                    return true;
                }
            }
            return false;
        }

        if (!node[char]) {
            return false;
        }

        return dfs(node[char], index + 1);
    }

    return dfs(this.root, 0);
};

