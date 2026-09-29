type P = () => Promise<any>;

function promiseAll(functions: P[]): Promise<any[]> {
    return new Promise((resolve, reject) => {
        const results: any[] = [];
        let completed = 0;

        for (let i = 0; i < functions.length; i++) {
            functions[i]()
                .then((value) => {
                    results[i] = value;
                    completed++;

                    // All promises completed
                    if (completed === functions.length) {
                        resolve(results);
                    }
                })
                .catch((error) => {
                    reject(error);
                });
        }
    });
}
