from board_painter import BoardPainter

myboardpainter = BoardPainter()
myboardpainter.load_file(".\\positions\\personA_personB.json")
myboardpainter.create_board_image(".\\boardimages\\personA_personB.png")
myboardpainter.load_file(".\\positions\\personC_personD.json")
myboardpainter.create_board_image(".\\boardimages\\personC_personD.png")

myboardpainter.pieceimages_folder = "pieceimages_classicwood"
myboardpainter.pieceimages_extension = "png"
myboardpainter.load_file(".\\positions\\test_classicwood.json")
myboardpainter.create_board_image(".\\boardimages\\test_classicwood.png")
