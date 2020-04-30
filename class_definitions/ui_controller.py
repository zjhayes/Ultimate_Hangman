# Zachary Hayes
import tkinter
from tkinter import *


class UIController:
    '''UIController class controls the game interface.'''

    def __init__(self, game_controller):
        self.game = game_controller
        self.m = tkinter.Tk()
        self.setup()

        # Define UI Elements
        self.title_label = tkinter.Label(self.m, bg="blue", fg="black", text="")
        self.title_label.grid(column=0, row=0)
        self.score = tkinter.Label(self.m, bg="blue", fg="black", text="0")
        self.score.grid(column=0, row=1)
        self.run()

    def setup(self):
        '''Set the UI configurations'''
        self.m.configure(bg='blue')
        self.m.title("Ultimate Hangman")
        self.m.minsize(400, 600)

    def run(self):
        '''Runs the game'''
        self.m.mainloop()
