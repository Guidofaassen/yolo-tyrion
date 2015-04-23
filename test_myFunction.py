from myFunction import add_one

def test_answer():
    assert add_one(3) == 4

def test_answer2():
    assert add_one(4) == 5

def test_answer3():
    assert add_one(-2) == -1