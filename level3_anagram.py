from pathlib import Path

WORD_FILE = Path(__file__).parent / "words.txt"


def clean(text):
    return "".join(character for character in text.lower() if character.isalpha())


def sort_letters(text):
    return "".join(sorted(clean(text)))


def count_letters(text):
    counts = {}
    for letter in clean(text):
        counts[letter] = counts.get(letter, 0) + 1
    return counts


def load_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Could not find the word list: {file_path}")
        print("Create a text file with one word per line and try again.")
        return None
    except OSError as error:
        print(f"Could not read the word list: {error}")
        return None

    words = []
    seen = set()
    for line in lines:
        word = clean(line)
        if word and word not in seen:
            seen.add(word)
            words.append(word)

    if not words:
        print(f"The word list is empty: {file_path}")
        print("Add some words (one per line) and try again.")
        return None

    return words



def group_into_families(words):
    families = {}
    for word in words:
        key = sort_letters(word)
        if key not in families:
            families[key] = []
        families[key].append(word)
    return families


def find_anagrams(word, words):
    target = sort_letters(word)
    return [
        candidate for candidate in words
        if sort_letters(candidate) == target and candidate != clean(word)
    ]


def can_build(word, available):
    needed = count_letters(word)
    for letter, amount in needed.items():
        if available.get(letter, 0) < amount:
            return False
    return True



def ask_for_text(prompt):
    while True:
        text = input(prompt)
        if clean(text):
            return text
        print("  Please enter at least one letter.")



def check_two_words():
    first = ask_for_text("First word or phrase: ")
    second = ask_for_text("Second word or phrase: ")

    if clean(first) == clean(second):
        print("\nThese use the same letters in the same order, so they are not anagrams.")
    elif sort_letters(first) == sort_letters(second):
        print(f'\n"{first}" and "{second}" are anagrams.')
        print(f"Sorted letters: {sort_letters(first)}")
    else:
        print(f'\n"{first}" and "{second}" are NOT anagrams.')
        counts_first = count_letters(first)
        counts_second = count_letters(second)
        for letter in sorted(set(counts_first) | set(counts_second)):
            difference = counts_first.get(letter, 0) - counts_second.get(letter, 0)
            if difference > 0:
                print(f"  Extra in the first:  {letter} x{difference}")
            elif difference < 0:
                print(f"  Extra in the second: {letter} x{-difference}")


def show_anagrams_of_word(words):
    word = ask_for_text("Word to find anagrams of: ")
    matches = find_anagrams(word, words)

    if matches:
        print(f'\nFound {len(matches)} anagram(s) of "{word}":')
        for match in matches:
            print(f"  {match}")
    else:
        print(f'\nFound 0 anagrams of "{word}" in the word list.')


def show_largest_family(words):
    families = group_into_families(words)

    largest_key = max(families, key=lambda key: len(families[key]))
    largest = families[largest_key]

    if len(largest) < 2:
        print("\nNo anagram families found - every word is unique.")
        return

    print(f"\nLargest anagram family ({len(largest)} words, letters: {largest_key}):")
    print("  " + ", ".join(largest))


def build_words_from_letters(words):
    letters = ask_for_text("Enter your letters: ")
    available = count_letters(letters)

    buildable = [word for word in words if can_build(word, available)]
    buildable.sort(key=lambda word: (-len(word), word))

    if buildable:
        print(f"\nYou can build {len(buildable)} word(s) from \"{clean(letters)}\":")
        print("  " + ", ".join(buildable))
    else:
        print("\nNo words in the list can be built from those letters.")


def main():
    print("=== Anagram Finder ===")

    words = load_words(WORD_FILE)
    if words is None:
        return

    print(f"Loaded {len(words)} words.")

    while True:
        print("\n1. Check two words")
        print("2. Find all anagrams of a word")
        print("3. Show the largest anagram family")
        print("4. Build words from these letters")
        print("5. Quit")
        choice = input("Choose 1-5: ").strip()

        if choice == "1":
            check_two_words()
        elif choice == "2":
            show_anagrams_of_word(words)
        elif choice == "3":
            show_largest_family(words)
        elif choice == "4":
            build_words_from_letters(words)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("  Please choose a number from 1 to 5.")


main()