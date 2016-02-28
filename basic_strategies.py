import pickle


class demo_obj(object):
    def __init__(self, x, right, left):
        self.left = left
        self.right = right
        self.x = x

    def ignore_it(self):

        print(self.x)
        print(self.right > self.left)
        return pickle.dumps(self)

    def convert_it(self, seq_or_list, value):

        self.x = int(self.x)
        self.array = list(seq_or_list)
        self.value = value * 1.0
        return self.x * self.array

    def check_it(self, vals):

        assert isinstance(self.x, str)
        if not isinstance(self.left, self.right.__class__):
            raise TypeError('Left and right must be matching types')
        if not all(isinstance(x, (str, int, float, bool, None)) for x in vals):
            raise TypeError('Unable to convert to json')
        return 'OK'


myObj = demo_obj('2', 5, 6.0)
myObj.ignore_it()
myObj.convert_it('Hi!', 3)
print(myObj.x)
print(myObj.array)
print(myObj.value)

# Will fail, x is no longer a str because convert it converted
# myObj.check_it([1,'Hi',8.90,'JSON Data'])

# Will fail, 5 and 6.0 are not matching types
# myObj = demo_obj('2', 5, 6.0)
# myObj.check_it([1,'Hi',8.90,'JSON Data'])

myObj = demo_obj('2', 5, 6)
print(myObj.check_it([1, 'Hi', 8.90, 'JSON Data']))
