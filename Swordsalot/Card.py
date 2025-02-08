
class Card:
    use = ""
    quantity = 0
    name = ""
    strength = 0
    rarity = ""

    def __init__(self, quantity:int):
        self.quantity = quantity

    def __str__(self):
        return f'{self.use}: {self.name} x{self.quantity}'


class Attack(Card):
    use = "Attack"

class Defense(Card):
    use = "Defense"

class Slash(Attack):
    strength = 0
    name = "Slash"
    rarity = "C"
    
    def __init__(self, quantity: int, strength: int):
        super().__init__(quantity)
        self.strength = strength

class Shield(Defense):
    strength = 0
    name = "Shield"
    rarity = "C"

    def __init__(self, quantity:int, strength: int):
        super().__init__(quantity)
        self.strength = strength

class Movement(Card):
    strength = 0
    use = "Movement"
    def __init__(self, quantity:int, strength: int):
        self.quantity = quantity
        self.strength = strength

class Charge(Movement):
    name = "Charge"
    direction = "For"
    rarity = "C"

class Retreat(Movement):
    name = "Retreat"
    direction = "Back"
    rarity = "C"

class Strafe(Movement):
    name = "Strafe"
    direction = "Side"
    rarity = "C"

class Walk(Movement):
    name = "Walk"
    direction = "Any"
    rarity = "C"