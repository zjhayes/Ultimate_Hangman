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
        self.word_label = tkinter.Label(self.m, bg=self.bg_color, fg="black", text="")
        guess = tkinter.StringVar(self.m)
        self.available_choices = ['A', "B", "C"]
        self.guess.set('Guess:')
        self.guess_combobox = tkinter.OptionMenu(self.m, self.guess, *self.available_choices, command=self.on_guess_made)
        self.guess_combobox = tkinter.Combobox(self.m, width=10, textvariable=guess)
        self.guess_combobox.config(bg="navy", fg="black")
        hangman0 = PhotoImage(file="../images/hangman-0.gif")
        hangman1 = PhotoImage(file="../images/hangman-1.gif")
        hangman2 = PhotoImage(file="../images/hangman-2.gif")
        hangman3 = PhotoImage(file="../images/hangman-3.gif")
        hangman4 = PhotoImage(file="../images/hangman-4.gif")
        hangman5 = PhotoImage(file="../images/hangman-5.gif")
        hangman6 = PhotoImage(file="../images/hangman-6.gif")
        hangman7 = PhotoImage(file="../images/hangman-7.gif")
        hangman8 = PhotoImage(file="../images/hangman-8.gif")
        hangman9 = PhotoImage(file="../images/hangman-9.gif")
        hangman10 = PhotoImage(file="../images/hangman-10.gif")
        self.hangman_images = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8,
                               hangman9, hangman10]
        self.setup()
        self.put_ui_elements();
        self.run()

    def on_guess_made(self, event):
        '''When user makes a guess.'''
        self.available_choices.remove(event)
        self.update_option_menu()

    def update_option_menu(self):
        '''Update the guess OptionMenu values.'''
        menu = self.guess_combobox["menu"]
        menu.delete(0, "end")
        for option in self.available_choices:
            menu.add_command(label=option, command=self.command)

    def command(self):
        pass

    def setup(self):
        '''Set the UI configurations'''
        self.m.configure(bg=self.bg_color)
        self.m.title("Ultimate Hangman")
        self.m.minsize(400, 600)

    def put_ui_elements(self):
        '''Put UI elements on window grid.'''
        self.hangman_canvas.grid(row=0, column=0)
        self.hangman_canvas.create_image(0, 0, anchor=NW, image=self.hangman_images[0])
        self.title_label.grid(column=0, row=1)
        self.score.grid(column=0, row=2)
        self.word_label.grid(column=0, row=4)
        self.guess_combobox.grid(column = 0, row = 5)

    def set_new_word(self):
        self.word_label.config(text=self.game.get_word())

    def run(self):
        '''Runs the game'''
        self.set_new_word()
        self.m.mainloop()
