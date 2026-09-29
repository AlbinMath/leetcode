type JSONValue =
    | null
    | boolean
    | number
    | string
    | JSONValue[]
    | { [key: string]: JSONValue };

function compactObject(obj: JSONValue): JSONValue {
    // Handle arrays
    if (Array.isArray(obj)) {
        return obj
            .filter(Boolean)
            .map((item) => compactObject(item));
    }

    // Handle objects
    if (typeof obj === "object" && obj !== null) {
        const result: { [key: string]: JSONValue } = {};

        for (const key in obj) {
            if (Boolean(obj[key])) {
                result[key] = compactObject(obj[key]);
            }
        }

        return result;
    }

    // Primitive truthy values
    return obj;
}
