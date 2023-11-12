class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

car1 = Car("Toyota", "Camry", 2019, 50000)
print(car1.get_brand())  
print(car1.get_model())  
print(car1.get_year())  
print(car1.get_mileage())  

car1.set_brand("Honda")
car1.set_model("Accord")
car1.set_year(2020)
car1.set_mileage(60000)
print(car1.get_brand())  
print(car1.get_model())  
print(car1.get_year())  
print(car1.get_mileage())  
