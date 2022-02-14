# !! ---------- test_cipher.py ---------- !!
# Test that cipher.py works as expected
# 
# Ben Carpenter
# February 14, 2022
# ------------- test_cipher.py -------------


from cipher import encode, decode, generate_pad

def test_encode(): 
    assert encode("AAA", "AAA") == "AAA"
    assert encode("AAA", "AAAA") == "AAA"
    assert encode("AaA", "AAA") == "AaA"
    assert encode("A! A, A4", "AAAAAAAA") == "A! A, A4"
    assert encode("AAA", "BBB") == "BBB"


def test_decode():
    assert decode("BBB", "AAA") == "BBB"
    assert decode("BBB", "AAAA") == "BBB"
    assert decode("BbB", "AAA") == "BbB"
    assert decode("B! B, B4", "AAAAAAAA") == "B! B, B4"
    assert decode("BBB", "BBB") == "AAA"

def test_generate_pad():
    assert len(generate_pad(1)) == 1

    pad1 = generate_pad(1028)
    pad2 = generate_pad(1028)
    pad3 = generate_pad(1028)

    assert pad1 != pad2 and pad2 != pad3 and pad1 != pad3
    