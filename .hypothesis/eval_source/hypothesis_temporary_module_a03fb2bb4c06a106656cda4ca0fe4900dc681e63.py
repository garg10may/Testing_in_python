from hypothesis.utils.conventions import not_set

def accept(f):
    def test_is_five_prime(self, s=not_set):
        return f(self, s)
    return test_is_five_prime
