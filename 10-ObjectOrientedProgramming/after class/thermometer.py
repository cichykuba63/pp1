import random

class Thermometer:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure_temp(self):
        if self.is_on:
            self.temperature = round(random.randint(34, 42) + random.random(), 1)
        else:
            print("Turn on the thermometer first.")

    def display_temp(self):
        if self.is_on:
            try:
                if self.temperature < 37.0:
                    print(f"Temperature: {self.temperature}")
                elif self.temperature >= 37.0 and self.temperature < 41.0:
                    print(f"Temperature: {self.temperature} (fever)")
                elif self.temperature >= 41.0:
                    print(f"Temperature: {self.temperature} (CRITICAL TEMPERATURE!)")
        
            except AttributeError:
                print("Measure Temperature first.")
            
        else:
            print("Turn on the thermometer first.")