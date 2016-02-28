from req_type import Field


class TypeBase(type):
    def __new__(cls, name, bases, cls_dict):
        new_dict = {}
        for key, value in cls_dict.items():
            if isinstance(value, type) and issubclass(value, Field):
                new_dict[key] = value(key)
            else:
                new_dict[key] = value

        return super(TypeBase, cls).__new__(cls, name, bases, new_dict)