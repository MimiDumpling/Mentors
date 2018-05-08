function calculate(array){
    const newArray = []
    console.log(array)

    if(array.includes("*")) {
      for(const index in array) {
        if(array[index] === "*") {
          const product = Number(array[(index - 1)]) * Number(array[(Number(index) + 1)])
          //const newArray = Array.map(array, (element) => (element + 1))
          
          //const newArray = array.reduce((acc, value) => {
          //   acc[value] = value;
          //   return acc;
          // }, {});
          
          newArray.push(product)
          newArray.splice(index - 1, 1)
          
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
      result += Number(num)
    }

    return result
}

console.log(calculate(["1", "+", "2", "*", "3", "+", "20"])) //27
console.log(calculate(["1", "+", "1", "+", "1"])) //3
console.log(calculate(["6", "+", "8", "*", "12", "+", "47"])) //149