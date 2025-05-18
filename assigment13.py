"""
Create a class Engine and a class Car. Use composition 
by passing an Engine object to the Car class during initialization.
Access a method of the Engine class via the Car class.
"""

class Engine():
    def start(self):
        print("Engine started")
        
    def stop(self):
        print("Engine stopped")
        
        
class Car(Engine):
    def __init__(self,name, model):
        self.name = name
        self.model = model
        self.engine = Engine()
        
    def start_engine(self):
        print(f"{self.name} {self.model} engine is starting...")
        self.engine.start()
        self.engine.stop()
        
e = Engine()
c = Car("TOYOTO", 2022)
c.start_engine()