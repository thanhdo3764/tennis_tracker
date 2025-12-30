from my_app.constants import *
from my_app.court_illustrator import *
import matplotlib.pyplot as plt

def main():
	doubles_corners = {"bottom_left": (-8, -5),
				"bottom_right": (8, -5),
				"top_right": (4, 2),
				"top_left": (-4, 2)}

	drawing = CourtIllustrator()
	drawing.draw_camera_view(drawing.axes[0], doubles_corners)
	drawing.draw_court(drawing.axes[1])
	landings = [
	    (1.2, -5.3),
	    (-0.8, -6.0),
	    (0.3, -4.9),
	]
	# draw_ball_landing(ax, landings)
	plt.show()

if __name__ == '__main__':
	main()