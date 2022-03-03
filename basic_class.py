# Classes are wrappers for our data and methods(function)

class Car:

    def __init__(self, name: str, model: str, color: str = "") -> None:
        # constructor 
        self.name = name
        self.model = model
        self.color = color

    def __str__(self):
        return f"name: {self.name}, model: {self.model}, color: {self.color}"

    def fill_gas(self) -> None:
        print(f"{self.name} is filled.")


my_car = Car("lightning", "porshe", "red")
print(my_car)
print(type(my_car))
my_car.fill_gas()

# dict_car = {"name": "lightning", "model":"porshe", "color":"red"}
# print(dict_car)
# print(type(dict_car))


# inheritance

# Create a class as a subclass of another class

class Tesla(Car):
    
    def fill_gas(self) -> None:
        print(f"{self.name} is electric baby.")

my_tesi = Tesla("tesi", "model_S", "white")
my_tesi.fill_gas()
