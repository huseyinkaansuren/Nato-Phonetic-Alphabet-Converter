import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_frame = pandas.DataFrame(data)
nato_dict = {row.letter:row.code for (index,row) in data_frame.iterrows()}


user_input = input("Enter a word: ").upper()

nato_phonetic_code = [nato_dict[letter] for letter in user_input]

print(nato_phonetic_code)
