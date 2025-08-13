from classes.chu_board_painter import ChuBoardPainter

mychuboardpainter = ChuBoardPainter()
mychuboardpainter.pieceimages_folder = "..\\chu_shogi_piece_images\\output_set1"
mychuboardpainter.load_file(".\\shogi_variants\\positions\\tenjiku_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\tenjiku_initial_position_set1.png")
mychuboardpainter.load_file(".\\shogi_variants\\positions\\tenjiku_show_promotions.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\tenjiku_show_promotions_set1.png")

mychuboardpainter.pieceimages_folder = "..\\chu_shogi_piece_images\\output_set2"
mychuboardpainter.load_file(".\\shogi_variants\\positions\\tenjiku_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\tenjiku_initial_position_set2.png")
mychuboardpainter.load_file(".\\shogi_variants\\positions\\tenjiku_show_promotions.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\tenjiku_show_promotions_set2.png")
