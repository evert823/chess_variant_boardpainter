#mvp_3d is a MVP for handle chess position with 3D structure and create the image
from classes.mvp_3d import mvp_3d

mymvp_3d = mvp_3d()

positionpath = ".\\positions_3d"
boardpath = ".\\boardimages\\3D"

mymvp_3d.MyBoardPainter.pieceimages_folder = "pieceimages_classicwood"
mymvp_3d.MyBoardPainter.pieceimages_extension = "png"
mymvp_3d.MyBoardPainter.a1_is_white = False

mymvp_3d.load_file(f"{positionpath}\\my3Dposition.json")
mymvp_3d.create_board_image_and_save(f"{boardpath}\\my3Dposition.png")
