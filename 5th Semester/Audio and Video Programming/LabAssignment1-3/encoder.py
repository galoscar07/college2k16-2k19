import numpy as np


class Encoder:
    @staticmethod
    def encode1(file):
        # read header
        print('Encode 1 - read header from file')
        (image_format, lines, columns, max_color, header_length) = Encoder.read_header(file)

        # parse pixels
        print('Encode 1 - parse pixels from file')
        if image_format == "P3":
            (Y, U, V) = Encoder.read_p3(file, lines, columns, header_length)
        else:
            (Y, U, V) = Encoder.read_p6(file, lines, columns, header_length)

        # form blocks
        print('Encode 1 - form blocks')
        blocks = Encoder.form_blocks(Y, U, V, lines, columns)

        return lines, columns, blocks

    @staticmethod
    def encode2(lines, columns, blocks):
        # supersample U and V blocks
        print('Encode 2 - supersample U and V blocks')
        for block in blocks:
            if block['type'] != 'Y':
                block['data'] = Encoder.supersample(block['data'])

        # subtract 128
        print('Encode 2 - subtract 128')
        for block in blocks:
            for i in range(8):
                for j in range(8):
                    block['data'][i][j] -= 128

        # forward DCT
        print('Encode 2 - forward DCT')
        for block in blocks:
            block['data'] = Encoder.forward_dct(block['data'])

        # quantization
        print('Encode 2 - quantization')
        for block in blocks:
            block['data'] = Encoder.quantization(block['data'])

        return lines, columns, blocks

    @staticmethod
    def encode3(lines, columns, blocks):
        # zig-zag each matrix to form a 1d array
        print("Encode 3 - zig-zag each matrix")
        for block in blocks:
            block['data'] = Encoder.zig_zag(block['data'])

        # run-length encode each array
        print("Encode 3 - run-length encode each array")
        for block in blocks:
            block['data'] = Encoder.run_length_encoding(block['data'])

        # add all the arrays
        print("Encode 3 - concatenate all the arrays")
        vector = []
        for block in blocks:
            vector += block['data']

        return lines, columns, vector

    @staticmethod
    def run_length_encoding(array):
        result = []

        size_amplitude = {1: (0, 1), 2: (2, 3), 3: (4, 7), 4: (8, 15), 5: (16, 31), 6: (32, 63), 7: (64, 127),
                          8: (128, 255), 9: (256, 511), 10: (512, 1023)}

        dc_amplitude = array[0]
        dc_size = 0

        for k, v in size_amplitude.items():
            if v[0] <= np.abs(dc_amplitude) <= v[1]:
                dc_size = k
                break

        result.append(dc_size)
        result.append(dc_amplitude)

        zeroes = 0
        for i in array[1:]:
            if i == 0:
                zeroes += 1
                continue
            runlength = zeroes
            zeroes = 0
            amplitude = i
            size = 0
            for k, v in size_amplitude.items():
                if v[0] <= np.abs(amplitude) <= v[1]:
                    size = k
                    break
            result.append(runlength)
            result.append(size)
            result.append(amplitude)

        if zeroes > 0:
            result.append(0)
            result.append(0)

        return result

    @staticmethod
    def zig_zag(matrix):
        # https://en.wikipedia.org/wiki/Precomputation
        order = [(0, 0),
                 (0, 1), (1, 0),
                 (2, 0), (1, 1), (0, 2),
                 (0, 3), (1, 2), (2, 1), (3, 0),
                 (4, 0), (3, 1), (2, 2), (1, 3), (0, 4),
                 (0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0),
                 (6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6),
                 (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0),
                 (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7),
                 (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2),
                 (7, 3), (6, 4), (5, 5), (4, 6), (3, 7),
                 (4, 7), (5, 6), (6, 5), (7, 4),
                 (7, 5), (6, 6), (5, 7),
                 (6, 7), (7, 6),
                 (7, 7)]

        line = []
        for pos in order:
            line.append(matrix[pos[0]][pos[1]])

        return line

    @staticmethod
    def quantization(matrix):
        result = [[0 for _ in range(8)] for _ in range(8)]
        q = [[6, 4, 4, 6, 10, 16, 20, 24],
             [5, 5, 6, 8, 10, 23, 24, 22],
             [6, 5, 6, 10, 16, 23, 28, 22],
             [6, 7, 9, 12, 20, 35, 32, 25],
             [7, 9, 15, 22, 27, 44, 41, 31],
             [10, 14, 22, 26, 32, 42, 45, 37],
             [20, 26, 31, 35, 41, 48, 48, 40],
             [29, 37, 38, 39, 45, 40, 41, 40]]

        for i in range(8):
            for j in range(8):
                result[i][j] = int(matrix[i][j] / q[i][j])

        return result

    @staticmethod
    def supersample(matrix):
        data = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(4):
            for j in range(4):
                data[2 * i][2 * j] = matrix[i][j]
                data[2 * i + 1][2 * j] = matrix[i][j]
                data[2 * i][2 * j + 1] = matrix[i][j]
                data[2 * i + 1][2 * j + 1] = matrix[i][j]
        return data

    @staticmethod
    def forward_dct(source):
        result = [[0 for _ in range(8)] for _ in range(8)]
        for u in range(8):
            for v in range(8):
                coefficient = 1 / 4 * Encoder.alpha(u) * Encoder.alpha(v)
                sigmas = 0
                for x in range(8):
                    for y in range(8):
                        sigmas += source[x][y] * np.math.cos((2 * x + 1) * u * 3.1415 / 16) * \
                                  np.math.cos((2 * y + 1) * v * 3.1415 / 16)
                coefficient *= sigmas
                result[u][v] = coefficient
        return result

    @staticmethod
    def alpha(n):
        if n == 0:
            return 0.7071
        return 1

    @staticmethod
    def read_header(file):
        header_length = 0
        with open(file, "r", errors="ignore") as f:
            line = f.readline()
            header_length += 1
            # type (P3 or P6)
            while line:
                if not line.startswith("#"):
                    break
                line = f.readline()
                header_length += 1
            if "P3" in line.upper():
                image_format = "P3"
            else:
                image_format = "P6"
            # dimensions
            line = f.readline()
            header_length += 1
            while line:
                if not line.startswith("#"):
                    break
                line = f.readline()
                header_length += 1
            (columns, lines) = line.split()
            columns = int(columns)
            lines = int(lines)
            # max color value
            line = f.readline()
            header_length += 1
            while line:
                if not line.startswith("#"):
                    break
                line = f.readline()
                header_length += 1
            # max color (usually 255)
            max_color = int(line.strip())
        return image_format, lines, columns, max_color, header_length

    @staticmethod
    def read_p3(file, lines, columns, header_length):
        y = [[0 for _ in range(columns)] for _ in range(lines)]
        u = [[0 for _ in range(columns)] for _ in range(lines)]
        v = [[0 for _ in range(columns)] for _ in range(lines)]

        with open(file, "r") as file:
            for _ in range(header_length):
                file.readline()

            for i in range(lines):
                for j in range(columns):
                    r = int(file.readline())
                    g = int(file.readline())
                    b = int(file.readline())

                    y[i][j] = Encoder.compute_y(r, g, b)
                    u[i][j] = Encoder.compute_u(r, g, b)
                    v[i][j] = Encoder.compute_v(r, g, b)

        return y, u, v

    @staticmethod
    def read_p6(file, lines, columns, header_length):
        y = [[0 for _ in range(columns)] for _ in range(lines)]
        u = [[0 for _ in range(columns)] for _ in range(lines)]
        v = [[0 for _ in range(columns)] for _ in range(lines)]

        s = header_length
        with open(file, "rb") as file:
            while s > 0:
                if file.read(1) == b'\n':
                    s -= 1

            for i in range(lines):
                for j in range(columns):
                    r = int.from_bytes(file.read(1), byteorder="big")
                    g = int.from_bytes(file.read(1), byteorder="big")
                    b = int.from_bytes(file.read(1), byteorder="big")

                    y[i][j] = Encoder.compute_y(r, g, b)
                    u[i][j] = Encoder.compute_u(r, g, b)
                    v[i][j] = Encoder.compute_v(r, g, b)

        return y, u, v

    @staticmethod
    def form_blocks(y, u, v, l, c):
        blocks = []

        positions = [(i, j) for i in range(l)[::8] for j in range(c)[::8]]

        for p in positions:
            blocks.append(Encoder.compute_y_block(y, p))
            blocks.append(Encoder.compute_u_block(u, p))
            blocks.append(Encoder.compute_v_block(v, p))

        return blocks

    @staticmethod
    def compute_y_block(y, position):
        block = {'type': 'Y', 'position': position}
        data = [[0 for _ in range(8)] for _ in range(8)]

        for i in range(8):
            for j in range(8):
                data[i][j] = y[i + position[0]][j + position[1]]

        block['data'] = data
        return block

    @staticmethod
    def compute_u_block(matrix, position):
        block = {'type': 'U', 'position': position}
        data = [[0 for _ in range(4)] for _ in range(4)]

        lin = position[0]
        col = position[1]
        for i in range(4):
            for j in range(4):
                data[i][j] = int((matrix[lin + 2 * i][col + 2 * j] + matrix[lin + 2 * i][col + 2 * j + 1] +
                                  matrix[lin + 2 * i + 1][col + 2 * j] + matrix[lin + 2 * i + 1][col + 2 * j + 1]) / 4)

        block['data'] = data
        return block

    @staticmethod
    def compute_v_block(matrix, position):
        block = {'type': 'V', 'position': position}
        data = [[0 for _ in range(4)] for _ in range(4)]

        lin = position[0]
        col = position[1]
        for i in range(4):
            for j in range(4):
                data[i][j] = (matrix[lin + 2 * i][col + 2 * j] + matrix[lin + 2 * i][col + 2 * j + 1] +
                              matrix[lin + 2 * i + 1][col + 2 * j] + matrix[lin + 2 * i + 1][col + 2 * j + 1]) / 4

        block['data'] = data
        return block

    @staticmethod
    def compute_y(r, g, b):
        y = 0.299 * r + 0.587 * g + 0.114 * b
        return int(y)

    @staticmethod
    def compute_u(r, g, b):
        y = Encoder.compute_y(r, g, b)
        u = 0.492 * (b - y)
        return int(u)

    @staticmethod
    def compute_v(r, g, b):
        y = Encoder.compute_y(r, g, b)
        v = 0.877 * (r - y)
        return int(v)
