import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# dictionary comprehension
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

word = input("enter a word: ").upper()

# list comprehension
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
