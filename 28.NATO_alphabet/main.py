import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("28.NATO_alphabet/nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ").upper()
phonetic_list = [data_dict[letter] for letter in name]
print(phonetic_list)