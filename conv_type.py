import logging

log = logging.getLogger(__name__)

__author__ = 'andriod'


class Field(object):
    def __init__(self, fname):
        self.fname = fname

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.fname]

    def __set__(self, instance, value):
        instance.__dict__[self.fname] = self.conv_type(value)


class String(Field):
    conv_type = str


class Int(Field):
    conv_type = int
