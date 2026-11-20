var UndergroundSystem = function() {
    this.checkIns = new Map();
    this.routes = new Map();
};
UndergroundSystem.prototype.checkIn = function(id, stationName, t) {
    this.checkIns.set(id, [stationName, t]);
};
UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    const [startStation, startTime] = this.checkIns.get(id);
    this.checkIns.delete(id);
    
    const key = `${startStation}:${stationName}`;
    const stats = this.routes.get(key) || [0, 0];
    stats[0] += t - startTime;
    stats[1] += 1;
    this.routes.set(key, stats);
};
UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    const [totalTime, tripCount] = this.routes.get(`${startStation}:${endStation}`);
    return totalTime / tripCount;
};
