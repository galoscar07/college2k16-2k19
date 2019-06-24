import sys

from PyQt5.QtWidgets import QApplication
from scipy.interpolate import interp1d

from photo_editor import EasyPzUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = EasyPzUI()
    sys.exit(app.exec_())


    # i = 0.01
    # while i <= 1:
    #     l0 = [0, 0.25, 0.5, 0.75, 1]
    #     R0 = [0, 0, 255, 255, 255]
    #     G0 = [0, 255, 255, 128, 0]
    #     B0 = [128, 0, 0, 0, 0]
    #     R = interp1d(l0, R0, kind='cubic')
    #     G = interp1d(l0, G0, kind='cubic')
    #     B = interp1d(l0, B0, kind='cubic')
    #     f = open("map.py", "a")
    #     red = R(i)
    #     green = G(i)
    #     blue = B(i)
    #     if red < 0:
    #         red = 0
    #     elif red > 255:
    #         red = 255
    #
    #     if green < 0:
    #         green = 0
    #     elif green > 255:
    #         green = 255
    #
    #     if blue < 0:
    #         blue = 0
    #     elif blue > 255:
    #         blue = 255
    #     red = "{0:.0f}".format(red) if type(red) != int else red
    #     green = "{0:.0f}".format(green) if type(green) != int else green
    #     blue = "{0:.0f}".format(blue) if type(blue) != int else blue
    #     f = open("map.py", "a")
    #     f.write("%s: (%s, %s, %s), \n" % ("{0:.2f}".format(i), red, green, blue))
    #     i += 0.01
    # f.close()
