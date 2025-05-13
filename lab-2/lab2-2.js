// shape.js (базовий інтерфейс)
class Shape {
  getArea() {
    throw new Error("Method not implemented");
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }

  getArea() {
    return Math.PI * this.radius * this.radius;
  }
}

// обчислення загальної площі
class AreaCalculator {
  constructor(shapes) {
    this.shapes = shapes;
  }

  calculateTotalArea() {
    return this.shapes.reduce((sum, shape) => sum + shape.getArea(), 0);
  }
}

// main.js (використання)
const shapes = [new Rectangle(4, 5), new Circle(3), new Rectangle(2, 2)];

const calculator = new AreaCalculator(shapes);
console.log("Total Area:", calculator.calculateTotalArea());
