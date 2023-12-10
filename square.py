import unittest

def square(n):
    return n*n

def cube(n):
    return n*n*n

class TestCase(unittest.TestCase):
    def test_square(self):
        self.assertEquals(square(4), 16)

    def test_cube(self):
        self.assertEquals(cube(4), 16)