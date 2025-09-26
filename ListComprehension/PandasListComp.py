student_dict= {"student": ["Angela", "James", "lily"],
               "score": [56,76,98]}

#Loop through dictionary
for (key, value) in student_dict.items():
    print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print()

#Loop through rows of data frame using iterrows
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
