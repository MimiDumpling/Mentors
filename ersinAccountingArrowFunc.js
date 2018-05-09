// Write an expression using higher-order array methods 
// (say, filter and reduce) to compute the total value 
// of the machines in the inventory array.

const inventory = [
  {type:   "machine", value: 5000},
  {type:   "machine", value:  650},
  {type:      "duck", value:   10},
  {type: "furniture", value: 1200},
  {type:   "machine", value:   77}
]

//let totalMachineValue = YOUR_CODE_HERE

let justMachines = (obj) => obj['type'] === 'machine';
let getValues = (accumulator, obj) => accumulator + obj.value;
let getSum = (total, num) => total + num;

const machines = inventory.filter(justMachines)
const values = machines.reduce(getValues, 0)

console.log(`Answer: `, values)

// console.log(totalMachineValue)
// 5727