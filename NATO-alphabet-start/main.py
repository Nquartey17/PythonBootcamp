import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)

letter_df = {row.letter:row.code for (index, row) in df.iterrows()}
print(letter_df.items())

name = input("Enter a word: ").upper()
nato_name = [letter_df[letter] for letter in name if letter in letter_df.keys()]
print(nato_name)