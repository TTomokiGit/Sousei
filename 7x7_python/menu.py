from tkinter import *


class MenuFrame(Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.geometry("500x600")
        self.master.title("7x7_alpha_menu")
        self.master.configure(bg = "#ffffff")
        self.master.resizable(False, False)

        self.frame = Frame(self.master, bg = "#ffffff", height = 600, width = 500)

        self.frame.place(x=0, y=0)

        self.create_widgets()
        
        
    def create_widgets(self):
        
        self.frame.tkraise()

        self.canvas = Canvas(
            self.frame,
            bg = "#ffffff",
            height = 600,
            width = 500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.img_close = PhotoImage(file = f"7x7_python/imgs/frame_menu/close.png")
        self.button_close = Button(
            self.canvas,
            image = self.img_close,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.exit,
            relief = "flat")
        self.button_close.place(x = 399, y = 0)

        self.img_desc = PhotoImage(file = f"7x7_python/imgs/frame_menu/desc.png")
        self.button_desc = Button(
            self.canvas,
            image = self.img_desc,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")
        self.button_desc.place(x = 118, y = 152)


    #function
    def btn_clicked(self):
        print("^~?")

    def exit(self):
        self.master.destroy()
    
    def __del__(self):
        print("Previous menu destroyed")
