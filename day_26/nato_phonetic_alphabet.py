import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index,row) in data_frame.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ")
    try:
        nato_phonetic = [data_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only english letters accepted.")
        generate_phonetic()
    else:
        print(nato_phonetic)

generate_phonetic()