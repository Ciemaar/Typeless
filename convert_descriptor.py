from fractions import Fraction


class ExploreDescriptor(object):
    '''Exploratory Descriptor'''
    def __init__(self, fname):
        self.fname = fname

    def __get__(self, instance, owner):
        print('Doing get for %s on object %s'%(self.fname, instance))
        if instance is None:
            return self
        return instance.__dict__[self.fname]

    def __set__(self, instance, value):
        print('Doing set for %s on object %s'%(self.fname, instance))
        instance.__dict__[self.fname] = value

    def __delete__(self, instance):
        print('Doing delete for %s on object %s'%(self.fname, instance))
        del instance.__dict__[self.fname]

class PositiveFraction(object):
    '''Force field value to be a positive fraction'''
    def __init__(self, fname):
        self.fname = fname

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.fname]

    def __set__(self, instance, value):
        instance.__dict__[self.fname] = max(Fraction(value), 0)

class Components(object):
    amount = PositiveFraction('amount')

    def __init__(self, ingredient, amount, unit):
        self.unit = unit
        self.ingredient = ingredient
        self.amount = amount

print()

recipe = [
    Components('Olive Oil', .75, 'cups'),
    Components('Vinegar', '.25', 'cups'),
    Components('Dijion Mustard', 1, 'tablespoons'),
    Components('Salt', '1/4', 'teaspoons'),
    Components('Pepper', 1 / 2, 'teaspoons')
]

for c in recipe:
    print('%s %s - %s'%(c.amount,c.unit, c.ingredient))

print()
print(Components.amount)
print(c.amount)
