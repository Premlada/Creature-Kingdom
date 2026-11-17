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


# Test code
if __name__ == "__main__":
    dragon = Creature("Dragon", 100, 20)
    goblin = Creature("Goblin", 50, 10)

    dragon.attack(goblin)
    print(goblin.is_alive())
