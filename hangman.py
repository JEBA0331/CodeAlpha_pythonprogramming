import random

words = ["python", "intern", "coding", "project", "developer"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("❌ Game Over! The word was:", word)
