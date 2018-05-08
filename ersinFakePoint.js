// Use a single object literal to create an object that is 
// indistinguishable from a Point instance, without 
// calling the Point constructor.

class Point {
  constructor(x, y) {
    this.x = x, this.y = y
  }
  add(other) {
    return new Point(this.x + other.x, this.y + other.y)
  }
}

// YOUR CODE HERE
const fakePoint = {x:2, y:2}
fakePoint.__proto__ = Point.prototype
console.log(typeof fakePoint)

// TEST
console.log(fakePoint instanceof Point)