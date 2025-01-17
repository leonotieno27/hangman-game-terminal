"""
Hang man game by leonq

"""

import random
import time
import os

#word in the library
words = [
    "kite", "apple", "banana", "grape", "orange", "mango", "cherry", "pear", "peach", "plum",
    "lemon", "lime", "strawberry", "blueberry", "raspberry", "watermelon", "cantaloupe", "melon",
    "kiwi", "fig", "date", "papaya", "guava", "pineapple", "avocado", "coconut", "lychee", "pomegranate",
    "carrot", "potato", "tomato", "cucumber", "zucchini", "lettuce", "spinach", "broccoli", "cauliflower",
    "cabbage", "asparagus", "celery", "pepper", "onion", "garlic", "radish", "beet", "mushroom", "turnip",
    "ginger", "parsnip", "kale", "arugula", "corn", "peas", "beans", "lentils", "rice", "wheat",
    "barley", "oats", "quinoa", "buckwheat", "millet", "rye", "spelt", "sorghum", "amaranth", "chia",
    "flax", "sunflower", "sesame", "almond", "walnut", "pecan", "hazelnut", "pistachio", "cashew", "macadamia",
    "brazilnut", "acorn", "chestnut", "filbert", "hickory", "pine", "nutmeg", "clove", "cinnamon", "vanilla",
    "mint", "basil", "oregano", "thyme", "rosemary", "sage", "parsley", "cilantro", "dill", "chive",
    "lavender", "saffron", "cumin", "paprika", "tarragon", "marjoram", "lemongrass", "turmeric", "cardamom", "gingerbread",
    "bread", "butter", "milk", "cheese", "yogurt", "cream", "egg", "meat", "chicken", "beef",
    "pork", "lamb", "fish", "shrimp", "crab", "lobster", "clam", "oyster", "scallop", "squid",
    "octopus", "caviar", "salmon", "trout", "herring", "mackerel", "sardine", "anchovy", "tuna", "bass",
    "cod", "halibut", "flounder", "sole", "tilapia", "catfish", "eel", "hake", "snapper", "marlin"
]

#clear screen
os.system('clear')

counter = 0
i = 0

print("\t\t\t***HANG-MAN GAME ***\n")

random_number = random.randint(1, 147)
guessed_word = words[random_number]

print("I'm thinking of a word:")
time.sleep(1)
print("Can you guess the letters of the word.")

while i < len(guessed_word):
    letter = input(f"Guess letter {i + 1}: ")
    if guessed_word[i] == letter:
        print("Correct.")
        i += 1 
    else:
        counter += 1
        print(f"Strike: {counter}")
        #images of the hang man after loss
        if counter == 1:
            print("""
                    +---+
                    |   |
                    O   |
                        |
                        |
                        |
                =========
                    """)
        elif counter == 2:
            print(
                """
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                =========
                """
            )
        elif counter == 3:
            print(
                """
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
            =========
                """
            )
        elif counter == 4:
            print(
                """
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
            =========

                """
            )
        else:
            print(
                """
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
            =========
                """
            )
    #at strike 5 loose the game
    if counter == 5:
        print(f"You loose. The word is {guessed_word}")
        break
#if loop ends and counter is less than three
if counter < 3:
    print(f"You win: Good guess for {guessed_word}")
    





