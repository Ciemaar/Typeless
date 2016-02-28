import unittest

import req_type
import typeless


class MetaclassTestCase(unittest.TestCase):
    def setUp(self):
        super(MetaclassTestCase, self).setUp()

        class Holder(object, metaclass=typeless.TypeBase):

            name = req_type.String
            count = req_type.Int

        self.holder = Holder

    def test_basic(self):
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