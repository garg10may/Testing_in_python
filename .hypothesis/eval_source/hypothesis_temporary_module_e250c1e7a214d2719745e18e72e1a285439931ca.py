from hypothesis.utils.conventions import not_set

def accept(f):
    def test_encoding_decoding(self=not_set):
        return f(self)
    return test_encoding_decoding
