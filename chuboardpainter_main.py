from classes.chu_board_painter import ChuBoardPainter

mychuboardpainter = ChuBoardPainter()
mychuboardpainter.load_file(".\\positions\\chu_shogi.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi.png")
