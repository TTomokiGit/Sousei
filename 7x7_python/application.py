from tkinter import *
from menu import MenuWindow
from game import GameFrame


class Application(Frame):
    def __init__(self, master = None):
        super().__init__(master)

        #sub instance
        self.menu = None
        self.game = None
       
        #define app
        self.master.geometry("1600x900")
        self.master.title("7x7_alpha")
        self.master.configure(bg = "#ffffff")
        self.master.resizable(False, False)

        self.frame_start = Frame(self.master, bg = "#ffffff", height = 900, width = 1600)
        self.frame_headcount = Frame(self.master, bg = "#ffffff", height = 900, width = 1600)

        self.frame_start.place(x=0, y=0)
        self.frame_headcount.place(x=0, y=0)

        #create intial widgets
        self.create_start_widgets()


    def create_start_widgets(self):

        self.frame_start.tkraise()

        #create canvas
        self.canvas = Canvas(
            self.frame_start,
            bg = "#ffffff",
            height = 900,
            width = 1600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x=0, y=0)

        #text
        self.canvas.create_text(
            799.5, 175.0,
            text = "7x7",
            fill = "#ffc700",
            font = ("None", int(250.0)))

        #button
        self.img_start = PhotoImage(file = f"7x7_python/imgs/frame_start/start.png")
        self.button_start = Button(
            self.canvas,
            image = self.img_start,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.create_headcount_widgets,
            relief = "flat")
        self.button_start.place(x = 484, y = 351)

        self.img_desc = PhotoImage(file = f"7x7_python/imgs/frame_start/desc.png")
        self.button_desc = Button(
            self.canvas,
            image = self.img_desc,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.create_menu,
            relief = "flat")
        self.button_desc.place(x = 484, y = 600)


    def create_headcount_widgets(self):

        self.frame_headcount.tkraise()

        #create canvas
        self.canvas = Canvas(
            self.frame_headcount,
            bg = "#ffffff",
            height = 900,
            width = 1600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        #text
        self.canvas.create_text(
            799.5, 330.0,
            text = "人数を選択",
            fill = "#000000",
            font = ("None", int(150.0)))

        #button
        self.img_4player = PhotoImage(file = f"7x7_python/imgs/frame_headcount/4player.png")
        self.button_4player = Button(
            self.canvas,
            image = self.img_4player,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.create_game,
            relief = "flat")
        self.button_4player.place(x = 1050, y = 533)


    #function    
    def exit(self):
        self.master.destroy()

    def create_menu(self):
        if self.menu == None or not self.menu.winfo_exists():
            self.menu = Toplevel(self.master)
            self.menu = MenuWindow(self.menu)
    
    def create_game(self):
        if not(self.game == None):
            self.game.destroy()
            del self.game

        self.game = GameFrame(self.master)