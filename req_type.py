import logging

log = logging.getLogger(__name__)

__author__ = 'andriod'





class Field(object):
    def __init__(self, fname):
        self.fname = fname
    def __get__(self, instance, owner = None):
        return instance.__dict__[self.fname]
    def __set__(self, instance, value):
        if not isinstance(value, self.req_type):
            raise TypeError("Field %s must of type %s."%(self.fname,self.req_type))
        instance.__dict__[self.fname] = value

class String(Field):
    req_type = str

class Int(Field):
    req_type = int






