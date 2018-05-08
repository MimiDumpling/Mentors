// Your code here

class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  
  plus(point) {
    const x = Number(point.x);
    const y = Number(point.y);
    
    return new Point(this.x + x, this.y + y);
  }
}

console.log(new Point(1, 2).plus(new Point(2, 1)))
// → Point{x: 3, y: 3}

const test = new Point(4,4)
console.log(test)
