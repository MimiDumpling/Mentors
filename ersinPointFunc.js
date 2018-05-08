//write the Point class as a function

// class Point {
//   constructor(x, y) {
//     this.x = x, this.y = y
//   }
//   add(other) {
//     return new Point(this.x + other.x, this.y + other.y)
//   }
// }

const Point = (x, y) => {}

Point.prototype = {
    constructor: (x,y) => {this.x = x, this.y = y},
    add: (other) => {return new Point(this.x + other.x, this.y + other.y)}
}

console.log(new Point(1, 2))