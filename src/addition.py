# app.py
# This is a test commit
#just adding new line for testing
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
