from typing import Tuple
from my_app.constants import *
from cv2 import findHomography, perspectiveTransform
import numpy as np

class Transformer:
	_homography = None

	# pts must be [bottom left, bottom right, top right, top left]
	def __init__(self, pts):
		self._homography, _ = findHomography(np.array(pts, dtype=np.float32), np.array(list(WORLD_PTS.values()), dtype=np.float32))

	def update_homography(self, pts):
		self._homography, _ = findHomography(np.array(pts, dtype=np.float32), np.array(list(WORLD_PTS.values()), dtype=np.float32))

	# ball_landing contains a tuple of (x, y)
	def convert_ball_landing(self, ball_landing: Tuple[int, int]):
		np_ball_pt = np.array([[[*ball_landing]]], dtype=np.float32)
		world_ball_pt = perspectiveTransform(np_ball_pt, self._homography)
		x, y = world_ball_pt[0][0]
		return (x,y)