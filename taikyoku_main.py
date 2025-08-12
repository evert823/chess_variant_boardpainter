from classes.chu_board_painter import ChuBoardPainter

mychuboardpainter = ChuBoardPainter()

#Instead of duplicating image files across repos we can reference the other repo
#We do so for Taikyoku
#mychuboardpainter.pieceimages_folder = "shogi_variants\\pieceimages_chushogi_set2"
mychuboardpainter.pieceimages_folder = "..\\chu_shogi_piece_images\\output_set2"

mychuboardpainter.load_file(".\\shogi_variants\\positions\\taikyoku_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\taikyoku_initial_position_set2.png")
