import matplotlib.pyplot as plt
from constants import COURT_LENGTH, COURT_WIDTH_DOUBLES, COURT_WIDTH_SINGLES, SERVICE_LINE_DIST

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

def main():
	fig, ax = plt.subplots(figsize=(6, 5))  # 1 & 2
	draw_court(ax)                           # 3
	plt.show()

if __name__ == '__main__':
	main()