import unittest

from fullstack.server.elena.parse.parser import *


class TestParsing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodeStorage = parse("srtm_prod.osm")

    def test_parseCheck(self):
        self.assertEqual(len(self.nodeStorage.nodeMap), 10684)


if __name__ == '__main__':
    unittest.main()
