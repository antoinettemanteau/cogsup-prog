import expyriment
expyriment.control.set_develop_mode(True)
exp = expyriment.design.Experiment(
    name="Four Corner Squares",
    background_colour=expyriment.misc.constants.C_BLACK
)
expyriment.control.initialize(exp)
screen_width, screen_height = exp.screen.size
square_size = int(screen_width * 0.05)
x_offset = (screen_width / 2) - (square_size / 2)
y_offset = (screen_height / 2) - (square_size / 2)
positions = [
    (x_offset, y_offset),
    (-x_offset, y_offset),
    (x_offset, -y_offset),
    (-x_offset, -y_offset)
]
canvas = expyriment.stimuli.Canvas(size=exp.screen.size)
for pos in positions:
    square = expyriment.stimuli.Rectangle(
        size=(square_size, square_size),
        position=pos,
        colour=expyriment.misc.constants.C_RED,
        line_width=1
    )
    square.plot(canvas)
expyriment.control.start(exp)
canvas.present()
exp.keyboard.wait()
expyriment.control.end()