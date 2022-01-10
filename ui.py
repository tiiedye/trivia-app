from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CORRECT_COLOR = "#7aff8e"
INCORRECT_COLOR = "#cc454e"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 14, "normal")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(text=f"Score: {self.score}", font=SCORE_FONT, fg="white", bg=THEME_COLOR)
        self.score_lbl.grid(column=1, row=0)

        self.canvas = Canvas(width=400, height=350, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(200, 175, text="Question text here", fill=THEME_COLOR,
                                                     font=QUESTION_FONT, width=380)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(50, 50))

        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.submit_true)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.submit_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def submit_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def submit_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg=CORRECT_COLOR)
            self.score += 1
            self.score_lbl.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg=INCORRECT_COLOR)
        self.window.after(1000, self.get_next_q)
