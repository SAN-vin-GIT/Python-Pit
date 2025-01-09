from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Poppins"



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzical")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.a_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=(FONT_NAME, 16))
        self.a_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="negus : the supreme ruler",
            fill=THEME_COLOR,
            font=(FONT_NAME, 20, "italic"),
            width=260  # Ensures text wraps properly
        )
        self.canvas.grid(padx=20, pady=20, row=1, column=0, columnspan=2)

        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_image, bd=0, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(padx=20, pady=20, row=2, column=0)

        self.wrong_button = Button(image=wrong_image, bd=0, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(padx=20, pady=20, row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.a_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Yayy! You finished the Quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)