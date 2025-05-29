#mvp_3d is a MVP for handle chess position with 3D structure and create the image
from PIL import Image
from chess_position_3d import ChessPosition3D
from board_painter import BoardPainter

class mvp_3d:
    def __init__(self):
        self.MyChessPosition3D = ChessPosition3D()
        self.MyBoardPainter = BoardPainter()
        self.layer_marge = 6
        self.boardimage = None
        self.w = 0
        self.h = 0

    def load_file(self, pfilename):
        self.MyChessPosition3D.load_from_json(pfilename)

    def prepare_layer(self, z: int):
        for j in range(self.MyChessPosition3D.boardheight):
            for i in range(self.MyChessPosition3D.boardwidth):
                self.MyBoardPainter.MyChessPosition.squares[j][i] = self.MyChessPosition3D.squares[z][j][i]
        self.MyBoardPainter.create_board_image()

    def prepare_board(self):
        self.MyBoardPainter.MyChessPosition.reset_boardsize(self.MyChessPosition3D.boardwidth, self.MyChessPosition3D.boardheight)
        self.w, self.h = self.MyBoardPainter.boardimage_w_h()
        full_w = (self.w * self.MyChessPosition3D.depth_3d) + ((self.MyChessPosition3D.depth_3d + 1) * self.layer_marge)
        full_h = self.h + (2 * self.layer_marge)
        self.boardimage = Image.new('RGB', (full_w, full_h), (80, 4, 4))

    def create_board_image_and_save(self, pimagefilename):
        self.prepare_board()
        for z in range(self.MyChessPosition3D.depth_3d):
            self.prepare_layer(z)
            x = ((self.w + self.layer_marge) * z) + self.layer_marge
            y = self.layer_marge
            self.boardimage.paste(self.MyBoardPainter.boardimage, (x, y))
        self.boardimage.save(pimagefilename)

