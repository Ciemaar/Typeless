class CheckComparable(object):
    def __set__(self, instance, value):
        for fname, field in instance.__class__.__dict__.items():
            if field == self:
                continue
            if isinstance(field, self.__class__) and fname in instance.__dict__:
                # test compare, do not accept a non-comparable type
                value > getattr(instance, fname)
        instance.__dict__[self.fname] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.fname]

    def __delete__(self, instance):
        del instance.__dict__[self.fname]

    def __init__(self, fname):
        self.fname = fname


class Node(object):
    left = CheckComparable('left')
    right = CheckComparable('right')


node = Node()
node.left = 5
node.right = 15
try:
    node.right = '15'
except TypeError:
    print('Got Expected TypeError')

del node.left
node.right = '15'
node.left = '5'
