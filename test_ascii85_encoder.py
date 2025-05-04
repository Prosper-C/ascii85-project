import pytest
from ascii85_encoder import ascii85_encode

def test_ascii85_simple():
    assert ascii85_encode(b'Hello') == '87cURDZ'

def test_ascii85_empty():
    assert ascii85_encode(b'') == ''

def test_ascii85_zero_block():
    assert ascii85_encode(b'\x00\x00\x00\x00') == 'z'

def test_ascii85_padding():
    assert ascii85_encode(b'abc') == '@:E^'  # Update padding result here

def test_ascii85_multiple_blocks():
    assert ascii85_encode(b'Hello world') == '87cURD]j7BEbo7'  # Update multi-block result
