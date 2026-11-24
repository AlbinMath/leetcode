class EventHeap {
    constructor() {
        this.data = [];
    }
    size() {
        return this.data.length;
    }
    _higherPriority(a, b) {
        if (a[0] !== b[0]) return a[0] > b[0];
        return a[1] < b[1];
    }
    push(val) {
        this.data.push(val);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this._higherPriority(this.data[p], this.data[i])) break;
            [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
            i = p;
        }
    }
    pop() {
        const top = this.data[0];
        const last = this.data.pop();
        if (this.data.length > 0) {
            this.data[0] = last;
            let i = 0;
            const n = this.data.length;
            while (true) {
                let best = i;
                const l = (i << 1) + 1;
                const r = (i << 1) + 2;
                if (l < n && this._higherPriority(this.data[l], this.data[best])) best = l;
                if (r < n && this._higherPriority(this.data[r], this.data[best])) best = r;
                if (best === i) break;
                [this.data[i], this.data[best]] = [this.data[best], this.data[i]];
                i = best;
            }
        }
        return top;
    }
}
var EventManager = function(events) {
    this.activePriority = new Map();
    this.heap = new EventHeap();
    
    for (const [eventId, priority] of events) {
        this.activePriority.set(eventId, priority);
        this.heap.push([priority, eventId]);
    }
};
EventManager.prototype.updatePriority = function(eventId, newPriority) {
    this.activePriority.set(eventId, newPriority);
    this.heap.push([newPriority, eventId]);
};
EventManager.prototype.pollHighest = function() {
    while (this.heap.size() > 0) {
        const [priority, eventId] = this.heap.pop();
        if (this.activePriority.get(eventId) === priority) {
            this.activePriority.delete(eventId);
            return eventId;
        }
    }
    return -1;
};
