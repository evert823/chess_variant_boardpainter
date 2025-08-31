from classes.board_painter import BoardPainter

myboardpainter = BoardPainter()
myboardpainter.load_file(".\\positions\\personA_personB.json")
myboardpainter.create_board_image_and_save(".\\boardimages\\personA_personB.png")
myboardpainter.load_file(".\\positions\\personC_personD.json")
myboardpainter.create_board_image_and_save(".\\boardimages\\personC_personD.png")
myboardpainter.load_file(".\\positions\\kr_nn_2char.json")
myboardpainter.create_board_image_and_save(".\\boardimages\\kr_nn_2char.png")

myboardpainter.pieceimages_folder = "pieceimages_classicwood"
myboardpainter.pieceimages_extension = "png"
myboardpainter.a1_is_white = False

myboardpainter.load_file(".\\positions\\test_classicwood.json")
myboardpainter.create_board_image_and_save(".\\boardimages\\test_classicwood.png")
myboardpainter.load_file(".\\positions\\dark_forest_initial.json")
myboardpainter.create_board_image_and_save(".\\boardimages\\dark_forest_initial.png")
myboardpainter.load_file(".\\positions\\dumbarton_initial.json")
myboardpainter.create_board_image_and_save(".\\boardimages\\dumbarton_initial.png")
