type JSONValue =
    | null
    | boolean
    | number
    | string
    | JSONValue[]
    | { [key: string]: JSONValue };

Function.prototype.callPolyfill = function(
    context: any,
    ...args: any[]
): any {
    const key = Symbol();

    context[key] = this;

    const result = context[key](...args);

    delete context[key];

    return result;
};
