import random
import json
import time


def clearCLI():
    print("\033c")


dataSelect = input("1: vocab data | 2: test data")
if dataSelect == "1":
    data = "vocabDefinitions.json"
elif dataSelect == "2":
    data = "testData.json"
else:
    print("invalid... defaulting to vocab")
    data = "vocabDefinitions.json"

# Load JSON data from a file
with open(data, 'r') as file:
    loaded_data = json.load(file)


def get_value_from_json(word_list, key):
    # Access the value using the provided key
    value = word_list.get(key, None)
    return value


keys = list(loaded_data.keys())


def choose_word():

    chosen_word = random.choice(keys)
    keys.remove(chosen_word)
    return chosen_word


def __main__():
    clearCLI()
    print("Choose how many random words to practice")
    print("1-110")
    getWordAmount = int(input())
    clearCLI()
    roundNum = 0
    correctQuestions = 0

    for i in range(getWordAmount):
        roundActive = True
        while roundActive:
            if correctQuestions > 0:
                accuracy = f"accuracy: {round((correctQuestions / roundNum) * 100)}%"
            else:
                accuracy = f" "

            word = choose_word()
            definition = get_value_from_json(loaded_data, word)
            clearCLI()
            print(f"round: {str(roundNum + 1)} {accuracy}")
            print(f"What word does this describe?")
            print(json.dumps(definition, indent=0))

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
