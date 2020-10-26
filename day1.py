class Tank:
    def __init__(self, has_armor):
        self.has_armor = has_armor
        self.armor_strength = 5
        self.owner = None
    
    def print_info(self):
        print(f'The Tank\n{"*"*10}\nArmor: {self.has_armor}\nArmor Strength: {self.armor_strength}\nOwner: {self.owner}')

empty_tank = Tank("Plate")
empty_tank.print_info()

nick_tank = Tank("Plate")
nick_tank.owner = "Nick"
nick_tank.armor_strength = 10
nick_tank.print_info()
