from typing import Tuple
from my_app.constants import *
from cv2 import findHomography, perspectiveTransform
import numpy as np

class Transformer:
	_homography = None
	_inv_homography = None

	# pts must be [bottom left, bottom right, top right, top left]
	def __init__(self, pts):
		self._homography, _ = findHomography(np.array(pts, dtype=np.float32), np.array(list(WORLD_PTS.values()), dtype=np.float32))
		self._inv_homography, _ = findHomography(np.array(list(WORLD_PTS.values()), dtype=np.float32), np.array(pts, dtype=np.float32))

	def update_homography(self, pts):
		self._homography, _ = findHomography(np.array(pts, dtype=np.float32), np.array(list(WORLD_PTS.values(), dtype=np.float32)))
		self._inv_homography, _ = findHomography(np.array(list(WORLD_PTS.values()), dtype=np.float32), np.array(pts, dtype=np.float32))

	# ball_landing contains a tuple of (x, y)
	def convert_points(self, pts, inverse=False):
		np_pts = np.array(pts, dtype=np.float32)
		np_pts = np_pts.reshape(-1, 1, 2)
		world_pts = perspectiveTransform(np_pts, self._inv_homography if inverse else self._homography)
		world_pts = world_pts.reshape(-1, 2)
		return world_pts