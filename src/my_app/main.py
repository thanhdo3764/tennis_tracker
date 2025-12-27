from my_app.constants import *
import matplotlib.pyplot as plt
from cv2 import findHomography, perspectiveTransform
import numpy as np


def draw_court(ax):
	# Outer court
	ax.plot(
		[-COURT_WIDTH_DOUBLES/2, COURT_WIDTH_DOUBLES/2, COURT_WIDTH_DOUBLES/2, -COURT_WIDTH_DOUBLES/2, -COURT_WIDTH_DOUBLES/2],
		[-COURT_LENGTH/2, -COURT_LENGTH/2, COURT_LENGTH/2, COURT_LENGTH/2, -COURT_LENGTH/2],
		color="black"
	)

	# Singles sidelines
	for x in (-COURT_WIDTH_SINGLES/2, COURT_WIDTH_SINGLES/2):
		ax.plot([x, x], [-COURT_LENGTH/2, COURT_LENGTH/2], color="black")

	# Net
	ax.plot([-COURT_WIDTH_DOUBLES/2, COURT_WIDTH_DOUBLES/2], [0, 0], color="black")

	# Service lines
	for y in (-SERVICE_LINE_DIST, SERVICE_LINE_DIST):
		ax.plot([-COURT_WIDTH_SINGLES/2, COURT_WIDTH_SINGLES/2], [y, y], color="black")

	# Center service line
	ax.plot([0, 0], [-SERVICE_LINE_DIST, SERVICE_LINE_DIST], color="black")

	ax.set_aspect("equal")
	ax.axis("off")

def draw_ball_landing(ax, landings):
	xs, ys = zip(*landings)
	ax.scatter(xs, ys, c="yellow", edgecolors="black", s=100, zorder=5)

def image_to_top_down_pts(img_pts, img_ball_pt):
	homography_matrix, _ = findHomography(np.array(img_pts, dtype=np.float32), np.array(list(WORLD_PTS.values()), dtype=np.float32))
	np_img_ball_pt = np.array([[[*img_ball_pt]]], dtype=np.float32)
	world_ball_pt = perspectiveTransform(np_img_ball_pt, homography_matrix)
	x, y = world_ball_pt[0][0]
	print(x,y)
	return (x,y)

def main():

	fig, ax = plt.subplots(figsize=(6, 5))
	draw_court(ax)
	landings = [
	    (1.2, -5.3),
	    (-0.8, -6.0),
	    (0.3, -4.9),
	]
	draw_ball_landing(ax, landings)
	plt.show()

if __name__ == '__main__':
	main()