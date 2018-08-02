def __hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))

def snap_color(palette, hex):
    min_colours = {}
    r, g, b = __hex_to_rgb(hex)

    for name, color in palette.items():
        r_c, g_c, b_c = __hex_to_rgb(color)
        rd = (r_c - r) ** 2
        gd = (g_c - g) ** 2
        bd = (b_c - b) ** 2
        min_colours[(rd + gd + bd)] = name

    idx = min(min_colours.keys())

    name = min_colours[idx]

    return hex, name

