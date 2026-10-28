/**
 * @param {string} characters
 * @param {number} combinationLength
 */
var CombinationIterator = function(characters, combinationLength) {
    this.combinations = [];
    this.index = 0;

    const generate = (start, current) => {
        if (current.length === combinationLength) {
            this.combinations.push(current);
            return;
        }

        for (let i = start; i < characters.length; i++) {
            generate(i + 1, current + characters[i]);
        }
    };

    generate(0, "");
};

/**
 * @return {string}
 */
CombinationIterator.prototype.next = function() {
    return this.combinations[this.index++];
};

/**
 * @return {boolean}
 */
CombinationIterator.prototype.hasNext = function() {
    return this.index < this.combinations.length;
};
