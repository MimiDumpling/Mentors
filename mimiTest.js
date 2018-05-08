// array = [1, 2, 3]

// array[0] = 'Mimi'

// console.log(array)

options = {
    sourceProperty: "src",
    sourceValue: "bar.js"
  }

options['sourceProperty'] = "hi"

console.log(options)
console.log(options.sourceProperty) //src
console.log(options['sourceProperty']) //src
