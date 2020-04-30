# Zachary Hayes
import tkinter
from tkinter import *


class UIController:
    '''UIController class controls the game interface.'''

    def __init__(self, game_controller):
        self.game = game_controller
        self.m = tkinter.Tk()

        # Define UI Elements
        self.bg_color = "#c3d7f7"
        self.title_label = tkinter.Label(self.m, bg=self.bg_color, fg="black", text="Ultimate Hangman")
        self.score = tkinter.Label(self.m, bg=self.bg_color, fg="black", text="0")
        self.hangman_canvas = Canvas(self.m, width=175, height=275, bg=self.bg_color, borderwidth=0, highlightthickness=0)
        self.hangman0 = PhotoImage(file="../images/hangman-0.gif")
        self.setup()
        self.put_ui_elements();
        self.run()

    def setup(self):
        '''Set the UI configurations'''
        self.m.configure(bg=self.bg_color)
        self.m.title("Ultimate Hangman")
        self.m.minsize(400, 600)

    def put_ui_elements(self):
        '''Put UI elements on window grid.'''
        self.title_label.grid(column=0, row=1)
        self.score.grid(column=0, row=2)
        self.hangman_canvas.grid(row=0, column=0)
        self.hangman_canvas.create_image(0,0, anchor=NW, image=self.hangman0)
        self.hangman_canvas.create_image(0,0, anchor=NW, image=self.hangman0)

    def run(self):
        '''Runs the game'''
        self.m.mainloop()
