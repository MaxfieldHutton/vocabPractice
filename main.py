import os
import random
import json
import time


def getInt(_inputText):
    while True:
        user_input = input(f"{_inputText}")
        try:
            wordAmount = int(user_input)
            break
        except ValueError:
            print("Please enter a valid integer.")
    return wordAmount


def clearCLI():
    ##print("\033c")
    os.system('cls' if os.name == 'nt' else 'clear')


dataSelect = getInt("1: vocab data | 2: test data \n")

if dataSelect == "1":
    data = "WordLists/vocabDefinitions.json"
elif dataSelect == "2":
    data = "WordLists/testData.json"
else:
    print("invalid... defaulting to vocab")
    data = "WordLists/vocabDefinitions.json"

# Load JSON data from a file
with open(data, 'r') as file:
    loaded_data = json.load(file)


def get_value_from_json(word_list, key):
    # Access the value using the provided key
    value = word_list.get(key, None)
    return value


keys = list(loaded_data.keys())


def choose_word(remove):
    chosen_word = random.choice(keys)
    if remove:
        keys.remove(chosen_word)
    return chosen_word


def __main__():
    clearCLI()
    wordAmount = getInt("Choose how many random words to practice from 1-110 \n")
    if wordAmount >= 110:
        wordAmount = 110
    if wordAmount <= 1:
        wordAmount = 1

    clearCLI()
    roundNum = 0
    correctQuestions = 0

    for i in range(wordAmount):
        roundActive = True
        while roundActive:
            if correctQuestions > 0:
                accuracy = f"accuracy: {round((correctQuestions / roundNum) * 100)}%"
            else:
                accuracy = f" "

            word = choose_word(True)
            definition = get_value_from_json(loaded_data, word)
            clearCLI()
            print(f"round: {str(roundNum + 1)} {accuracy}")
            print(f"What word does this describe?")
            jsonDefinition = json.dumps(definition, indent=0)
            print(jsonDefinition)

            choices = []
            choices.append(word)
            for i in range(3):
                choices.append(choose_word(False))
            random.shuffle(choices)
            print(f"{choices}")

            getInput = str(input().capitalize())
            if getInput == word:
                print(f"Correct!")
                roundNum += 1
                correctQuestions += 1
                time.sleep(1)
                clearCLI()
                roundActive = False
            else:
                print(f"Incorrect :( the answer was " + str(word))
                roundNum += 1
                time.sleep(2)
                clearCLI()
                roundActive = False
    print(f"Game Over {accuracy}")


__main__()

print("press R to restart or any other key to exit")
if input().capitalize() == "R":
    __main__()
else:
    exit(0)
