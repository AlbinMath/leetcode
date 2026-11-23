function cancellable(
    generator: Generator<Promise<any>, any, any>
): [() => void, Promise<any>] {

    let cancelled = false;
    let finished = false;

    const promise = new Promise<any>((resolve, reject) => {

        function step(
            method: "next" | "throw",
            value?: any
        ): void {

            if (finished) return;

            let result: IteratorResult<any>;

            try {
                result = generator[method](value);
            } catch (error) {
                finished = true;
                reject(error);
                return;
            }

            if (result.done) {
                finished = true;
                resolve(result.value);
                return;
            }

            Promise.resolve(result.value).then(
                (value) => {
                    if (cancelled) {
                        step("throw", "Cancelled");
                    } else {
                        step("next", value);
                    }
                },
                (error) => {
                    step("throw", error);
                }
            );
        }

        step("next");
    });

    const cancel = () => {
        if (!finished) {
            cancelled = true;
        }
    };

    return [cancel, promise];
}
