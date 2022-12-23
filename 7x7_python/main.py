from tkinter import *
from application import Application

#main
def main():
    window = Tk()
    Application(master=window).mainloop()

if __name__ == "__main__":
    main()