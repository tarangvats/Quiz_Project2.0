THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx =20, pady=20, bg = THEME_COLOR)


        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=('Arial', 20, 'italic'))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125,width=200, text = "Some Question" , fill=THEME_COLOR, font = ("Arial",20,'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)



        tick = PhotoImage(file="images/true.png")
        cross = PhotoImage(file="images/false.png")

        self.right = Button(image = tick,highlightthickness=0,command = self.true)
        self.right.grid(row=2,column=0)

        self.wrong = Button(image=cross,highlightthickness=0,command = self.false)
        self.wrong.grid(row=2,column=1)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.question_number<10:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text = q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question,text="Quiz Completed")
            self.canvas.config(bg="grey")
            self.right.destroy()
            self.wrong.destroy()


    def true(self):
        check = self.quiz.check_answer("True")

        self.score_label.config(text=f"Score: {self.quiz.score}")

        if check is True:
            self.canvas.config(bg="green")


        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
        return check

    def false(self):
        check = self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if check is True:
            self.canvas.config(bg="green")


        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
        return check









