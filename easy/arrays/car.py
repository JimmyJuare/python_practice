class Character(object):
    def __init__(self, name, special_power):
        self.name = name
        self.special_power = special_power
    def fight(self):
        return 'pow!'
    
    def get_name(self):
        return self.name
    def get_power(self):
        return self.special_power
    def set_power(self, new_power):
        self.special_power = new_power
    def set_name(self, new_name):
        self.name = new_name
        
jacob = Character('Jacob', 'retardation')
jimmy = Character('Jimmy', 'retardation lvl 2')
print(jacob.get_name())
print(jacob.get_power())

print(jimmy.get_name())
print(jimmy.get_power())
