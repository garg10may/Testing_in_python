from hypothesis.utils.conventions import not_set

def accept(f):
    def test_encoding_decoding(self, s=not_set):
        return f(self, s)
    return test_encoding_decoding
