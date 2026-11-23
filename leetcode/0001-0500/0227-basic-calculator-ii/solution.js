/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
  const stack = [];
  let num = 0;
  let op = '+'; // operator preceding the current number

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];

    if (ch >= '0' && ch <= '9') {
      num = num * 10 + (ch.charCodeAt(0) - 48);
    }

    // Process when we hit an operator, or reach the end of the string
    if ((ch !== ' ' && (ch < '0' || ch > '9')) || i === s.length - 1) {
      if (op === '+') {
        stack.push(num);
      } else if (op === '-') {
        stack.push(-num);
      } else if (op === '*') {
        stack.push(stack.pop() * num);
      } else if (op === '/') {
        stack.push(Math.trunc(stack.pop() / num));
      }
      op = ch;
      num = 0;
    }
  }

  return stack.reduce((a, b) => a + b, 0);
};
