from classes.chu_board_painter import ChuBoardPainter

mychuboardpainter = ChuBoardPainter()

mychuboardpainter.pieceimages_folder = "..\\chu_shogi_piece_images\\output_set2"

mychuboardpainter.load_file(".\\shogi_variants\\positions\\dai_dai_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\dai_dai_initial_position_set2.png")

mychuboardpainter.load_file(".\\shogi_variants\\positions\\maka_dai_dai_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\maka_dai_dai_initial_position_set2.png")

mychuboardpainter.load_file(".\\shogi_variants\\positions\\tai_initial_position.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\tai_initial_position_set2.png")

mychuboardpainter.pieceimages_folder = "..\\chu_shogi_piece_images\\output_set2"
mychuboardpainter.load_file(".\\shogi_variants\\positions\\invented_by_GHPC.json")
mychuboardpainter.create_board_image_and_save(".\\shogi_variants\\boardimages\\invented_by_GHPC.png")
