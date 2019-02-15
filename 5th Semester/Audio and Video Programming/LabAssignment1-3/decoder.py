import numpy as np


class Decoder:
    @staticmethod
    def decode1(lines, columns, blocks, file):
        pixel_matrix = [[[0, 0, 0] for _ in range(columns)] for _ in range(lines)]

        # decode the blocks
        print('Decode 1 - decode blocks')
        for block in blocks:
            Decoder.decode_block(block, pixel_matrix)

        # turn to rgb
        print('Decode 1 - turn to RGB')
        for i in range(lines):
            for j in range(columns):
                pixel_matrix[i][j] = Decoder.yuv_to_rgb(pixel_matrix[i][j])

        # write to file
        print('Decode 1 - write to file')
        Decoder.write_p3(file, lines, columns, pixel_matrix)

    @staticmethod
    def decode2(lines, columns, blocks):
        # dequantization
        print('Decode 2 - dequantization')
        for block in blocks:
            block['data'] = Decoder.dequantization(block['data'])

        print('Decode 2 - inverse DCT')
        # inverse DCT
        for block in blocks:
            block['data'] = Decoder.inverse_dct(block['data'])

        print('Decode 2 - add 128')
        # add 128
        for block in blocks:
            for i in range(8):
                for j in range(8):
                    block['data'][i][j] += 128

        return lines, columns, blocks

    @staticmethod
    def decode3(lines, columns, vector):
        # parse block coefficients from the vector
        print("Decode 3 - parse array into lists of tuples")
        blocks = []
        vector_index = 0
        for l in range(lines)[::8]:
            for c in range(columns)[::8]:
                pos = (l, c)
                block_y = {'position': pos, 'type': 'Y', 'data': []}
                block_u = {'position': pos, 'type': 'U', 'data': []}
                block_v = {'position': pos, 'type': 'V', 'data': []}

                # turn the arrays into tuples here
                block_y['data'], vector_index = Decoder.parse_encoded_block(vector, vector_index)
                block_u['data'], vector_index = Decoder.parse_encoded_block(vector, vector_index)
                block_v['data'], vector_index = Decoder.parse_encoded_block(vector, vector_index)

                blocks.append(block_y)
                blocks.append(block_u)
                blocks.append(block_v)

        # decode the tuple lists
        print("Decode 3 - decode the lists of tuples")
        for block in blocks:
            block['data'] = Decoder.run_length_decoding(block['data'])

        # zig-zag each array to form a matrix
        print("Decode 3 - zig-zag each array to form blocks")
        for block in blocks:
            block['data'] = Decoder.zig_zag(block['data'])

        return lines, columns, blocks

    @staticmethod
    def run_length_decoding(source):
        # dc coefficient
        array = [source[0][1]]

        for ac_tuple in source[1:]:
            if ac_tuple == (0, 0):
                # add the trailing zeroes
                array = array + [0] * (64 - len(array))
                break
            else:
                # add zeroes
                array = array + [0] * ac_tuple[0]
                # add  value
                array.append(ac_tuple[2])

        return array

    @staticmethod
    def parse_encoded_block(vector, vector_index):
        data = []
        dc_coefficient = (vector[vector_index], vector[vector_index + 1])
        data.append(dc_coefficient)
        vector_index += 2

        ac_coefficients = 0
        while ac_coefficients < 63:
            runlength = vector[vector_index]
            size = vector[vector_index + 1]

            # for (0,0)
            if (runlength, size) == (0, 0):
                vector_index += 2
                ac_tuple = (runlength, size)
                data.append(ac_tuple)
                break

            amplitude = vector[vector_index + 2]

            # ac coefficient
            ac_tuple = (runlength, size, amplitude)
            data.append(ac_tuple)
            ac_coefficients += 1
            # zeroes
            ac_coefficients += runlength
            # move forward in the vector
            vector_index += 3

        return data, vector_index

    @staticmethod
    def zig_zag(line):
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

        matrix = [[0 for _ in range(8)] for _ in range(8)]

        for i in range(64):
            pos = order[i]
            matrix[pos[0]][pos[1]] = line[i]
        return matrix

    @staticmethod
    def inverse_dct(coefficients):
        result = [[0 for _ in range(8)] for _ in range(8)]
        for x in range(8):
            for y in range(8):
                value = 1 / 4
                sigmas = 0
                for u in range(8):
                    for v in range(8):
                        sigmas += Decoder.alpha(u) * Decoder.alpha(v) * coefficients[u][v] * \
                                  np.math.cos((2 * x + 1) * u * 3.1415 / 16) * \
                                  np.math.cos((2 * y + 1) * v * 3.1415 / 16)
                value *= sigmas
                result[x][y] = int(value)
        return result

    @staticmethod
    def alpha(n):
        if n == 0:
            return 0.7071
        return 1

    @staticmethod
    def dequantization(matrix):
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
                result[i][j] = int(matrix[i][j] * q[i][j])

        return result

    @staticmethod
    def decode_block(block, pixel_matrix):
        pos = block['position']
        color = None
        if block['type'] == 'Y':
            color = 0
        elif block['type'] == 'U':
            color = 1
        elif block['type'] == 'V':
            color = 2

        for i in range(8):
            for j in range(8):
                pixel_matrix[pos[0] + i][pos[1] + j][color] = block['data'][i][j]

    @staticmethod
    def yuv_to_rgb(pixel):
        y = pixel[0]
        u = pixel[1]
        v = pixel[2]

        r = max(min(int(y + 1.140 * v), 255), 0)
        g = max(min(int(y - 0.395 * u - 0.581 * v), 255), 0)
        b = max(min(int(y + 2.032 * u), 255), 0)

        return [r, g, b]

    @staticmethod
    def write_p3(file, lines, columns, pixel_matrix):
        with open(file, "w") as output:
            output.write("P3\n")
            output.write(str(columns) + " " + str(lines) + "\n")
            output.write("255" + "\n")
            for i in range(lines):
                for j in range(columns):
                    output.write(
                        str(pixel_matrix[i][j][0]) + "\n" + str(pixel_matrix[i][j][1]) + "\n" + str(
                            pixel_matrix[i][j][2]) + "\n")
