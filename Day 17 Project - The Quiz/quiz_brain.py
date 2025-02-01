class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.answer = None
        self.decision = None
        self.question_number = 0
        self.question_list = q_list

    def still(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        self.decision = (input(f"Q.{self.question_number}: {current.text} (True/False)?: ")).lower()
        self.answer = current.answer.lower()

    def check_answer(self):
        if self.decision == self.answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was {self.answer.upper()}")
        print(f"Your current score is: {self.score}/{self.question_number}")






