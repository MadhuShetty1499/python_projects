from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.text = self.canvas.create_text(150, 125, text="quiz.next_question()")
        self.canvas.itemconfig(self.text, fill = "black", font = ("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.right_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.true)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.false)
        self.wrong_button.grid(column=1, row=2)

        self.score_board = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "normal"))
        self.score_board.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"You have reached the end of the questions!")
            self.canvas.config(bg="Yellow")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.score_board.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white",
                                font=("Arial", 12, "normal"))


    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.score_board.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white",
                                font=("Arial", 12, "normal"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)