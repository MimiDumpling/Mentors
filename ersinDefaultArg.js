// It would be nice to be able to call our `lastIndexOf` function 
// without providing the third argument, and have it default to 
// starting at the end of the array. It would be even nicer if 
// we could express this with an ES6 default argument value. Can we?

// In which scope are default arguments evaluated? 
// (Experiment to find out.)

function lastIndexOf(arr, elt, start = arr[arr.length - 1]) {
  // One way to set start's default at 0:
  // start = start || 0

  for (let i = start - 1; i >= 0; i--)
    if (arr[i] === elt) return i
  return -1
}

console.log(lastIndexOf([1, 2, 1, 2], 2))


