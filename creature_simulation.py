
class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.hp -= self.attack_power
        print(f"{target.name} has {target.hp} HP remaining.")

    def is_alive(self):
        return self.hp > 0


class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power, altitude=0):
        super().__init__(name, hp, attack_power)
        self.altitude = altitude

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to {self.altitude} meters.")

    def attack(self, target):
        print(f"{self.name} attacks {target.name} from above!")
        target.hp -= self.attack_power
        print(f"{target.name} has {target.hp} HP remaining.")


class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power, depth=0):
        super().__init__(name, hp, attack_power)
        self.depth = depth

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to {self.depth} meters.")

    def attack(self, target):
        print(f"{self.name} attacks {target.name} underwater!")
        target.hp -= self.attack_power
        print(f"{target.name} has {target.hp} HP remaining.")


class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = fire_level

    def emit_fire(self, new_fire_level):
        self.fire_level = max(0, min(100, new_fire_level))
        print(f"{self.name} increases fire level to {self.fire_level}.")

    def attack(self, target):
        damage = self.attack_power + self.fire_level
        print(f"{self.name} attacks {target.name} with fire!")
        target.hp -= damage
        print(f"{target.name} has {target.hp} HP remaining.")


if __name__ == "__main__":
    dragon = FlyingCreature("Dragon", 100, 20)
    shark = SwimmingCreature("Shark", 100, 25)
    phoenix = FireCreature("Phoenix", 100, 15)
    goblin = Creature("Goblin", 100, 10)

    dragon.fly_to(100)
    dragon.attack(goblin)

    shark.dive_to(50)
    shark.attack(goblin)

    phoenix.emit_fire(50)
    phoenix.attack(goblin)

    print(goblin.is_alive())
