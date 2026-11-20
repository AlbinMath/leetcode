var TweetCounts = function() {
    this.tweets = new Map();
    this.freqMap = {
        minute: 60,
        hour: 3600,
        day: 86400
    };
};

TweetCounts.prototype.recordTweet = function(tweetName, time) {
    if (!this.tweets.has(tweetName)) {
        this.tweets.set(tweetName, []);
    }
    this.tweets.get(tweetName).push(time);
};

TweetCounts.prototype.getTweetCountsPerFrequency = function(freq, tweetName, startTime, endTime) {
    const delta = this.freqMap[freq];
    const numBuckets = Math.floor((endTime - startTime) / delta) + 1;
    const counts = new Array(numBuckets).fill(0);
    
    const times = this.tweets.get(tweetName) || [];
    for (const t of times) {
        if (t >= startTime && t <= endTime) {
            const idx = Math.floor((t - startTime) / delta);
            counts[idx]++;
        }
    }
    
    return counts;
};
