import random

class SpaceStatus:
    def __init__(self) ->  None:
        # variable
        self.spaces = [[ "A", "A", "N", "N", "N", "B", "B"],
                       [ "A", "A", "N", "N", "N", "B", "B"],
                       [ "N", "N", "N", "N", "N", "N", "N"],
                       [ "N", "N", "N", "N", "N", "N", "N"],
                       [ "N", "N", "N", "N", "N", "N", "N"],
                       [ "D", "D", "N", "N", "N", "C", "C"],
                       [ "D", "D", "N", "N", "N", "C", "C"]]

    def judge(self, player: str, y, x):
        if (y==0 or y==1 or y==5 or y==6) and (x==0 or x==1 or x==5 or x==6):
            return 0
        elif y==3 or x==3 or ((y==2 or y==4) and 2<=x<=4):
            if y==0:
                if (self.spaces[y+1][x]==player or self.spaces[y][x-1]==player or self.spaces[y][x+1]==player) and self.spaces[y][x] != player:
                    return 1
                else:
                    return 0
            elif y==6:
                if (self.spaces[y-1][x]==player or self.spaces[y][x-1]==player or self.spaces[y][x+1]==player) and self.spaces[y][x] != player:
                    return 1
                else:
                    return 0
            elif x==0:
                if (self.spaces[y-1][x]==player or self.spaces[y+1][x]==player or self.spaces[y][x+1]==player) and self.spaces[y][x] != player:
                    return 1
                else:
                    return 0
            elif x==6:
                if (self.spaces[y-1][x]==player or self.spaces[y+1][x]==player or self.spaces[y][x-1]==player) and self.spaces[y][x] != player:
                    return 1
                else:
                    return 0
            else:
                if (self.spaces[y-1][x]==player or self.spaces[y+1][x]==player or self.spaces[y][x-1]==player or self.spaces[y][x+1]==player) and self.spaces[y][x] != player:
                    return 1
                else:
                    return 0


        elif y==0:
            if self.spaces[y+1][x]==player or self.spaces[y][x-1]==player or self.spaces[y][x+1]==player:
                return 1
            else:
                return 0
        elif y==6:
            if self.spaces[y-1][x]==player or self.spaces[y][x-1]==player or self.spaces[y][x+1]==player:
                return 1
            else:
                return 0
        elif x==0:
            if self.spaces[y-1][x]==player or self.spaces[y+1][x]==player or self.spaces[y][x+1]==player:
                return 1
            else:
                return 0
        elif x==6:
            if self.spaces[y-1][x]==player or self.spaces[y+1][x]==player or self.spaces[y][x-1]==player:
                return 1
            else:
                return 0
        else:
            if self.spaces[y-1][x]==player or self.spaces[y+1][x]==player or self.spaces[y][x-1]==player or self.spaces[y][x+1]==player:
                return 1
            else:
                return 0

    def update(self, player: str, y, x):
        self.spaces[y][x] = player

    def rand_star(self):
        if random.getrandbits(1):
            return 1
        else:
            return 0