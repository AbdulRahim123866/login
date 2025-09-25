class Car:
    def __init__(self,make=None,model=None,year=None,color=None,engine=None):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.engine=engine

    def __str__(self):
        return f"{self.year} {self.make} {self.model} with {self.engine} engine"


class CarBuilder:
    def __init__(self):
        self._car=Car()

    def set_make(self,make):
        self._car.make=make
        return self
    def set_model(self,model):
        self._car.model=model
        return self
    def set_year(self,year):
        self._car.year=year
        return self
    def set_color(self,color):
        self._car.color=color
        return self
    def set_engine(self,engine):
        self._car.engine=engine
        return self
    def build(self):
        if not self._car.color:
            raise ValueError(f"Color is not built")
        return self._car

if __name__=="__main__":
    builder=CarBuilder()
    car=(builder.set_make("Toyota")
         .set_model("Camry")
         .set_year(2025)
         .set_color("White")
         .set_engine("Hybrid")
         .build())
    print(car)