from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for x in range(0, (len(question_data))):
    question_details = Question(question_data[x]["question"], question_data[x]["correct_answer"])
    question_bank.append(question_details)

quiz = QuizBrain(question_bank)

while quiz.still():
    quiz.next_question()
    quiz.check_answer()
    print("\n")
print("You've completed the quiz!")
print(f"Final Score: {quiz.score}/{len(quiz.question_list)}")







