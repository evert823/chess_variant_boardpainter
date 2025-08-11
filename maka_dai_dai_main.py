from classes.chu_board_painter import ChuBoardPainter

mychuboardpainter = ChuBoardPainter()

mychuboardpainter.pieceimages_folder = "pieceimages_chushogi_set2"
mychuboardpainter.load_file(".\\positions\\maka_dai_dai_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\maka_dai_dai_initial_position_set2.png")
