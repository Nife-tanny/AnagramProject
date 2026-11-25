def clean(text):
    return text.lower().replace(" ", "")


def sort_letters(text):
    return "".join(sorted(clean(text)))


def check_pair(first, second):
    if clean(first) == clean(second):
        print(f'"{first}" and "{second}" are the same word, so they are not anagrams.')
        return

    letters_first = sort_letters(first)
    letters_second = sort_letters(second)

    if letters_first == letters_second:
        print(f'"{first}" and "{second}" are anagrams.')
    else:
        print(f'"{first}" and "{second}" are NOT anagrams.')
        print(f"Sorted letters of the first word:  {letters_first}")
        print(f"Sorted letters of the second word: {letters_second}")
        return

    print(f"Sorted letters: {letters_first}")


def main():
    print("=== Anagram Checker ===")

    while True:
        first = input("\nFirst word: ")
        second = input("Second word: ")

        check_pair(first, second)

        again = input("\nCheck another pair? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


main()