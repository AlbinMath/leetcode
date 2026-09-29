class EventEmitter {
    events: Map<string, Function[]>;

    constructor() {
        this.events = new Map();
    }

    subscribe(event: string, cb: Function): { unsubscribe: () => void } {
        if (!this.events.has(event)) {
            this.events.set(event, []);
        }

        const callbacks = this.events.get(event)!;
        callbacks.push(cb);

        return {
            unsubscribe: () => {
                const index = callbacks.indexOf(cb);

                if (index !== -1) {
                    callbacks.splice(index, 1);
                }
            }
        };
    }

    emit(event: string, args: any[] = []): any[] {
        if (!this.events.has(event)) {
            return [];
        }

        const callbacks = this.events.get(event)!;

        return callbacks.map(cb => cb(...args));
    }
}
