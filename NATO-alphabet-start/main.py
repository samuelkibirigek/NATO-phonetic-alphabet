student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word to apply the NATO alphabet on: ").upper()

new_list = [alphabet_dict[letter] for letter in word]

print(new_list)

new_dict = {word[pos]: new_list[pos] for pos in range(len(word))}

print(new_dict)



