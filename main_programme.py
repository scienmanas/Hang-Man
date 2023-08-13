import random
from wordstochoose import word_list
from hangman_art import logo
from hangman_art import stages

run = False

def Find_index(check_letter, select_word):
    index = 0
    while(True):
        if(check_letter==select_word[index]):
            return index
        else:
            index+=1
            continue

select_word = random.choice(word_list)
display = []
for i in range(0,len(select_word)) :
    display+="-"

killed_variable = 0
print(logo)
while (killed_variable<7) :
    check_letter = input("Guess a letter🙂 : ")
    if check_letter in select_word:
        index = Find_index(check_letter,select_word)
        display[index] = check_letter
        print(f"{' '.join(display)}")
        if (killed_variable==0):
            continue
        else:
            print(stages[7-killed_variable])
    else:
        killed_variable+=1
        print(f"You guessed {check_letter}, that's not in the word. You lose a life")
        print(f"{' '.join(display)}")
        print(stages[7-killed_variable])
    if "-" in display:
        continue
    else:
        print("You won 🎉🎉🎊🎊")
        break

if(killed_variable==7):
    print("You Lost! 😏😏")