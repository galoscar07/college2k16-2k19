class ColorFilters:
    filters = {"negative": "Negative", "grey_scale": "Grayscale", 'primary_filter': 'Primary', 'red': 'Red'}
    NEGATIVE, GRAY_SCALE, PRIMARY_FILTER, RED = filters.keys()


def gray_scale(img):
    """
    Create average A = (R+G+B)/3 then => R=A, B=A, C=A
    """
    pix = img.load()
    for i in range(img.width):
        for j in range(img.height):
            s = sum(pix[i, j]) // 3
            pix[i, j] = (s, s, s)


def red(img):
    """
    R = R, B = B * 0,1, G = G * 0.1
    """
    pix = img.load()
    for i in range(img.width):
        for j in range(img.height):
            pix[i, j] = (pix[i, j][0], int(pix[i, j][1] * 0.1), int(pix[i, j][2] * 0.1))


def negative(img):
    """
    R = 255 - R, B = 255 - B, C = 255 - C
    """
    pix = img.load()
    for i in range(img.width):
        for j in range(img.height):
            pix[i, j] = (255 - pix[i, j][0], 255 - pix[i, j][1], 255 - pix[i, j][2])


def primary_filter(img):
    """
    If R/G/B > 127 => R/G/B = 255 else R/G/B=0
    """
    pix = img.load()
    for i in range(img.width):
        for j in range(img.height):
            pix[i, j] = (255 if pix[i, j][0] > 127 else 0, 255 if pix[i, j][1] > 127 else 0,
                         255 if pix[i, j][2] > 127 else 0)


def color_filter(img, filter_name):
    img_copy = img.copy()
    if filter_name == ColorFilters.NEGATIVE:
        negative(img_copy)
    elif filter_name == ColorFilters.GRAY_SCALE:
        gray_scale(img_copy)
    elif filter_name == ColorFilters.PRIMARY_FILTER:
        primary_filter(img_copy)
    elif filter_name == ColorFilters.RED:
        red(img_copy)
    else:
        raise ValueError(f"can't find filter {filter_name}")

    return img_copy
