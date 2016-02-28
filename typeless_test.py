import logging

log = logging.getLogger(__name__)

import req_type

__author__ = 'andriod'
logging.basicConfig()

import unittest


class DescriptorTestCase(unittest.TestCase):
    def setUp(self):
        super(DescriptorTestCase, self).setUp()

        class Holder(object):
            name = req_type.String('name')
            count = req_type.Int('count')
        self.holder = Holder

    def test_fields(self):
        to = self.holder()
        to.name = "Hi"
        to.count = 3

        try:
            to.name = 3
        except TypeError:
            pass
        else:
            assert False, "Failed to generate type error"

        try:
            to.count = "3"
        except TypeError:
            pass
        else:
            assert False, "Failed to generate type error"


if __name__ == '__main__':
    unittest.main()
