// """
// Make a string of numbers into an integer without using int().
// Given a function called digit().

// def digit(digit_str):
//     Converts a single character into an integer
//     Ex) "5" -> 5

// Also called string to integer.
// Try integer to string.
// "512"
// 5 *= 10
// 50 + 1
// 510 + 2

// Remember pow() 
// pow(10, 2) -> 10^2
// """

// def make_int(string):
//     splitted = list(string)
//     power = len(splitted) - 1
//     summation = 0

//     for item in splitted:
//         n_item = digit(item)
//         summation += pow(10, power) * n_item
//         power -= 1

//     return summations

function makeInt(string) {
  let power = string.length - 1;
  let summation = 0;

  for (const element of string) {
    // digit() is a method given for prob
    // Converts a single character into an integer

    const current = Number(element);
    const addOn = Math.pow(10, power) * current;
    summation += addOn;
    power -= 1;
  }

  return summation
}

console.log(makeInt("453"))
console.log(typeof makeInt("453"))