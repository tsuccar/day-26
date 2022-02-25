# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
import pandas as pd
nato_data = pd.read_csv ("nato_phonetic_alphabet.csv")

# new_dict = {nato_data.loc[index,'letter']:nato_data.loc[index,'code'] for (index,row) in nato_data.iterrows()}
new_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}

print (new_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word:").upper()
user_input_list = [char for char in user_input]

phonetic_list = [new_dict[char] for char in user_input_list ]
print(phonetic_list)


#TODO 3. condense the number of line from above.


user_input = input("Enter a word:").upper()
phonetic_list = [new_dict[char] for char in user_input ]
print(phonetic_list)