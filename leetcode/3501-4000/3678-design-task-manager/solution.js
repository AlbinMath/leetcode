class TaskMaxHeap {
    constructor() {
        this.data = [];
    }
    size() {
        return this.data.length;
    }
    _higherPriority(a, b) {
        if (a[0] !== b[0]) return a[0] > b[0];
        return a[1] > b[1];
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
var TaskManager = function(tasks) {
    this.taskInfo = new Map();
    this.heap = new TaskMaxHeap();
    
    for (const [userId, taskId, priority] of tasks) {
        this.taskInfo.set(taskId, [userId, priority]);
        this.heap.push([priority, taskId, userId]);
    }
};
TaskManager.prototype.add = function(userId, taskId, priority) {
    this.taskInfo.set(taskId, [userId, priority]);
    this.heap.push([priority, taskId, userId]);
};
TaskManager.prototype.edit = function(taskId, newPriority) {
    const [userId] = this.taskInfo.get(taskId);
    this.taskInfo.set(taskId, [userId, newPriority]);
    this.heap.push([newPriority, taskId, userId]);
};
TaskManager.prototype.rmv = function(taskId) {
    this.taskInfo.delete(taskId);
};
TaskManager.prototype.execTop = function() {
    while (this.heap.size() > 0) {
        const [priority, taskId, userId] = this.heap.pop();
        const current = this.taskInfo.get(taskId);
        if (current && current[0] === userId && current[1] === priority) {
            this.taskInfo.delete(taskId);
            return userId;
        }
    }
    return -1;
};
