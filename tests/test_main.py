import unittest
from my_app.main import *
from my_app.constants import WORLD_PTS
from my_app.transforms import *

class TestMain(unittest.TestCase):

	def test_convert_ball_landing(self):
		img_pts = [(0,0), (5,0), (6,10), (0, 10)]
		world_pts = list(WORLD_PTS.values())
		t = Transformer(img_pts)
		for i in range(4):
			converted_pt = t.convert_ball_landing(img_pts[i])
			self.assertEqual(converted_pt, world_pts[i])

if __name__ == '__main__':
	unittest.main()