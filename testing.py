


from hypothesis import given, example
import hypothesis.strategies as st
import unittest


def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(2,number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)


            
class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    @given(st.integers())
    def test_is_five_prime(self,s):
        """Is five successfully determined to be prime?"""
        self.assertFalse(is_prime(s))

if __name__ == '__main__':
    unittest.main()