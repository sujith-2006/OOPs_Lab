# Write program to demonstrate constructor channing / constructor overriding

class Vehicle:
    def __init__(self, engine):
        print("Inside Vehicle Constructor")
        self.engine = engine
    
class Car(Vehicle):
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print("Inside Car Constructor")
        self.max_speed = max_speed
        

class Electric_Car(Car):
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print("Inside Electric Car Constructor")
        self.km_range = km_range
        