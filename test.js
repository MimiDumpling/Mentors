class SortedArray {
  constructor(compare) {
    this.compare = compare;
    this.content = [];
  }
  
  insert(elt) {
    const pos = this.content.findIndex(x => this.compare(elt, x) < 0)
    
  	this.content.splice(pos, 0, elt);
  }
}

var sorted = new SortedArray(function(a, b) { return a - b })
sorted.insert(5)
sorted.insert(1)
sorted.insert(2)
sorted.insert(4)
sorted.insert(3)
console.log("array:", sorted.content)

function(x) {
  return x;
}

(x) => { return x; }
(x) => (x)
x => (x)
x => x

const answer = x => x

function(x, y) {
  return x + y;
}

(x, y) => { return x + y; }
(x, y) => (x + y)
(x, y) => x + y

function() {
  return;
}

() => ()
x => {}
() => {}

function (x) {
  x++;
  x += 5;
  return x;
}

(x) => {x++; x += 5; return x;}
x => {x++; x += 5; return x;}
