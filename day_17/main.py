from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_number = 0
question_bank = []
random.shuffle(question_data)
for question in question_data:
    question_bank.append(Question(
        question['question'], question['correct_answer']
    ))

quiz_brain = QuizBrain(question_number, question_bank)

while quiz_brain.has_next():
    question = quiz_brain.next_question()
    answer = input(f"Q.{quiz_brain.question_number}: {question.text} (True/False): ")
    is_correct = quiz_brain.check_answer(question, answer)
    if is_correct:
        print("You are right!")
    else:
        print(f"The correct was {question.answer}")
    print(f"Your current score: {quiz_brain.get_score()}/{quiz_brain.total_question()}")
    print()

print("You've completed the quiz")
print(f"Your score: {quiz_brain.get_score()}/{quiz_brain.total_question()}")