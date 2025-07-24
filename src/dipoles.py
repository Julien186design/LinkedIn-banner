"""
Header file for electrical components (dipoles)
Contains drawing functions for resistor, inductor and capacitor
"""

def draw_resistor(draw, x, y, color, width=3):
    resistor = [20, 40, 20] # width, height, terminal

    draw.line([(x - resistor[1], y - resistor[0]),
               (x + resistor[1], y - resistor[0])], fill=color, width=width)

    draw.line([(x - resistor[1], y + resistor[0]),
               (x + resistor[1], y + resistor[0])], fill=color, width=width)
    # left vertical line
    draw.line([(x - resistor[1], y - resistor[0]),
               (x - resistor[1], y + resistor[0])], fill=color, width=width)
    # right vertical line
    draw.line([(x + resistor[1], y - resistor[0]),
               (x + resistor[1], y + resistor[0])], fill=color, width=width)

    draw.line([(x + resistor[1] + resistor[2], y),
               (x + resistor[1], y)], fill=color, width=width)
    draw.line([(x - resistor[1] - resistor[2], y),
               (x - resistor[1], y)], fill=color, width=width)

def draw_inductor(draw, x, y, color, width=3, arc_width=20, arc_height=60):
    terminal = 25
    nb_spires = 5
    for i in range(nb_spires):
        offset = (i - nb_spires / 2) * arc_width
        draw.arc(
            [x + offset, y - arc_height / 4, x + offset + arc_width, y + arc_height / 4],
            start=180, end=0, fill=color, width=width)

    left = nb_spires * arc_width / 2
    right = (nb_spires - nb_spires / 2) * arc_width
    draw.line([(x - left, y), (x - left - terminal, y)], fill=color, width=width)
    draw.line([(x + right, y), (x + right + terminal, y)], fill=color, width=width)

def draw_capacitor(draw, x, y, color, width=3, plate_height=40, spacing=10):
    terminal = 35
    draw.line([(x - spacing // 2, y),
               (x - spacing // 2 - terminal, y)],
              fill=color, width=width)
    draw.line([(x + spacing // 2, y),
               (x + spacing // 2 + terminal, y)],
              fill=color, width=width)

    # First plate
    draw.line([(x - spacing // 2, y - plate_height // 2),
               (x - spacing // 2, y + plate_height // 2)],
              fill=color, width=width)

    # Second plate
    draw.line([(x + spacing // 2, y - plate_height // 2),
               (x + spacing // 2, y + plate_height // 2)],
              fill=color, width=width)

def draw_components(draw, central_x, central_y, color, left_x, right_x):

    # Resistor
    draw_resistor(draw, left_x, central_y, color)

    # Inductor
    draw_inductor(draw, central_x, central_y, color)

    # Capacitor
    draw_capacitor(draw, right_x, central_y, color)
