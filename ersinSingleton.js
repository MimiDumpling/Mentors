// Add a get method to the ids object, 
// which returns the next id and increments 
// its next counter. Use the short method syntax.

var ids = {
  next: 0,
  get: function () {
  	const result = this.next;
    this.next += 1
    return result
    // this also works: this.next++
  },
}

console.log(ids.get())
// → 0
console.log(ids.get())
// → 1
