class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Этот звук издает животное."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Гав-гав!"

    def get_breed(self):
        return f"Порода: {self.breed}"

if __name__ == "__main__":
    generic_animal = Animal("Животное")
    print(f"{generic_animal.name} говорит: {generic_animal.speak()}")

    my_dog = Dog("Бобик", "Овчарка")
    print(f"{my_dog.name} говорит: {my_dog.speak()}")
    print(my_dog.get_breed())