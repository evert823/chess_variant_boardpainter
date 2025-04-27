from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from chess_position import ChessPosition
from piece_name_handler import PieceNameHandler

class BoardPainter:
    def __init__(self):
        self.MyChessPosition = ChessPosition()
        self.MyPieceNameHandler = PieceNameHandler()
        self.pieceimages_folder = "pieceimages"
        self.pieceimages_extension = "jpg"
        self.piecesize = 57
        self.edgesize_top = 6
        self.edgesize_bottom = 24
        self.edgesize_left = 22
        self.edgesize_right = 6
        self.boardimage = Image.new('RGB', (self.piecesize, self.piecesize), (0, 0, 0))
        self.load_piece_definitions()

    def load_piece_definitions(self):
        self.MyPieceNameHandler.load_piece_definitions()
        mytest = self.MyPieceNameHandler.lookup_piecename_by_symbol("K")
        assert mytest == "King"
        mytest = self.MyPieceNameHandler.lookup_piecename_by_symbol(".")
        assert mytest == ""

    def load_file(self, pfilename):
        self.MyChessPosition.load_from_json(pfilename)

    def prepare_board(self):
        w = self.MyChessPosition.boardwidth * self.piecesize
        w += self.edgesize_left
        w += self.edgesize_right
        h = self.MyChessPosition.boardheight * self.piecesize
        h += self.edgesize_top
        h += self.edgesize_bottom
        self.boardimage = Image.new('RGB', (w, h), (0, 0, 0))

    def add_coordinates(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        draw = ImageDraw.Draw(self.boardimage)
        font = ImageFont.truetype("arial.ttf", 16)

        for j in range(self.MyChessPosition.boardheight):
            rj = (self.MyChessPosition.boardheight - 1) - j
            y = rj * self.piecesize
            y += self.edgesize_top
            y += 21
            draw.text((7, y),str(j + 1),(255,255,255),font=font)

        for i in range(self.MyChessPosition.boardwidth):
            y = (self.MyChessPosition.boardheight) * self.piecesize
            y += self.edgesize_top
            x = i * self.piecesize
            x += self.edgesize_left
            x += 23
            try:
                myabc = alphabet[i]
            except:
                myabc = str(i)
            draw.text((x, y),myabc,(255,255,255),font=font)

    def _symbol_found(self, psymbol: str, ppiecename: str):
        teststring = psymbol.replace("-", "").replace(" ", "").replace(".", "")
        if teststring != "" and ppiecename == "":
            return False
        return True

    def paste_piece_image(self, j: int, i: int, psymbol: str):
        if psymbol[0] == "-":
            piececolour = "black"
        else:
            piececolour = "white"
        piecename = self.MyPieceNameHandler.lookup_piecename_by_symbol(psymbol.replace("-", ""))
        symbol_found = self._symbol_found(psymbol=psymbol, ppiecename=piecename)

        x = i * self.piecesize
        x += self.edgesize_left
        rj = (self.MyChessPosition.boardheight - 1) - j
        y = rj * self.piecesize
        y += self.edgesize_top

        if (i + j) % 2 == 0:
            squarecolour = "white"
        else:
            squarecolour = "black"

        if symbol_found == False:
            imagefilename = f"_notfoundon{squarecolour}.{self.pieceimages_extension}"
        elif piecename == "":
            imagefilename = f"vacanton{squarecolour}.{self.pieceimages_extension}"
        else:
            imagefilename = f"{piececolour}{piecename.lower()}on{squarecolour}.{self.pieceimages_extension}"

        try:
            pieceimage = Image.open(f"{self.pieceimages_folder}\\{imagefilename}", mode='r')
        except:
            imagefilename = f"_notfoundon{squarecolour}.{self.pieceimages_extension}"
            pieceimage = Image.open(f"{self.pieceimages_folder}\\{imagefilename}", mode='r')

        pieceimage.convert('RGB')
        self.boardimage.paste(pieceimage, (x, y))

    def create_board_image(self, pimagefilename):
        self.prepare_board()
        self.add_coordinates()

        for j in range(self.MyChessPosition.boardheight):
            for i in range(self.MyChessPosition.boardwidth):
                symbol = self.MyChessPosition.squares[j][i]
                self.paste_piece_image(j, i, symbol)

        self.boardimage.save(pimagefilename)
