from classes.chu_board_painter import ChuBoardPainter

mychuboardpainter = ChuBoardPainter()
mychuboardpainter.load_file(".\\positions\\chu_shogi_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi_initial_position.png")
mychuboardpainter.load_file(".\\positions\\chu_shogi_show_promotions.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi_show_promotions.png")
