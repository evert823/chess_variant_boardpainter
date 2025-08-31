from classes.board_painter import BoardPainter

myboardpainter = BoardPainter()

positionpath = ".\\positions"
boardpath = ".\\boardimages"

myboardpainter.load_file(f"{positionpath}\\personA_personB.json")
myboardpainter.create_board_image_and_save(f"{boardpath}\\personA_personB.png")
myboardpainter.load_file(f"{positionpath}\\personC_personD.json")
myboardpainter.create_board_image_and_save(f"{boardpath}\\personC_personD.png")
myboardpainter.load_file(f"{positionpath}\\kr_nn_2char.json")
myboardpainter.create_board_image_and_save(f"{boardpath}\\kr_nn_2char.png")

myboardpainter.pieceimages_folder = "pieceimages_classicwood"
myboardpainter.pieceimages_extension = "png"
myboardpainter.a1_is_white = False

myboardpainter.load_file(f"{positionpath}\\test_classicwood.json")
myboardpainter.create_board_image_and_save(f"{boardpath}\\test_classicwood.png")
myboardpainter.load_file(f"{positionpath}\\dark_forest_initial.json")
myboardpainter.create_board_image_and_save(f"{boardpath}\\dark_forest_initial.png")
myboardpainter.load_file(f"{positionpath}\\dumbarton_initial.json")
myboardpainter.create_board_image_and_save(f"{boardpath}\\dumbarton_initial.png")
