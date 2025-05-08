import random

# Asma aşamaları
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Kelime havuzu
WORDS = ["python", "elma", "araba", "kalem", "kitap", "bilgisayar", "programlama", "istanbul"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print("\nHatalı harfler:", " ".join(missed_letters))
    
    display_word = ""
    for letter in secret_word:
        if letter in correct_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Kelime:", display_word)

def get_guess(already_guessed):
    while True:
        guess = input("Bir harf tahmin et: ").lower()
        if len(guess) != 1:
            print("Lütfen tek harf gir.")
        elif not guess.isalpha():
            print("Lütfen sadece harf gir.")
        elif guess in already_guessed:
            print("Bu harfi zaten denedin.")
        else:
            return guess

def play_again():
    return input("Tekrar oynamak ister misin? (e/h): ").lower().startswith("e")

def main():
    print("Adam Asmaca Oyununa Hoş Geldin!")
    missed_letters = []
    correct_letters = []
    secret_word = get_random_word()
    game_over = False

    while True:
        display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters.append(guess)

            found_all = True
            for letter in secret_word:
                if letter not in correct_letters:
                    found_all = False
                    break
            if found_all:
                print(f"Tebrikler! Kelimeyi bildin: {secret_word}")
                game_over = True
        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print("Tahmin hakkın bitti!")
                print(f"Kelime: {secret_word}")
                game_over = True

        if game_over:
            if play_again():
                missed_letters = []
                correct_letters = []
                secret_word = get_random_word()
                game_over = False
            else:
                break

if __name__ == "__main__":
    main()
