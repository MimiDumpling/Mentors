// import sys

// """
// Given an unsorted list of integers, find the 
// two integers with the lowest difference between
// their values. Return the difference of those
// two integers.

// BONUS: solve for 2 unsorted lists
// BONUS: re-write with no maxsize and start at index 1
// """

// def short_dist(integers):

//     lst = sorted(integers)
//     diff = sys.maxsize

//     for index, n in enumerate(lst):
//         if index < len(lst) - 1:
//             x = lst[index + 1] - n
//             if x < diff:
//                 diff = x

//     return diff

// print "+++TESTS+++"
// print "Correct Answer: 1, Result: ", short_dist([47, 1, 12, 48, 9, 23])
// print "Correct Answer: 3, Result: ", short_dist([1, 4, 100])
// print "Correct Answer: 2, Result: ", short_dist([2, 0])

function shortDist (integers) {
  const array = integers.sort(function(a, b){return a - b}) 
  console.log(array)

  // gives a bigass number
  // diff = Math.floor(Math.random() * 1000000000);

  diff = array.reduce((diff, value, index) => {
    const nextValue = array[index + 1];

    if (nextValue - value < diff) {
      return nextValue - value;
    }
    return diff;
  }, array[-1])

  // for (const index in array) {
  //   if (index < (array.length - 1)) {
  //     index2 = Number(index) + 1
  //     x = Number(array[index2]) - Number(array[index]);

  //     if (x < diff) {
  //       diff = x
  //     }
  //   }
  // }

  return diff
}

console.log("+++TESTS+++")
console.log("Correct Answer: 1, Result: ", shortDist([47, 1, 12, 48, 9, 23]))
console.log("Correct Answer: 3, Result: ", shortDist([1, 4, 100]))
console.log("Correct Answer: 2, Result: ", shortDist([2, 0]))