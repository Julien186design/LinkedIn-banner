from PIL import Image, ImageDraw, ImageFont
from dipoles import draw_components

def basics():
    # LinkedIn dimensions
    width, height = 928, 190

    # Colors
    bg_color = (15, 32, 39)
    gradient_end = (44, 83, 100)
    text_color = (255, 255, 255)
    component_color = (78, 205, 196)

    # Create image and drawing object
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Create horizontal gradient
    for x in range(width):
        ratio = x / width
        r = int(bg_color[0] * (1 - ratio) + gradient_end[0] * ratio)
        g = int(bg_color[1] * (1 - ratio) + gradient_end[1] * ratio)
        b = int(bg_color[2] * (1 - ratio) + gradient_end[2] * ratio)
        draw.line([(x, 0), (x, height)], fill=(r, g, b))

    # Load fonts
    try:
        font_large = ImageFont.truetype("arial.ttf", 30)
        font_small = ImageFont.truetype("arial.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()


    # Main text
    x = 100
    draw.text((x, 20), "INGÉNIEUR ÉLECTRIQUE", fill=text_color, font=font_large)

    # Return all necessary objects
    dephasing = 180
    central_x = 575
    return img, draw, height, font_small, component_color, text_color, dephasing, central_x

def dipoles_with_name():
    img, draw, height, font_small, component_color, text_color, dephasing, central_x = basics()

    central_y = height // 2
    left_x = central_x - dephasing
    right_x = central_x + dephasing

    # Draw all components (now from dipoles.py file)
    draw_components(draw, central_x, height // 2, component_color, left_x, right_x)

    # Resistor
    text = "RÉSISTANCE"
    text_width = draw.textlength(text, font=font_small)
    text_x = left_x - text_width // 2
    draw.text((text_x, central_y + 50), text, fill=text_color, font=font_small)

    # Inductor
    text = "INDUCTANCE"
    text_width = draw.textlength(text, font=font_small)
    text_x = central_x - text_width // 2
    draw.text((text_x, central_y + 50), text, fill=text_color, font=font_small)

    # Capacitor
    text = "CONDENSATEUR"
    text_width = draw.textlength(text, font=font_small)
    text_x = right_x - text_width / 2
    draw.text((text_x, central_y + 50), text, fill=text_color, font=font_small)

    # Save image
    img.save("LinkedIn banner - texts.png")

def draw_formula_with_fraction(draw, x, y, main_text, num_text, denom_text, font, font_italic,
                               text_color, component_color, width=3, bar_extra_length=1.0):
    main_width = draw.textlength(main_text, font=font)
    draw.text((x, y), main_text, fill=text_color, font=font)

    bar_x_start = x + main_width
    ascent, descent = font.getmetrics()
    bar_y = y + (ascent - descent) + font.size // 5

    width_l = draw.textlength("L", font=font)
    bar_x_end = bar_x_start + int(2 * width_l * bar_extra_length)  # Multiply by bar_extra_length for adjustment
    draw.line([(bar_x_start, bar_y), (bar_x_end, bar_y)], fill=component_color, width=width)

    draw.text((bar_x_start, y - font.size // 5), num_text, fill=text_color, font=font_italic)
    draw.text((bar_x_start, y + font.size), denom_text, fill=text_color, font=font_italic)

def dipoles_with_formula(width=3):
    img, draw, height, font_small, component_color, text_color, dephasing, central_x = basics()
    h = 6
    central_y = h * height // 8
    left_x = central_x - dephasing
    right_x = central_x + dephasing

    # Draw all components (now from dipoles.py file)
    draw_components(draw, central_x, (h - 2) * height // 8, component_color, left_x, right_x)

    font_italic = ImageFont.truetype("ariali.ttf", font_small.size)

    # Resistor
    text = "U = R.I"
    text_width = draw.textlength(text, font=font_small)
    draw.text((left_x - text_width // 2, central_y), text, fill=text_color, font=font_small)

    # Inductor
    draw_formula_with_fraction(
        draw, central_x - draw.textlength("U = L.di", font=font_small) // 2, central_y,
        "U = L.", "dI", "dt", font_small, font_italic, text_color, component_color, width, 0.9
    )

    # Capacitor (note: here it's "I = C." not "U = C.")
    draw_formula_with_fraction(
        draw, right_x - draw.textlength("I = C.dU", font=font_small) // 2, central_y,
        "i = C.", "dU", "dt", font_small, font_italic, text_color, component_color, width, 1.2
    )

    img.save("LinkedIn banner - formulas.png")
