#handle chess position with 3D structure - load from JSON
import json

class ChessPosition3D:
    def __init__(self):
        self.boardwidth = -1
        self.boardheight = -1
        self.depth_3d = -1
        self.squares = []
        self.reset_boardsize(0, 0, 0)

    def reset_boardsize(self, pboardwidth, pboardheight, pdepth_3d):
        self.boardwidth = pboardwidth
        self.boardheight = pboardheight
        self.depth_3d = pdepth_3d
        self.squares.clear()
        for z in range(self.depth_3d):
            mylayer = []
            for j in range(self.boardheight):
                myrank = []
                for i in range(self.boardwidth):
                    myrank.append("")
                mylayer.append(myrank)
            self.squares.append(mylayer)

    def load_from_json(self, pfilename):
        #Load from json file and convert to class structure
        positionfile = open(pfilename, 'r')
        positiondict = json.load(positionfile)
        positionfile.close()
        self.boardwidth = positiondict["boardwidth"]
        self.boardheight = positiondict["boardheight"]
        self.depth_3d = positiondict["depth_3d"]
        self.reset_boardsize(self.boardwidth, self.boardheight, self.depth_3d)

        for z in range(self.depth_3d):
            for j in range(self.boardheight):
                rj = (self.boardheight - 1) - j
                mysymbol = positiondict["layers"][z]["squares"][rj].split("|")
                for i in range(self.boardwidth):
                    s = mysymbol[i].lstrip()
                    self.squares[z][j][i] = s
        #self.print_squares()

    def print_squares(self):
        for z in range(self.depth_3d):
            for j in range(self.boardheight):
                for i in range(self.boardwidth):
                    print(self.squares[z][j][i], end=",")
                print("", end="\n")
