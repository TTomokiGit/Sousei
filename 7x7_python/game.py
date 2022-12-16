from tkinter import *
from functools import partial
from cyclist import Cyclist
from menu import MenuWindow
from space import SpaceStatus
from point import PointStatus

class GameFrame(Frame):

    def __init__(self, master = None):
        super().__init__(master)

        #sub instance
        self.menu = None
        self.space = SpaceStatus()

        self.point = {"A": None,
                      "B": None,
                      "C": None,
                      "D": None}
        self.point["A"] = PointStatus()
        self.point["B"] = PointStatus()
        self.point["C"] = PointStatus()
        self.point["D"] = PointStatus()
        
        #status
        self.turn = 0
        self.star = 0
        self.is_starred = { "A": 0,
                            "B": 0,
                            "C": 0,
                            "D": 0}
        self.players = Cyclist(["A", "B", "C", "D"])
        self.current_player = self.players.present()

        #frame
        self.frame_sub = Frame(self.master, bg = "#ffffff", height = 900, width = 200)
        self.frame_point = Frame(self.master, bg = "#ffffff", height = 900, width = 500)
        self.frame_mass = Frame(self.master, bg = "#ffffff", height = 900, width = 900)
        self.frame_result = Frame(self.master, bg = "#ffffff", height = 900, width = 1600)

        self.frame_sub.place(x=1400, y=0)
        self.frame_point.place(x=900, y=0)
        self.frame_mass.place(x=0, y=0)
        self.frame_result.place(x=0, y=0)

        self.create_sub_widgets()
        self.create_game_widgets()


    def create_sub_widgets(self):
        self.frame_sub.tkraise()

        self.canvas = Canvas(
            self.frame_sub,
            bg = "#ffffff",
            height = 900,
            width = 200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x=0, y=0)

        self.img_menu = PhotoImage(file = f"7x7_python/imgs/frame_game/menu.png")
        self.button_menu = Button(
            self.canvas,
            image = self.img_menu,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.create_menu,
            relief = "flat")
        self.button_menu.place(x = 0, y = 0)

        self.img_result = PhotoImage(file = f"7x7_python/imgs/frame_game/restart.png")
        self.button_restart = Button(
            self.canvas,
            image = self.img_result,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.create_result,
            relief = "flat")
        self.button_restart.place(x = 0, y = 700)


    def create_game_widgets(self):
        self.frame_mass.tkraise()
        self.frame_point.tkraise()
        
        print(self.current_player)

        self.canvas_point = Canvas(
            self.frame_point,
            bg = "#ffffff",
            height = 900,
            width = 500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas_point.place(x=0, y=0)

        self.canvas_point.create_text(
            100, 20,
            text = f"turn={self.turn + 1}",
            fill = "#000000",
            font = ("None", int(30.0)))

        self.canvas_point.create_text(
            100, 60,
            text = f"player={self.current_player}",
            fill = "#000000",
            font = ("None", int(30.0)))

        self.canvas_point.create_text(
            200, 181.5,
            text = "A\n学力:{0}  電力:{1}  資源:{2}\nIT:{3}  工場:{4}\n加工:{5}  貿易:{6}".format(
                self.point["A"].points["Study"],
                self.point["A"].points["Power"],
                self.point["A"].points["Resources"],
                self.point["A"].points["IT"],
                self.point["A"].points["Factory"],
                self.point["A"].points["Processing"],
                self.point["A"].points["Trading"]),
            fill = "#000000",
            font = ("None", int(30.0)))

        self.canvas_point.create_text(
            200, 368.5,
            text = "B\n学力:{0}  電力:{1}  資源:{2}\nIT:{3}  工場:{4}\n加工:{5}  貿易:{6}".format(
                self.point["B"].points["Study"],
                self.point["B"].points["Power"],
                self.point["B"].points["Resources"],
                self.point["B"].points["IT"],
                self.point["B"].points["Factory"],
                self.point["B"].points["Processing"],
                self.point["B"].points["Trading"]),
            fill = "#000000",
            font = ("None", int(30.0)))

        self.canvas_point.create_text(
            200, 555.5,
            text = "C\n学力:{0}  電力:{1}  資源:{2}\nIT:{3}  工場:{4}\n加工:{5}  貿易:{6}".format(
                self.point["C"].points["Study"],
                self.point["C"].points["Power"],
                self.point["C"].points["Resources"],
                self.point["C"].points["IT"],
                self.point["C"].points["Factory"],
                self.point["C"].points["Processing"],
                self.point["C"].points["Trading"]),
            fill = "#000000",
            font = ("None", int(30.0)))

        self.canvas_point.create_text(
            200, 735.5,
            text = "D\n学力:{0}  電力:{1}  資源:{2}\nIT:{3}  工場:{4}\n加工:{5}  貿易:{6}".format(
                self.point["D"].points["Study"],
                self.point["D"].points["Power"],
                self.point["D"].points["Resources"],
                self.point["D"].points["IT"],
                self.point["D"].points["Factory"],
                self.point["D"].points["Processing"],
                self.point["D"].points["Trading"]),
            fill = "#000000",
            font = ("None", int(30.0)))


        self.massCanvas = Canvas(
            self.frame_mass,
            bg = "#ffffff",
            height = 900,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.massCanvas.place(x=40, y=40)

        self.pixel = PhotoImage(width=100, height=100)

        self.STRING_ARRAY = [["A","電力","加工","2","IT","学力","B"],
                             ["学力","資源","貿易","4","工場","資源","電力"],
                             ["IT","工場","5","1","5","貿易","加工"],
                             ["7","6","3","★","3","6","7"],
                             ["加工","貿易","5","1","5","工場","IT"],
                             ["電力","資源","工場","4","貿易","資源","学力"],
                             ["D","学力","IT","2","加工","電力","C"]]

        self.COLOR_TABLE = {"A": "#ffadad",
                            "B": "#adadff",
                            "C": "#adffad",
                            "D": "#ffffad",
                            "N": "#ffffff"}

        self.space_color = [[s.translate(str.maketrans(self.COLOR_TABLE)) for s in _] for _ in self.space.spaces]

        for i in range(7):
            for j in range(7):
                self.button_mass = Button(
                    self.massCanvas,
                    text = self.STRING_ARRAY[i][j],
                    font=("MSゴシック", "20", "bold"),
                    image = self.pixel,
                    bg = self.space_color[i][j],
                    command = partial(self.on_click, self.current_player, i, j),
                    compound="c",
                    relief = "sunken")
                self.button_mass.grid(row=i, column=j)   
        

    def create_result(self):
        self.frame_sub.destroy()
        self.frame_point.destroy()
        self.frame_mass.destroy()
      
        self.frame_result.tkraise()

        #create canvas
        self.canvas = Canvas(
            self.frame_result,
            bg = "#ffffff",
            height = 900,
            width = 1600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        #text
        self.canvas.create_text(
            800.0, 176.0,
            text = "結果発表",
            fill = "#000000",
            font = ("None", int(180.0)))

        #button
        self.img_end = PhotoImage(file = f"7x7_python/imgs/frame_game/end.png")
        self.button_end = Button(
            self.canvas,
            image = self.img_end,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.exit,
            relief = "flat")
        self.button_end.place(x = 1400, y = 694)

        self.img_restart = PhotoImage(file = f"7x7_python/imgs/frame_game/restart.png")
        self.button_restart = Button(
            self.canvas,
            image = self.img_restart,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.exit_frame,
            relief = "flat")
        self.button_restart.place(x = 1160, y = 700)


    #function
    def exit_frame(self):
        self.frame_sub.destroy()
        self.frame_point.destroy()
        self.frame_mass.destroy()
        self.frame_result.destroy()

    def exit(self):
        self.master.destroy()
        
    def next_turn(self):
        self.turn += 1
        self.current_player = self.players.next()
        self.massCanvas.destroy()
        self.canvas_point.destroy()
        self.create_game_widgets()

    def on_click(self, player, n, m):
        print(n, m)

        self.space_was_able = bool(self.space.judge(player, n, m))
        self.point_was_able = bool(self.point[player].judge(player, self.space.spaces[n][m], n, m))
        
        if self.star:
            if n==3 and m==3 or (n==0 or n==1 or n==5 or n==6) and (m==0 or m==1 or m==5 or m==6):
                pass
            else:
                self.point[player].turn_update()
                self.space.update(player, n, m)
                self.star = 0
                self.next_turn()
        else:
            if (n==3 and m==3) and self.space_was_able and not self.is_starred[player]:
                if self.space.rand_star():
                    self.star = 1
                    self.is_starred[player] = 1

                else:
                    self.next_turn()

            elif self.space_was_able and self.point_was_able:
                    self.point[player].update(player, self.space.spaces[n][m])
                    self.point[player].turn_update()
                    self.space.update(player, n, m)
                    self.next_turn()
            else:
                pass

    #callback
    def create_menu(self):
        if self.menu == None or not self.menu.winfo_exists():
            self.menu = Toplevel(self.master)
            self.app = MenuWindow(self.menu)


    def __del__(self):
        del self.space
        del self.point["A"]
        del self.point["B"]
        del self.point["C"]
        del self.point["D"]
        print("Previous game destroyed")
