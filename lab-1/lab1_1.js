class Animal {
  makeSound() {
    throw new Error(
      "Метод makeSound() повинен бути реалізований у похідному класі."
    );
  }

  sleep() {
    console.log(`${this.constructor.name} is sleeping...`);
  }
}

class Dog extends Animal {
  makeSound() {
    console.log("Woof! Woof!");
  }
}

class Cat extends Animal {
  makeSound() {
    console.log("Meow! Meow!");
  }
}

const dog = new Dog();
const cat = new Cat();

dog.makeSound();
cat.makeSound();

dog.sleep();
cat.sleep();
