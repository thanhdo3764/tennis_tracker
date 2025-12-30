import matplotlib.pyplot as plt
from my_app.constants import *
from my_app.transforms  import *

class CourtIllustrator:
	fig = None
	axes = None

	def __init__(self):
		self.fig, self.axes = plt.subplots(nrows=1, ncols=2, figsize=(14,6))

	def draw_camera_view(self, ax, doubles_corners):
		corners_list = [doubles_corners["bottom_left"], doubles_corners["bottom_right"], doubles_corners["top_right"], doubles_corners["top_left"]]
		converter = Transformer(corners_list)

		# Outer court
		square = [DOUBLES_CORNERS["bottom_left"], DOUBLES_CORNERS["bottom_right"], DOUBLES_CORNERS["top_right"], DOUBLES_CORNERS["top_left"], DOUBLES_CORNERS["bottom_left"]]
		square = converter.convert_points(square, inverse=True)
		xs, ys = zip(*square)
		ax.plot(xs, ys, color="black")

		# Singles sidelines
		left_line = [SINGLES_CORNERS["bottom_left"], SINGLES_CORNERS["top_left"]]
		left_line = converter.convert_points(left_line, inverse=True)
		right_line = [SINGLES_CORNERS["bottom_right"], SINGLES_CORNERS["top_right"]]
		right_line = converter.convert_points(right_line, inverse=True)
		xs, ys = zip(*left_line)
		ax.plot(xs, ys, color="black")
		xs, ys = zip(*right_line)
		ax.plot(xs, ys, color="black")

		# Net
		line = [(-COURT_WIDTH_DOUBLES/2, 0),(COURT_WIDTH_DOUBLES/2, 0)]
		line = converter.convert_points(line, inverse=True)
		xs, ys = zip(*line)
		ax.plot(xs, ys, color="black")

		# Service lines
		top_line = [SERVICE_CORNERS["top_left"], SERVICE_CORNERS["top_right"]]
		top_line = converter.convert_points(top_line, inverse=True)
		bottom_line = [SERVICE_CORNERS["bottom_left"], SERVICE_CORNERS["bottom_right"]]
		bottom_line = converter.convert_points(bottom_line, inverse=True)
		xs, ys = zip(*top_line)
		ax.plot(xs, ys, color="black")
		xs, ys = zip(*bottom_line)
		ax.plot(xs, ys, color="black")

		# Center service line
		line = [(0, SERVICE_LINE_DIST), (0, -SERVICE_LINE_DIST)]
		line = converter.convert_points(line, inverse=True)
		xs, ys = zip(*line)
		ax.plot(xs, ys, color="black")

		ax.set_aspect("equal")
		ax.axis("off")

	def draw_court(self, ax):
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

	def draw_ball_landing(self, ax, landings):
		xs, ys = zip(*landings)
		ax.scatter(xs, ys, c="yellow", edgecolors="black", s=100, zorder=5)