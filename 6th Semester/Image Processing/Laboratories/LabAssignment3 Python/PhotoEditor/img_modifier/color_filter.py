from scipy.interpolate import interp1d

from map import mapluminance


class ColorFilters:
    filters = {
        "median_filter": "Median Filter",
        "contour": "Accentuarea Contururilor",
        "pseudo": "Pseudo Colorarea Imaginilor Medicale"}
    median_filter, contour, pseudo = filters.keys()


def median_filter(img):
    final = img.copy()
    pix = img.load()
    pix_final = img.load()
    members = [pix[0, 0]] * 9
    for y in range(1, img.width - 1):
        for x in range(1, img.height - 1):
            members[0] = pix[y - 1, x - 1]
            members[1] = pix[y, x - 1]
            members[2] = pix[y + 1, x - 1]
            members[3] = pix[y - 1, x]
            members[4] = pix[y, x]
            members[5] = pix[y + 1, x]
            members[6] = pix[y - 1, x + 1]
            members[7] = pix[y, x + 1]
            members[8] = pix[y + 1, x + 1]

            members.sort()
            pix_final[y, x] = members[4]
    for i in range(img.width):
        for j in range(img.height):
            pix[i,j] = pix_final[i,j]


def pseudo(img):
    """
    We have a map of colors, then we compute the luminance and then we interpolate the value of the luminance in order
    to find out the value that it is supposed to have
    """
    map = {
        0: (0, 0, 128),  # (darkblue)
        0.25: (0, 255, 0),  # (green)
        0.5: (255, 255, 0),  # (yellow)
        0.75: (255, 128, 0),  # (orange)
        1.0: (255, 0, 0)  # (red)
    }
    pix = img.load()
    for i in range(img.width):
        for j in range(img.height):
            L = ((0.21 * pix[i, j][0]) + (0.72 * pix[i, j][1]) + (0.07 * pix[i, j][2])) / 255
            L = "{0:.2f}".format(L)
            L = float(L)
            pix[i,j] = (mapluminance[L][0], mapluminance[L][1], mapluminance[L][2])
            # l0 = [0, 0.25, 0.5, 0.75, 1]
            # R0 = [0, 0, 255, 255, 255]
            # G0 = [0, 255, 255, 128, 0]
            # B0 = [128, 0, 0, 0, 0]
            # R = interp1d(l0, R0, kind='cubic')
            # G = interp1d(l0, G0, kind='cubic')
            # B = interp1d(l0, B0, kind='cubic')
            # if L == 0:
            #     pix[i, j] = map[0]
            # elif L == 0.25:
            #     pix[i, j] = map[0.25]
            # elif L == 0.5:
            #     pix[i, j] = map[0.5]
            # elif L == 0.75:
            #     pix[i, j] = map[0.75]
            # elif L == 1:
            #     pix[i, j] = map[1.0]
            # else:
            #     pix[i, j] = (R(L), G(L), B(L))


def contour(img):
    l = 5
    pix = img.load()
    img_copy = img.copy()
    pix_filtered = img_copy.load()
    for i in range(img.width):
        for j in range(img.height):
            s = sum(pix_filtered[i, j]) // 3
            pix_filtered[i, j] = (s, s, s)

    for i in range(img.width):
        for j in range(img.height):
            ur = pix[i, j][0]
            fr = pix_filtered[i, j][0]
            vr = ur + int(l * (ur-fr))
            if vr < 0:
                vr = 0
            elif vr > 255:
                vr = 255

            ug = pix[i, j][1]
            fg = pix_filtered[i, j][1]
            vg = ug + int(l * (ug - fg))
            if vg < 0:
                vg = 0
            elif vg > 255:
                vg = 255

            ub = pix[i, j][0]
            fb = pix_filtered[i, j][0]
            vb = ub + int(l * (ub - fb))
            if vb < 0:
                vb = 0
            elif vb > 255:
                vb = 255
            pix[i, j] = (vr, vg, vb)


def color_filter(img, filter_name):
    img_copy = img.copy()
    if filter_name == ColorFilters.median_filter:
        median_filter(img_copy)
    elif filter_name == ColorFilters.contour:
        contour(img_copy)
    elif filter_name == ColorFilters.pseudo:
        pseudo(img_copy)
    else:
        raise ValueError(f"can't find filter {filter_name}")

    return img_copy
