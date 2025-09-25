import random
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

#dictionary comprehension: "dict name" = ["key:value" for "element" in "list"]
student_scores = {student: random.randint(1,100) for student in names}
print(student_scores)

#Conditional dictionary comprehension challenge
# "dict name" = ["key:value" for "(key:value)" in "dictionary.items() -> for all items in dictionary"]
passed_students= {student:score for (student, score) in student_scores.items() if score >= 60}