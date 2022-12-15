from tkinter import *
from application import Application

import os
print(os.getcwd())

#main
def main():
    window = Tk()
    app = Application(master=window)
    app.mainloop()

if __name__ == "__main__":
    main()