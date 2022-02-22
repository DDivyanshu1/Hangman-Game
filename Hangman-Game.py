
import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list


print(logo)



chosen_word = random.sample(word_list, 1)
lives =6
q = []


chosen_word= ''.join(chosen_word)
n = len(chosen_word)
print(chosen_word)


for i in range(n):
    q.append("_")
print(q)


end = False

while not end:

    if "_" in q:

#input the guessed letter
        guess = input("\nGuess a letter -->  ").lower()


# if guessed letter is in the word
        for l in range(n):
            if guess==chosen_word[l]:
                    if q[l]=="_":
                        q[l]=guess
                        break
            else: continue
# print the puzzle with correctly guessed words 
        print(q)


# if the guessed letter is worng reducing 1 life and printing the hangman ascii art
        if guess not in chosen_word:
            if lives>0:
                print('The guessed letter is not in the word, hence you lose a life.')
                print(stages[lives])
                lives-=1
                print(f'You have {lives} lives left!!!\n')
            else:
                end = True
                print(stages[0])
                print('you lose')
        else:continue



    else:
        end = True
        print('\nYou Won!!')