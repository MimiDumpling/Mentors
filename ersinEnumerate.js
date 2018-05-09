// """
// Write a function that takes two lists of numbers, 
// of equal length, containing the same numbers, 
// but in scrambled order. 
// so for example, [41, 27, 12, 8] and [8, 27, 12, 41]. 
// return a list of tuples that maps 
// from one list to another - each tuple contains the index 
// of a number in the first list, and then the index of 
// that same number in the second list. it's okay 
// if the runtime is n^2.
// so for that example I gave, 
// the result would be: [(0, 3), (1, 1), (2, 2), (3, 0)]
// """

// def tuple_map(lst1, lst2):

//     result = []

//     for index1, number1 in enumerate(lst1):
//         for index2, number2 in enumerate(lst2):
//             if lst1[index1] == lst2[index2]:
//                 result.append((index1, index2))

//     return result

// print tuple_map([41, 27, 12, 8], [8, 27, 12, 41])

// renamed function because JavaScript doesn't support tuples
function arrayMap(array1, array2) {
  const result = []

  for (const index1 in array1) {
    const num1 = array1[index1];

    for (const index2 in array2) {
      const num2 = array2[index2];

      if (array1[index1] === array2[index2]) {
        result.push([index1, index2])
      }
    }
  }
  return result
}

console.log(arrayMap([41, 27, 12, 8], [8, 27, 12, 41]))
// Answer: [[0, 3], [1, 1], [2, 2], [3, 0]