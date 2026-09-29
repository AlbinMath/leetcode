var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration
 * @return {boolean}
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();

    // Check whether an unexpired key already exists
    const exists = this.cache.has(key) &&
                   this.cache.get(key).expiry > now;

    // Store/overwrite the value and expiration time
    this.cache.set(key, {
        value: value,
        expiry: now + duration
    });

    return exists;
};

/** 
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();

    if (!this.cache.has(key)) {
        return -1;
    }

    const item = this.cache.get(key);

    // Expired
    if (item.expiry <= now) {
        this.cache.delete(key);
        return -1;
    }

    return item.value;
};

/** 
 * @return {number}
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;

    for (const [key, item] of this.cache) {
        if (item.expiry > now) {
            count++;
        } else {
            this.cache.delete(key);
        }
    }

    return count;
};
