
WIDTH  = 320
HEIGHT  =  240
INDEX_WIDTH = int(WIDTH/2)

hds2xx_lv_colors = []

hds2xx_colors_565 = [
    0xffff, # [00] None
    0xffff, # [01] white
    0x0000, # [02] black

    0x2A4A, # [03] Window background color
    0x10a3, # [04] Info box background color
    0xFF20, # [05] Channel 1 color
    0x6E3E, # [06] Channel 2 color
    0x07e0, # [07] green00FF00
    0xCE9B, # [08] Wave grid color
    0xF8E0, # [09] redff0000
    0x4A69, # [10] channel off color

    0x21C7, # [11] ag main panel color
    0xAD75, # [12] ag status bar color
    0xFBE4, # [13] orange
    0x17DE, # [14] cyan
    0xb5b6, # [15]
    0xb9f7,
    0x42f1,
    0x1905,
    0x4a69,
    0x2124,
    0xA3DF
]


print("start..")

def get_rgb888_from_rgb565(rgb565):
    r = (rgb565 & 0xf800) >> 8
    g = (rgb565 & 0x07e0) >> 3
    b = (rgb565 & 0x001f) << 3
    return r, g, b


for color in hds2xx_colors_565:
    r, b, g = get_rgb888_from_rgb565(color)
    lv_color = lv.color_make(0x55, 0x55, 0x55)
    lv_color.ch.red = r
    lv_color.ch.blue = b
    lv_color.ch.green = g
    hds2xx_lv_colors.append(lv_color)


cbuf = bytearray(WIDTH * HEIGHT  * 4)
canvas = lv.canvas(lv.scr_act())
canvas.set_buffer(cbuf, WIDTH, HEIGHT , lv.img.CF.TRUE_COLOR)
canvas.center()


ui_buf = []
i = 0
y_half = int(HEIGHT / 2)
for y in range(0, HEIGHT):
    for x in range(0, INDEX_WIDTH):
        if (y < y_half):
            ui_buf.append(0x33)
        else:
            ui_buf.append(0x88)

for y in range(0,HEIGHT):
    for x in range(0, INDEX_WIDTH):
        color_index = ui_buf[y*INDEX_WIDTH + x]
        color_index_0 = color_index >> 4
        color_index_1 = color_index & 0x0f

        canvas.set_px(2*x, y, hds2xx_lv_colors[color_index_0])
        canvas.set_px(2*x+1, y, hds2xx_lv_colors[color_index_1])

