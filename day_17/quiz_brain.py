class QuizBrain:

    def __init__(self, question_number, question_list):
        self.question_number = question_number
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        return next_question

    def has_next(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, question, answer):
        is_correct = question.answer == answer
        if is_correct:
            self.score += 1
        return is_correct

    def get_score(self):
        return self.score

    def total_question(self):
        return len(self.question_list)