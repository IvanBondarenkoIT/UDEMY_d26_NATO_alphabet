import pandas
# TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row[0]: row[1] for (index, row) in df.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_word = input("Enter word - ").upper()
    try:
        print([alphabet.get(i) for i in user_word])
    except IndexError: 
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    

generate_phonetic()
