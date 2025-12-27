import unittest
from my_app.main import *
from my_app.constants import WORLD_PTS

class TestMain(unittest.TestCase):


	def test_image_to_top_down_pts(self):
		img_pts = [(0,0), (5,0), (6,10), (0, 10)]
		world_pts = list(WORLD_PTS.values())
		for i in range(4):
			converted_pt = image_to_top_down_pts(img_pts, img_pts[i])
			self.assertEqual(converted_pt, world_pts[i])

if __name__ == '__main__':
	unittest.main()