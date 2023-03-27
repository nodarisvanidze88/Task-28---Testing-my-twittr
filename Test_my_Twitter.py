from My_Twittr import shorten

vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def main():
   test_shorten()


def test_shorten():
    assert shorten("one two three", vowel)=="n tw thr"
    assert shorten("ABCNoDaRI", vowel)=="BCNDR"
    assert shorten("1234", vowel)=="1234"


if __name__ == "__main__":
    main()
