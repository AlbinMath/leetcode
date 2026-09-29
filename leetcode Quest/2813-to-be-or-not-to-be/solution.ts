function expect(val: any) {
    return {
        toBe(other: any) {
            if (val !== other) {
                throw new Error("Not Equal");
            }

            return true;
        },

        notToBe(other: any) {
            if (val === other) {
                throw new Error("Equal");
            }

            return true;
        }
    };
}
