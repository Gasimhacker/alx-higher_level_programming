#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let max = process.argv[2];
  let oldMax = max;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      oldMax = max;
      max = process.argv[i];
    }
  }
  console.log(oldMax);
}
