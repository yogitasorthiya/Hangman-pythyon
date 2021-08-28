import string
from words import choose_word
from images import IMAGES


def ifvalid(input):
    if len(input)!=1:
        return False
    if not input.isalpha():
       return  False
    return True


def is_word_guessed(secret_word, letters_guessed):
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True

    return False
        
def get_guessed_word(secret_word, letters_guessed):
   

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    
    import string
    letters_left = string.ascii_lowercase
    letters_left=""
    for i in letters_guessed:
        if i not in letters_guessed:
            letters_left+=i
        return letters_left
    
def get_hint(secret_word,letters_guessed):
      import random
      letters_not_guessed=[]
      i=0
      while i<len(secret_word):
            if i not in letters_guessed:
                  if i not in letters_not_guessed:
                        letters_not_guessed.append(i)
            i+=1
      return random.choice(letters_not_guessed)

def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = []
    total_lives = remaining_lives = 8
    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]
    user_difficulty_choice = input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n")
    if user_difficulty_choice not in ["a", "b", "c"]:
        print ("Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai")
    else:
        if user_difficulty_choice == "b":
            total_lives = remaining_lives = 6
            images_selection_list_indices = [0, 2, 3, 5, 6, 7]

        elif user_difficulty_choice == "c":
            total_lives = remaining_lives = 4
            images_selection_list_indices = [1, 3, 5, 7]

    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: + available_letters")
        guess = input("Please guess a letter: ")
        letter = guess.lower()
        # if letter=="hint":
        #     print("hint for secret word"+get_hint(secret_word,letters_guessed))
        #     letter=get_hint(secret_word,letters_guessed)
        # else:
        #     if (not valid(letter)):
        #         print("in valid output")
        #         continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print (IMAGES[images_selection_list_indices[total_lives-remaining_lives]]) ## <-- CHANGES HERE
            remaining_lives-=1
            print("Remaining LIVE:"+str(remaining_lives))
            print("")
    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")
secret_word = choose_word()
hangman(secret_word)
