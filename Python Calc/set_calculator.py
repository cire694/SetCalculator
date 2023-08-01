from enum import Enum, auto
from itertools import combinations

# Attribues
class color(Enum):
    RED = 1
    GREEN = 2
    PURPLE = 3

class num(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

class shading(Enum):
    SOLID = 1
    STRIPE = 2
    EMPTY = 3

class shape(Enum):
    DIAMOND = 1
    SQUIGGLE = 2
    OVAL = 3

class card:
    def __init__(self, number, color, shading, shape):
        self.number = number
        self.color = color
        self.shading = shading
        self.shape = shape

    def __str__(self):
        return f"({self.number.name}, {self.color.name}, {self.shading.name}, {self.shape.name})"
    
class set_calculator: 
    def __init__(self, *cards):
        self.cards = cards
        if len(cards) < 3 or len(cards) % 3 != 0:
            raise ValueError("Invalid Card Amount")
        self.sets = []
        self.find_all_sets()

    def check_num( a, b, c):
        return len(set([a.number, b.number, c.number])) != 2
    
    def check_color( a, b, c):
        return len(set([a.color, b.color, c.color])) != 2
    
    def check_shading(a, b, c):
        return len(set([a.shading, b.shading, c.shading])) != 2
    
    def check_shape( a, b, c):
        return len(set([a.shape, b.shape, c.shape])) != 2
    
    def is_set(self, a, b, c):
        return all([set_calculator.check_num(a, b, c), 
                   set_calculator.check_color(a, b, c),
                   set_calculator.check_shading(a, b, c), 
                   set_calculator.check_shape(a, b, c)])
    def find_all_sets(self):
        for i in range(len(self.cards) - 2):
            first_card = self.cards[i]
            for j in range(i + 1, len(self.cards) - 1):
                second_card = self.cards[j]
                for k in range(j + 1, len(self.cards)):
                    third_card = self.cards[k]

                    if self.is_set(first_card, second_card, third_card):
                        self.sets.append((first_card, second_card, third_card))

    def __str__(self):
        result = "Sets:\n"

        for s in self.sets:
            result += "[ "
            for card in s:
                result += str(card) + ", "
            result = result[:-2] + " ]\n"

        return result
            
    
cards = (
    # Set 1
    card(num.TWO, color.PURPLE, shading.SOLID, shape.OVAL),
    card(num.TWO, color.GREEN, shading.STRIPE, shape.OVAL),
    card(num.TWO, color.RED, shading.EMPTY, shape.OVAL),

    # Set 2
    card(num.ONE, color.RED, shading.STRIPE, shape.OVAL),
    card(num.ONE, color.PURPLE, shading.SOLID, shape.OVAL),
    card(num.ONE, color.GREEN, shading.EMPTY, shape.OVAL),

    # Set 3
    card(num.THREE, color.PURPLE, shading.EMPTY, shape.DIAMOND),
    card(num.THREE, color.GREEN, shading.STRIPE, shape.DIAMOND),
    card(num.THREE, color.RED, shading.SOLID, shape.DIAMOND),

    # Set 4
    card(num.TWO, color.GREEN, shading.SOLID, shape.DIAMOND),
    card(num.THREE, color.PURPLE, shading.SOLID, shape.DIAMOND),
    card(num.ONE, color.RED, shading.STRIPE, shape.DIAMOND),

    # Set 5
    card(num.THREE, color.PURPLE, shading.SOLID, shape.SQUIGGLE),
    card(num.TWO, color.GREEN, shading.STRIPE, shape.SQUIGGLE),
    card(num.ONE, color.RED, shading.EMPTY, shape.SQUIGGLE),
)

calculator = set_calculator(*cards)
print(calculator)

