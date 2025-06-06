from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

question = QuizBrain(question_bank)
question.next_question()


