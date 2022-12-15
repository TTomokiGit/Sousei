class pointstatus:
    def __init__(self) -> None:
        # variable
        self.points = { "Study": 1,
                        "Power": 1,
                        "Resources": 1,
                        "IT": 0,
                        "Factory": 0,
                        "Processing": 0,
                        "Trading": 0}


        # constant
        self.DEST_ARRAY = [  [None,None,"Processing","2","IT",None,None],
                             [None,None,"Trading","4","Factory",None,None],
                             ["IT","Factory","5","1","5","Trading","Processing"],
                             ["7","6","3","star","3","6","7"],
                             ["Processing","Trading","5","1","5","Factory","IT"],
                             [None,None,"Factory","4","Trading",None,None],
                             [None,None,"IT","2","Processing",None,None]]
        
        self.FOURS_POINT_PLUS = {  "IT":{"A": 2, "B": 3, "C": 2, "D": 1},
                                    "Factory":{"A": 2, "B": 2, "C": 2, "D": 3},
                                    "Processing":{"A": 2, "B": 1, "C": 3, "D": 2},
                                    "Trading":{"A": 2, "B": 2, "C": 1, "D": 2}}

        self.DESTS_POINT_MINUS   = {"IT": {"Study": 1},
                                    "Factory": {"Resources": 1},
                                    "Processing": {"Power": 1},
                                    "Trading": {"Processing":1},
                                    "1": {"Processing":2, "Resources":2},
                                    "2": {"Trading":2, "Resources":2},
                                    "3": {"Trading":2, "Processing":2},
                                    "4": {"Study":1, "IT":2},
                                    "5": {"IT":2, "Power":1},
                                    "6": {"Study":1, "Factory":2},
                                    "7": {"Power":1, "Factory":2}}             


    def judge(self, player: str, owner: str, y, x):
        self.dest = self.DEST_ARRAY[y][x]
        if self.dest == "star" or self.dest == None:
            return 1
        else:
            self.flag = 0
            if owner == player or owner == "N":
                for self.key, self.value in self.DESTS_POINT_MINUS[self.dest].items():
                    self.dict = {self.key : self.value}
                    print(self.dict)
                    if self.points[self.key] >= self.value:
                        self.flag = 1
                    else:
                        self.flag = 0
                        break
            else:
                for self.key, self.value in self.DESTS_POINT_MINUS[self.dest].items():
                    self.dict = {self.key : 2*self.value}
                    if self.points[self.key] >= 2*self.value:
                        self.flag = 1
                    else:
                        self.flag = 0
                        break
            return self.flag


    def update(self, player: str, owner: str):
        if player == owner or owner == "N":
            for self.key, self.value in self.DESTS_POINT_MINUS[self.dest].items():
                self.dict = {self.key : self.value}
                self.points[self.key] -= self.dict[self.key]
            if self.dest in self.FOURS_POINT_PLUS:
                self.points[self.dest] += self.FOURS_POINT_PLUS[self.dest][player]
        else:
            for self.key, self.value in self.DESTS_POINT_MINUS[self.dest].items():
                self.dict = {self.key : 2*self.value}
                self.points[self.key] -= self.dict[self.key]
            if self.dest in self.FOURS_POINT_PLUS:
                self.points[self.dest] += self.FOURS_POINT_PLUS[self.dest][player]
                

    def turn_update(self):
        self.points["Study"] += 1
        self.points["Power"] += 1
        self.points["Resources"] += 1