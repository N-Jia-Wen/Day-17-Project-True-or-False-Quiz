class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, guess, current_answer):
        if guess.lower() == current_answer.lower():
            self.score += 1
            print(f"You got it right! Current score: {self.score}/{self.question_number}.")
        else:
            print(f"Sorry, you're wrong. Current score: {self.score}/{self.question_number}.")
        print(f"The correct answer is {current_answer}.\n")

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        guess = input(f"Q{self.question_number}: {current_question} True or False? ")
        self.check_answer(guess, current_answer)

    def final_results(self):
        print("Congratulations! You've completed the quiz!")
        print(f"Your final score was {self.score}/{self.question_number}.")
