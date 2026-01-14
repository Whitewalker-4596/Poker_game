import unittest

def product(a,b):
    # result = 0
    # for i in range(a):
    #     result+=b
    # return result
    return a*b

class TestMultiply(unittest.TestCase):
    def test_multiply_two_numbers(self):
        self.assertEqual(product(3,4), 12)
        # result = 0
        # for i in range(a):
        #     result+=b


if __name__ == "__main__":
    unittest.main()
