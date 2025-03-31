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
  #name;
  #age;

  constructor(name, age) {
    super();
    this.#name = name;
    this.#age = age;
  }

  makeSound() {
    console.log("Woof! Woof!");
  }

  getName() {
    return this.#name;
  }

  setName(name) {
    this.#name = name;
  }

  getAge() {
    return this.#age;
  }

  setAge(age) {
    this.#age = age;
  }
}

const animals = [new Dog("Rex", 5), new Dog("Jota", 9)];
for (const animal of animals) {
  console.log(animal.getName());
}
