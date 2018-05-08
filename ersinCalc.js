// """Calculate the equation inside the list in order of operation.
// The first and last item will always be a number. Numbers are
// separated by a + or * symbol. All items are in individual strings.
// Examples:
    
//     >>> calculate(["6", "+", "8", "*", "12", "+", "47"])
//     149
//     >>> calculate(["1", "+", "1", "+", "1"])
//     3
//     >>> calculate(["1", "+", "1", "*", "1", "+", "20"])
//     22
// """

// def calculate(lst):
//     """Mathematically calculates items inside list in order of operation."""

//     new_lst = []

//     if "*" in lst:
//         for index in range(len(lst) - 1):
//             if lst[index] == "*":
//                 product = int(lst[(index - 1)]) * int(lst[(index + 1)])
//                 new_lst.append(product)
//                 lst.pop(index - 1)
//                 new_lst.pop(index - 1)
//             else:
//                 new_lst.append(lst[index])
//         # print new_lst
//     else:
//         for index in range(len(lst)):
//             new_lst.append(lst[index])
//         # print new_lst


//     another_lst = []
        
//     for item in new_lst:
//         if item != "+":
//             another_lst.append(int(item))


//     result = 0
    
//     for n in another_lst:
//         result += n

//     return result

function calculate(array){
    const newArray = []
    console.log(array)

    if(array.includes("*")) {
      for(const index in array) {
        if(array[index] === "*") {
          const product = Number(array[(index - 1)]) * Number(array[(Number(index) + 1)])
          
          newArray.push(product)
          newArray.splice(index - 1, 1)
          array.splice(index, 1)
        } else {
          newArray.push(array[index])
        }
      }
    } else {
      for(const index in array) {
        newArray.push(array[index])
      }
    }
    const sumArray = []
    console.log(`This is the newArray: `, newArray)

    for(const num of newArray) {
      if(num != "+") {
        sumArray.push(parseInt(num))
      }
    }

    let result = 0
    console.log(`This is sumArray: `, sumArray)

    for(const num of sumArray) {
      console.log(`This is a num: `, Number(num))
      result += Number(num)
    }

    return result
}

console.log(calculate(["1", "+", "2", "*", "3", "+", "20"])) //27
console.log(calculate(["1", "+", "1", "+", "1"])) //3
console.log(calculate(["6", "+", "8", "*", "12", "+", "47"])) //149