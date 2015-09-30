from hypothesis.utils.conventions import not_set

def accept(f):
    def test_decode_inverts_encode(s=not_set):
        return f(s)
    return test_decode_inverts_encode
