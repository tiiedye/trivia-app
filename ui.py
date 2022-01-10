from tkinter import *

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 14, "normal")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(text="Score: 0", font=SCORE_FONT, fg="white", bg=THEME_COLOR)
        self.score_lbl.grid(column=1, row=0)

        self.canvas = Canvas(width=400, height=350, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(200, 175, text="Question text here", fill=THEME_COLOR, font=QUESTION_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(50, 50))

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0)
        self.true_btn.grid(column=0, row=2)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0)
        self.false_btn.grid(column=1, row=2)
        # All UI-code before main loop
        self.window.mainloop()
