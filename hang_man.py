import random
import sketch

def play_game():
    stages = sketch.stages
    word_list = ["apple", "banana", "grape", "mango", "orange","colombo","coconut","pineapple"]
    random_word = random.choice(word_list)
    attempts = 0

    print("Welcome to the WORD GUESSING GAME!\n")
    print("I HAVE A WORD IN MY MIND !!!..CAN YOU GUESS IT..???\n")
    print("THE SECRET WORD -","_ " * len(random_word))
    print(f"YOU WILL GET {attempts} ATTEMPTS to guess this secret word\n")

    guess_list = ['_' for i in range(len(random_word))]
    guessed_letters = set()
    while True:

        guess_letter = input("Guess a letter: ").lower().strip()

        if guess_letter in guessed_letters:
            print("⚠️ You guessed this letter already!\n")
            continue


        if len(guess_letter) == 1 or  guess_letter.isalpha():
            guessed_letters.add(guess_letter)
            if guess_letter in random_word:
                print(f"✅ You guessed it right..you unlocked the secret letter {guess_letter}")
                for index,letter in enumerate(random_word):
                    if letter == guess_letter:
                        guess_list[index] = guess_letter
                word = " ".join(guess_list)
                print(f"THE SECRET WORD - {word}")
                print(f"{attempts} attempts left...")
                if "".join(guess_list) == random_word:
                    print(f"🎉 YOU WON !!! you guess the WORD {random_word} within {attempts} attempts...\n")
                    break
            else:
                attempts += 1
                print(f"OH SORRY !! YOUR GUESS WAS WRONG... ")
                if attempts <= 7:
                    print(stages[attempts - 1])
                else:
                    print("you lost... hang man is completed")


        else:
            print("⚠️ Sorry, one letter at a time")

while True:
    play_game()
    again = input("DO YOU WANT TO PLAY AGAIN? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing!")
        break