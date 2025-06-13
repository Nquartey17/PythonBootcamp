from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

question = QuizBrain(question_bank)
while question.still_has_questions():
    question.next_question()

print(f"Your final score: {question.score}/{question.question_number}")
