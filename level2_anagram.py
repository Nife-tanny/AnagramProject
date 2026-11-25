
WORD_LIST = [
    "listen", "silent", "enlist", "tinsel", "inlets",
    "stone", "notes", "onset", "tones", "stop", "pots", "tops", "post", "spot",
    "evil", "vile", "live", "veil", "race", "care", "acre",
    "heart", "earth", "hater", "night", "thing", "dusty", "study",
]



def clean(text):
    return "".join(character for character in text.lower() if character.isalpha())


def sort_letters(text):
    return "".join(sorted(clean(text)))


def count_letters(text):
    counts = {}
    for letter in clean(text):
        counts[letter] = counts.get(letter, 0) + 1
    return counts


def find_differences(first, second):
    counts_first = count_letters(first)
    counts_second = count_letters(second)

    extra_in_first = {}
    extra_in_second = {}

    all_letters = set(counts_first) | set(counts_second)
    for letter in sorted(all_letters):
        difference = counts_first.get(letter, 0) - counts_second.get(letter, 0)
        if difference > 0:
            extra_in_first[letter] = difference
        elif difference < 0:
            extra_in_second[letter] = -difference

    return extra_in_first, extra_in_second


def format_counts(counts):
    return ", ".join(f"{letter} x{number}" for letter, number in counts.items())


def ask_for_text(prompt):
    while True:
        text = input(prompt)
        if clean(text):
            return text
        print("  Please enter at least one letter.")


def ask_yes_no(prompt):
    return input(prompt).strip().lower() == "y"


def check_two_words():
    first = ask_for_text("First word or phrase: ")
    second = ask_for_text("Second word or phrase: ")

    if clean(first) == clean(second):
        print(f'\n"{first}" and "{second}" use the same letters in the same order, '
              "so they are not anagrams.")
        return

    if sort_letters(first) == sort_letters(second):
        print(f'\n"{first}" and "{second}" are anagrams.')
        print(f"Sorted letters: {sort_letters(first)}")
        return

    print(f'\n"{first}" and "{second}" are NOT anagrams.')
    extra_in_first, extra_in_second = find_differences(first, second)

    if extra_in_first:
        print(f"  Extra in the first:  {format_counts(extra_in_first)}")
    if extra_in_second:
        print(f"  Extra in the second: {format_counts(extra_in_second)}")


def find_in_builtin_list():
    word = ask_for_text("Word to find anagrams of: ")
    target = sort_letters(word)

    matches = []
    for candidate in WORD_LIST:
        if sort_letters(candidate) == target and clean(candidate) != clean(word):
            matches.append(candidate)

    if matches:
        print(f"\nFound {len(matches)} anagram(s) of \"{word}\": {', '.join(matches)}")
    else:
        print(f'\nNo anagrams of "{word}" found in the built-in list.')



def main():
    print("=== Anagram Finder ===")

    while True:
        print("\n1. Check two words")
        print("2. Find anagrams of a word in the built-in list")
        print("3. Quit")
        choice = input("Choose 1, 2 or 3: ").strip()

        if choice == "1":
            check_two_words()
        elif choice == "2":
            find_in_builtin_list()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("  Please choose 1, 2 or 3.")


main()