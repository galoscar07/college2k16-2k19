from decoder import Decoder
from encoder import Encoder

if __name__ == '__main__':
    # Encode
    (lines, columns, blocks) = Encoder.encode1("nt-P6.ppm")
    (lines, columns, blocks) = Encoder.encode2(lines, columns, blocks)
    (lines, columns, vector) = Encoder.encode3(lines, columns, blocks)

    # Decode
    (lines, columns, blocks) = Decoder.decode3(lines, columns, vector)
    (lines, columns, blocks) = Decoder.decode2(lines, columns, blocks)
    Decoder.decode1(lines, columns, blocks, "out.ppm")
