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



# Test code
if __name__ == "__main__":
    shark = SwimmingCreature("Shark", 100, 25)
    fish = Creature("Fish", 50, 10)

    shark.dive_to(50)
    shark.attack(fish)

    print(fish.is_alive())

