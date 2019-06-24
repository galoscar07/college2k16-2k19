class ColorFilters:
    filters = {
        "binarizare": "Binarizarea imagini",
        "operatiuni": "Operatiuni de tip fereastra",
        "scaderea": "Scaderea imaginilor"}
    binarizare, operatiuni, scaderea = filters.keys()


def binarizare(img):
    """
    (R, G, B > 127) ? R, G, B = 255 : R, G, B = 0
    """
    pix = img.load()
    for i in range(img.width):
        for j in range(img.height):
            pix[i, j] = (255 if pix[i, j][0] > 127 else 0,
                         255 if pix[i, j][1] > 127 else 0,
                         255 if pix[i, j][2] > 127 else 0)


def operatiuni(img):
    a = 100
    b = 120
    pix = img.load()
    for i in range(img.width):
        for j in range(img.height):
            color = pix[i, j][0]
            if color < a:
                color = 0
            elif color > b:
                color = 0
            pix[i, j] = (2 * color, 2 * color, 2 * color)


def scaderea(img, img_original):
    if not img_original:
        return
    pix = img_original.load()
    pix2 = img.load()
    for i in range(img.width):
        for j in range(img.height):
            pix[i, j] = (pix[i,j][0]-pix2[i,j][0], pix[i,j][1]-pix2[i,j][1], pix[i,j][2]-pix2[i,j][2])

def negative(img):
    """
    R = 255 - R, B = 255 - B, C = 255 - C
    """
    pix = img.load()
    for i in range(img.width):
        for j in range(img.height):
            pix[i, j] = (255 - pix[i, j][0], 255 - pix[i, j][1], 255 - pix[i, j][2])


def color_filter(img, filter_name, img_original=None):
    img_copy = img.copy()
    if filter_name == ColorFilters.binarizare:
        binarizare(img_copy)
    elif filter_name == ColorFilters.operatiuni:
        operatiuni(img_copy)
    elif filter_name == ColorFilters.scaderea:
        scaderea(img_copy, img_original)
    else:
        raise ValueError(f"can't find filter {filter_name}")

    return img_copy
