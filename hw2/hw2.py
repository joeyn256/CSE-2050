import random
random.seed(652)
class Card:
    def __init__(self, number, color, shading, shape):
        self.number = number
        self.color = color
        self.shading = shading
        self.shape = shape
    def __str__(self):
        return f"Card({self.number}, {self.color}, {self.shading}, {self.shape})"
    # repr() is called instead of str() by some of pytho's built-ins. We'll always
    # want the same value returned in this course, so we can piggyback off of str
    def __repr__(self): return str(self)

    def __eq__(self, other):
        return str(self) == str(other)

# Valid values for default game of GROUP! included here to avoid spelling
# issues. Feel free to copy/paste:
# [1, 2, 3]
# ['diamond', 'squiggle', 'oval']
# ['green', 'blue', 'purple']
# ['empty', 'striped', 'solid']

class Deck:

    def __init__(self, numbers = [1, 2, 3], colors = ['green', 'blue', 'purple'], shadings = ['empty', 'striped', 'solid'], shapes = ['diamond', 'squiggle', 'oval']):
        self.my_nums = numbers
        self.my_shadings = shadings
        self.my_cols = colors
        self.my_shapes = shapes
        
        deck_list1 = []
        
        for i in self.my_nums:
            for j in self.my_cols:
                for k in self.my_shadings:
                    for l in self.my_shapes:
                        deck_list1.append(Card(i,j,k,l))
        self.deck_list = deck_list1
        # makes deck list
    
    def __len__(self):
        x = 0
        for i in self.deck_list:
            x += 1
        return x

    # should return number of items in deck
    # should remove and return top card
    def draw_top(self):
        if len(self) > 0:
            return self.deck_list.pop(len(self) -1)
        else:
            raise AttributeError

    # should randomly shuffle cards. Does not need a return.
    def shuffle(self):
        return random.shuffle(self.deck_list)
# Oonce Card and Deck are both finished, write tests for this algorithm, then
# write the algorithm

# True if, for all attributes, each card has the same or different values;
# e.g. {1, 1, 1} or {1, 2, 3}, but not {1, 1, 3}
def is_group(self,other,last):
    if self.number == other.number == last.number:
        return True
    elif self.color == other.color == last.color:
        return True
    elif self.shading == other.shading == last.shading:
        return True
    elif self.shape == other.shape == last.shape:
        return True
    elif (self.number != other.number and self.number != last.number and other.number != last.number) and (self.color != other.color and self.color != last.color and other.color != last.color) and (self.shading != other.shading and self.shading != last.shading and other.shading != last.shading) and (self.shape != other.shape and self.shape != last.shape and other.shape != last.shape):
        return True
    else:
        return False