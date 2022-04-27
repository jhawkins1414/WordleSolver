# Wordle Solver
# Jared Hawkins
# 4/27/2022

feedback = ""
guess = ""
guesses_left = []

try:
    with open('FiveLetterWords.txt') as FiveLetterWords:
        for line in FiveLetterWords:
            guesses_left.append(line.strip())
except FileNotFoundError:
    print("Error: File Not Found")

print("Enter a starting word and hit enter")

# 6 guesses
for guesses in range(6):

    # enter a guess
    guess = input('Guess: ').lower()

    # enter Wordle feedback
    print('Enter feedback - g for green, y for yellow, and w for white in the format wwwww')
    feedback = input("Feedback: ").lower()

    # if word is correct, finish
    if feedback == 'ggggg':
        print('Guesses: ', guesses + 1)
        quit()

    # go through word and remove words that do not fit schema
    temp = tuple(guesses_left)
    for word in temp:
        for i in range(5):
            if feedback[i] == 'w' and guess[i] in word:
                guesses_left.remove(word)
                break
            elif feedback[i] == 'g' and guess[i] != word[i]:
                guesses_left.remove(word)
                break
            elif feedback[i] == 'y' and guess[i] not in word:
                guesses_left.remove(word)
                break
            elif feedback[i] == 'y' and guess[i] == word[i]:
                guesses_left.remove(word)
                break

    # print words left in guess list
    for word in guesses_left:
        print(word)
        print(' ')

print('Sorry you ran out of guesses')
