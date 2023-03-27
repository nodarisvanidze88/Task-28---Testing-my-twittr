def main():
    vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    user = input("Input: ").strip()
    print(shorten(user, vowel))


def shorten(word, v):
    for i in word:
        if i in v:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
