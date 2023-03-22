#tests um.py
from um import count

def main():
    test_um()
    test_case()
    test_space()

#tests that only the word "um" is counted
def test_um():
    assert count("um") ==(1)
    assert count("uh") ==(0)
    assert count("ummm") ==(0)
    assert count("")==(0)
    assert count("Um, no") ==(1)

#tests that only "um" (case insensitive) is being counted
def test_case():
    assert count("UM, I THINK SO!") ==(1)
    assert count("uM, Um, um") ==(3)
    assert count("Ummmmm, no.") ==(0)

#tests that whitespace does not interfer with counting "um"
def test_space():
    assert count("I, um, don't think so") ==(1)
    assert count("           um, um, um") ==(3)
    assert count("um, um, um") ==(3)

if __name__ == "__main__":
    main()

