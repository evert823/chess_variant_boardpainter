from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from classes.chess_position import ChessPosition
from classes.piece_name_handler import PieceNameHandler

class ChuBoardPainter:
    """
    Here we implement a board painter tool for
    - Chu Shogi
    - Shogi variants in general
    """
    def __init__(self):
        self.MyChessPosition = ChessPosition()
        self.MyPieceNameHandler = PieceNameHandler()
        self.piecewidth = 72
        self.pieceheight = 79
        self.boardimage = Image.new('RGB', (self.piecewidth, self.pieceheight), (0, 0, 0))
        self.load_piece_definitions()

    def load_piece_definitions(self):
        self.MyPieceNameHandler.load_piece_definitions(filename=".\\piecedefinitions\\chushogipiecedefinitions.csv")
        mytest = self.MyPieceNameHandler.lookup_piecename_by_symbol("K")
        assert mytest == "King"
        mytest = self.MyPieceNameHandler.lookup_piecename_by_symbol("L")
        assert mytest == "Lance"
        mytest = self.MyPieceNameHandler.lookup_piecename_by_symbol(".")
        assert mytest == ""

    def load_file(self, pfilename):
        self.MyChessPosition.load_from_json(pfilename)
