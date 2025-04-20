# Superhero base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self._power = power  # Protected attribute
        self.city = city

    def display_info(self):
        print(f"{self.name} protects {self.city} using {self._power}!")

    def use_power(self):
        print(f"{self.name} uses {self._power} to fight crime!")


# Derived class: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars at {self.flight_speed} km/h and attacks with {self._power}!")


# Derived class: TechHero
class TechHero(Superhero):
    def __init__(self, name, power, city, gadgets):
        super().__init__(name, power, city)
        self.gadgets = gadgets

    def use_power(self):
        print(f"{self.name} uses gadgets like {', '.join(self.gadgets)} with {self._power} power!")


# Testing the classes
if __name__ == "__main__":
    hero1 = FlyingHero("SkyBlade", "Wind Slash", "SkyCity", 800)
    hero2 = TechHero("Circuit", "Electric Shock", "NeoTown", ["Drone", "EMP Blaster", "Invisibility Cloak"])

    for hero in [hero1, hero2]:
        hero.display_info()
        hero.use_power()
        print()

