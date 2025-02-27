from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
COLOR_ON_THEME = "#ffffff"
CANVAS_COLOR = "#ffffff"


class QuizzlerInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.completed = False
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text="Score: 0", background=THEME_COLOR, fg=COLOR_ON_THEME, font=('Arial', 12, 'normal'))
        self.score_text.grid(row=0, column=1, sticky='e')

        self.canvas = Canvas(width=300, height=250)
        self.canvas.configure(background=CANVAS_COLOR)

        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question Text Here",
                                                     font=('Arial', 16, 'italic'), fill=THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, pady=20, padx=20, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=0)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, pady=20, padx=20, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        if q_text == "":
            self.completed = True
            q_text = "Completed"
        self.canvas.itemconfigure(self.question_text, text=q_text)

    def answer_true(self):
        if not self.completed:
            is_correct = self.quiz.check_answer(user_answer="true")
            if is_correct:
                current_score = self.quiz.increase_score()
                self.update_score(current_score)
            self.give_feedback(is_correct)

    def answer_false(self):
        if not self.completed:
            is_correct = self.quiz.check_answer(user_answer="false")
            if is_correct:
                current_score = self.quiz.increase_score()
                self.update_score(current_score)
            self.give_feedback(is_correct)

    def update_score(self, score: int):
        self.score_text.configure(text=f"Score: {score}")

    def give_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.next_question)
