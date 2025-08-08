from classes.chu_board_painter import ChuBoardPainter

mychuboardpainter = ChuBoardPainter()
mychuboardpainter.pieceimages_folder = "pieceimages_chushogi_set1"
mychuboardpainter.load_file(".\\positions\\chu_shogi_demo.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi_demo_set1.png")
mychuboardpainter.load_file(".\\positions\\chu_shogi_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi_initial_position_set1.png")
mychuboardpainter.load_file(".\\positions\\chu_shogi_show_promotions.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi_show_promotions_set1.png")

mychuboardpainter.pieceimages_folder = "pieceimages_chushogi_set2"
mychuboardpainter.load_file(".\\positions\\chu_shogi_demo.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi_demo_set2.png")
mychuboardpainter.load_file(".\\positions\\chu_shogi_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi_initial_position_set2.png")
mychuboardpainter.load_file(".\\positions\\chu_shogi_show_promotions.json")
mychuboardpainter.create_board_image_and_save(".\\boardimages\\chu_shogi_show_promotions_set2.png")
