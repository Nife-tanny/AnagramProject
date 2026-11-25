scores = {
    1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

def clean(text):
    return "".join(character for character in text.lower() if character.isalpha())

def count_letters(text):
    counts = {}
    for letter in clean(text):
        counts[letter] = counts.get(letter, 0) + 1
    return counts

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



def total_scores(text):
    total = 0

    text = text.upper()

    for score, letters in scores.items():
        for letter in text:
            if letter in letters:
                total += score

    return total

rack = []
track = 1

while len(rack) < 7:
    print("Enter 7 letters into your rack")

    tile = input(f"Enter your letter {track}: ")

    if tile.isalpha() == False:
        print("Invalid entry. Please enter a letter")
        continue

    rack.append(tile)
    track += 1




# minimum of 2 letters are required to build the words
