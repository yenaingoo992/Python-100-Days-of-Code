import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index,row) in data_frame.iterrows()}

word = input("Enter a word: ")
nato_phonetic = [data_dict[letter.upper()] for letter in word]
print(nato_phonetic)