import cairo

# Canvas size (sesuai permintaan)
WIDTH, HEIGHT = 900, 300
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Transparent background
ctx.set_source_rgba(0, 0, 0, 0)
ctx.paint()

# Text lines
line1 = "Selamat Datang di"
line2 = "Permainan FunCount"

# Font setup
font_family = "Arial"
ctx.select_font_face(font_family, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

font_size_line1 = 48    # slightly larger for bigger height
font_size_line2 = 72    # main title

# Measure both lines
ctx.set_font_size(font_size_line1)
ext1 = ctx.text_extents(line1)
w1, h1 = ext1.width, ext1.height

ctx.set_font_size(font_size_line2)
ext2 = ctx.text_extents(line2)
w2, h2 = ext2.width, ext2.height

# Vertical centering (300 height → bigger spacing)
total_height = (h1 + h2) + 28  # 28 px gap between lines
start_y = (HEIGHT - total_height) / 2

# -------------------------
# Draw line 1
# -------------------------
ctx.set_font_size(font_size_line1)
(x1, y1, w1, h1, dx1, dy1) = ctx.text_extents(line1)

text_x1 = (WIDTH - w1) / 2 - x1
text_y1 = start_y + h1

outline_color = (0.18, 0.49, 0.20)
fill_color = (1, 1, 1)

ctx.move_to(text_x1, text_y1)
ctx.text_path(line1)
ctx.set_source_rgb(*outline_color)
ctx.set_line_width(6)
ctx.stroke_preserve()
ctx.set_source_rgb(*fill_color)
ctx.fill()

# -------------------------
# Draw line 2 (main title)
# -------------------------
ctx.set_font_size(font_size_line2)
(x2, y2, w2, h2, dx2, dy2) = ctx.text_extents(line2)

text_x2 = (WIDTH - w2) / 2 - x2
text_y2 = text_y1 + h2 + 28

ctx.move_to(text_x2, text_y2)
ctx.text_path(line2)
ctx.set_source_rgb(*outline_color)
ctx.set_line_width(8)
ctx.stroke_preserve()
ctx.set_source_rgb(*fill_color)
ctx.fill()

# Optional drop shadow (soft)
shadow_offset = 4
ctx.set_font_size(font_size_line2)
ctx.move_to(text_x2 + shadow_offset, text_y2 + shadow_offset)
ctx.text_path(line2)
ctx.set_source_rgba(0, 0, 0, 0.18)
ctx.fill()

# Save
surface.write_to_png("assets/welcome.png")
