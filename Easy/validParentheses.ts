// Easy

function isValid(s: string): boolean {
  let stack: string[] = [];
  const validMap: { [key: string]: string } = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  for (const c of s) {
    if (c in validMap) {
      const first = stack.length > 0 ? stack[stack.length - 1] : "";

      if (first === validMap[c]) {
        stack.pop();
      } else {
        return false;
      }
    } else {
      stack.push(c);
    }
  }
  return stack.length === 0 ? true : false;
}
